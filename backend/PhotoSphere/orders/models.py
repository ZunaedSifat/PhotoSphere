from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.db.models.signals import post_save

from photos.models import Photo
from orders import sslcommerze


def get_valid_till():
    return datetime.now() + timedelta(minutes=30)


class Order(models.Model):
    transaction_id = models.UUIDField(
        max_length=36, default=uuid4, editable=False, unique=True)
    photo = models.ForeignKey(
        to=Photo, on_delete=models.PROTECT, related_name='order')
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.PROTECT, blank=True)

    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=127)

    is_paid = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    redirection_url = models.URLField(blank=True)

    # todo: validate the order

    def __str__(self):
        return f'Order for {self.photo.title} by {self.user.get_full_name()}'

    def get_transaction(self):
        print('hello world')
        return sslcommerze.SSLPaymentSessionGenerator(
            transaction_id=self.transaction_id,
            total_amount=self.photo.price,
            is_sandbox=True
        ).add_customer_details(
            name=self.user.get_full_name() or "Admin User",
            phone=self.phone,
            email=self.user.email,
            address=self.address,
            city=self.city,
            country='Bangladesh'
        ).add_product_details(
            name=self.photo.title
        ).get_session()


def add_redirection_url(sender, instance, created, **kwargs):
    print('before create')
    if created:
        print('after create')
        instance.redirection_url = instance.get_transaction().get('GatewayPageURL')
        instance.save()
        print('after save')


post_save.connect(add_redirection_url, sender=Order)
