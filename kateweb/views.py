from django.shortcuts import render
from .models import MyInfo, Album, AlbumImage
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def process(request):
    return render(request, 'kateweb/process.html')


def albums(request):
    return render(request, 'kateweb/photo.html')


def contacts(request):
    return render(request, 'kateweb/contacts.html')

def process(request):
    return render(request, 'kateweb/process.html')


class HomePage(ListView):
    model = MyInfo
    template_name = 'kateweb/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Kate Friday photographer'
        ctx['albums_0_3'] = Album.objects.filter(id__lte=3).order_by('created')
        ctx['albums_4_6'] = list(Album.objects.filter(id__gt=3).order_by('created'))[:3:]
        ctx['albums_7_10'] = list(Album.objects.filter(id__gt=6).order_by('created'))[:3:]
        return ctx


class AlbumsViewPage(ListView):
    model = Album
    template_name = 'kateweb/gallery.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(AlbumsViewPage, self).get_context_data(**kwargs)

        ctx['title'] = 'Kate Friday albums'
        return ctx


def gallery(request):
    list = Album.objects.filter(is_visible=True).order_by('created')

    return render(request, 'kateweb/gallery.html', {'albums': list})


class AlbumDetail(DetailView):
    model = Album
    template_name = 'kateweb/album-detail.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        # context['title'] = AlbumImage.objectc.filter(album=se)
        return context
