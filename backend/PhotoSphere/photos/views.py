import datetime

from django.db.models import Q
from rest_framework import generics

from photos.serializers import PhotoSerializer
from photos.models import Photo
from photos.permissions import PhotoDetailsPermission, ListCreatePermission


class PhotoListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (ListCreatePermission,)
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user.profile)

    def filter_queryset(self, queryset):
        params = self.request.query_params
        if 'user' in params:
            try:
                user = int(params.get('user'))
                queryset = queryset.filter(uploader__user=user)
            except:
                pass

        if 'remove_my' in params:
            remove_my = params.get('remove_my') != 'false'
            if remove_my:
                queryset = queryset.filter(~Q(uploader__user=self.request.user))

        if 'for_sale' in params:
            for_sale = params.get('for_sale') != 'false'
            queryset = queryset.filter(for_sale=for_sale)

        if 'is_digital' in params:
            is_digital = params.get('is_digital') != 'false'
            queryset = queryset.filter(is_digital=is_digital)

        if 'time_low' in params:
            time_low = datetime.datetime.fromisoformat(params.get('time_low'))
            queryset = queryset.filter(created_at__gte=time_low)

        if 'time_hi' in params:
            time_hi = datetime.datetime.fromisoformat(params.get('time_hi'))
            queryset = queryset.filter(created_at__lte=time_hi)

        if 'order_by' in params:
            try:
                queryset = queryset.order_by(params.get('order_by'))
            except:
                pass

        return queryset


class PhotoDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (PhotoDetailsPermission, )
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    def perform_update(self, serializer):
        serializer.save(uploader=self.request.user.profile)
