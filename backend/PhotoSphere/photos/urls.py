from django.urls import path
from photos import views

urlpatterns = [
    path('', views.PhotoListCreateAPIView.as_view(), name='list_create_photo'),
    path('<int:pk>/', views.PhotoDetailsAPIView.as_view(), name='photo_details'),
    path('like/<int:pk>/', views.PhotoLikeView.as_view(), name='photo_like_view'),
]
