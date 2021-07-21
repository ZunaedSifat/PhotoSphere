from django.urls import path
from organizations import views


urlpatterns = [
    path('', views.OrganizationListCreateAPIView.as_view(), name='organization_list_create'),
    path('<int:pk>/', views.OrganizationRetrieveUpdateDestroyAPIView.as_view(), name='organization_details'),
    path('member/', views.OrganizationMemberListCreateAPIView.as_view(), name='organization_member_list_create'),
    path('member/<int:pk>/', views.OrganizationMemberRetrieveUpdateDestroyAPIView.as_view(), name='organization_member_details'),
]
