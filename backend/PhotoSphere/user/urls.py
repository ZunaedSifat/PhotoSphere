from django.urls import path
from user import views

urlpatterns = [
    path('', views.ProfileListAPIView.as_view(), name='list_profile'),
    path('<int:pk>/', views.ProfileRetrieveView.as_view(), name='profile_details'),
    path('me/', views.MyProfileView.as_view(), name='my_profile'),
    path('following/', views.FollowingListAPIView.as_view(), name='following_list'),
    path('follower/', views.FollowerListAPIView.as_view(), name='follower_list'),
    path('follow/<int:pk>/', views.FollowAPIView.as_view(), name='add_remove_follow'),
]
