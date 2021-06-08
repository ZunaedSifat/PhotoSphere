from django.urls import path
from user import views

urlpatterns = [
    path('', views.ProfileListAPIView.as_view(), name='list_profile'),
    path('me/', views.MyProfileView.as_view(), name='my_profile'),
    path('<int:pk>/', views.ProfileRetrieveView.as_view(), name='profile_details'),
]
