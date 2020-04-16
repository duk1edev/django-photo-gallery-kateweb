import os
import uuid

from django.contrib import admin
from django.core.files.base import ContentFile
import phfriday.settings
from .models import MyInfo, Album, AlbumImage
from .forms import AlbumForm
# Register your models here.
admin.site.register(MyInfo)
# admin.site.register(Album)
# admin.site.register(AlbumImage)
from datetime import datetime
import zipfile
from PIL import Image

@admin.register(Album)
class AlbumModelAdmin(admin.ModelAdmin):
    form = AlbumForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id','title', 'thumb')
    list_filter = ('created', )

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            album = form.save(commit=False)
            album.modified = datetime.now()
            album.save()

            if form.cleaned_data['zip'] != None:
                zip = zipfile.ZipFile(form.cleaned_data['zip'])
                for filename in sorted(zip.namelist()):

                    file_name = os.path.basename(filename)
                    if not file_name:
                        continue

                    data = zip.read(filename)
                    contentfile = ContentFile(data)

                    img = AlbumImage()
                    img.album = album
                    img.alt = filename
                    filename = "{0}{1}.jpg".format(album.slug, str(uuid.uuid4())[-13:])
                    img.image.save(filename, contentfile)

                    filepath = '{0}/albums/{1}'.format(phfriday.settings.MEDIA_ROOT, filename)
                    with Image.open(filepath) as i:
                        img.width, img.height = i.size

                    img.thumb.save('thumb-{0}'.format(filename), contentfile)
                    img.save()
                zip.close()
            super(AlbumModelAdmin, self).save_model(request, obj, form, change)


@admin.register(AlbumImage)
class AlbumImageModelAdmin(admin.ModelAdmin):
    list_display = ('alt', 'album')
    list_filter = ('album', 'created')


