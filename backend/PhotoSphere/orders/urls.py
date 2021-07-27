from django.urls import path
from orders import views


urlpatterns = [
    path('', views.OrderListCreateAPIView.as_view(), name='order_list_create'),
    path('<int:pk>/', views.OrderRetrieveAPIView.as_view(), name='order_retrieve'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/failed/', views.payment_failed, name='payment_failed'),
    path('payment/canceled/', views.payment_canceled, name='payment_canceled'),
]
