from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from orders.models import Order


@csrf_exempt
def payment_success(request):
    transaction_id = request.POST.get('tran_id')
    order = get_object_or_404(Order, transaction_id=transaction_id)
    order.is_paid = True
    order.save()
    order.photo.uploader = order.user.profile
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
