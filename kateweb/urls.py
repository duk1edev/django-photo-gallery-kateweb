from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('photo/', views.albums, name='photos'),
    path('contacts/', views.contacts, name='contacts'),
    path('albums/', views.AlbumsViewPage.as_view(), name='albums'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<slug>', views.AlbumDetail.as_view(), name='album-detail'),
    path('process/', views.process, name='process')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
