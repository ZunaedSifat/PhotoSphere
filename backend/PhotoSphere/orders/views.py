from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import AllowAny

from photos.permissions import ListCreatePermission
from orders.models import Order
from orders.serializers import OrderSerializer


@csrf_exempt
def payment_success(request):
    transaction_id = request.POST.get('tran_id')
    order = get_object_or_404(Order, transaction_id=transaction_id)
    order.is_paid = True
    order.save()
    order.photo.owner = order.user.profile
    order.photo.for_sale = False
    order.photo.save()
    return HttpResponseRedirect(redirect_to=f'http://localhost:8080/payment/success/{order.id}')


@csrf_exempt
def payment_failed(request):
    transaction_id = request.POST.get('tran_id')
    order = get_object_or_404(Order, transaction_id=transaction_id)
    return HttpResponseRedirect(redirect_to=f'http://localhost:8080/payment/fail/{order.id}')


@csrf_exempt
def payment_canceled(request):
    transaction_id = request.POST.get('tran_id')
    order = get_object_or_404(Order, transaction_id=transaction_id)
    return HttpResponseRedirect(redirect_to=f'http://localhost:8080/payment/cancel/{order.id}')


class OrderListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (ListCreatePermission, )
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        print("Came to perform create")
        print(f'Request user: {self.request.user}')
        serializer.save(user=self.request.user)


class OrderRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
