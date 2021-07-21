from django.urls import path
from exhibitions import views


urlpatterns = [
    path('', views.ExhibitionListCreateAPIView.as_view(), name='exhibition_list_create'),
    path('<int:pk>/', views.ExhibitionRetrieveUpdateDestroyAPIView.as_view(), name='exhibition_details'),
]
