from django.urls import path
from albums import views


urlpatterns = [
    path('', views.AlbumListCreateAPIView.as_view(), name='album_list_create'),
    path('<int:pk>/', views.AlbumDetailsAPIView.as_view(), name='album_details'),
]
