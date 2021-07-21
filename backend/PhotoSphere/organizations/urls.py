from django.urls import path
from organizations import views


urlpatterns = [
    path('', views.OrganizationListCreateAPIView.as_view(), name='organization_list_create'),
]
