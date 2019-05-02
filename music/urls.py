from django.urls import path
from music import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.home, name='index'),
    # path('<int:album_id>/', views.detail, name='detail'),
    # path('<int:album_id>/favorite/', views.favorite, name='favorite'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('album/add/', views.AlbumCreateView.as_view(), name='album-add'),
    path('<int:pk>/album_id/', views.DetailView.as_view(), name='album-update'),
    path('<int:pk>/delete', views.DetailView.as_view(), name='delete_album'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)