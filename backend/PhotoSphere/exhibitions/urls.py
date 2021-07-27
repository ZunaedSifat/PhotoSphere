from django.urls import path
from exhibitions import views


urlpatterns = [
    path('', views.ExhibitionListCreateAPIView.as_view(), name='exhibition_list_create'),
    path('<int:pk>/', views.ExhibitionRetrieveUpdateDestroyAPIView.as_view(), name='exhibition_details'),
    path('entry/', views.ExhibitionEntryListCreateAPIView.as_view(), name='exhibition_entry_list_create'),
    path('entry/<int:pk>/', views.ExhibitionEntryRetrieveUpdateDestroyAPIView.as_view(), name='exhibition_entry_details'),
    path('theme/', views.ThemeListCreateAPIView.as_view(), name='theme_list_create'),
    path('theme/<int:pk>/', views.ThemeRetrieveAPIView.as_view(), name='theme_retrieve'),
]
