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

        try:
            remove_my = int(params.get('remove_my'))
            if remove_my:
                queryset = queryset.filter(~Q(uploader__user=self.request.user))
        except:
            pass

        for_sale = params.get('for_sale') == '1'
        if for_sale:
            queryset = queryset.filter(for_sale=for_sale)

        return queryset


class PhotoDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (PhotoDetailsPermission, )
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    def perform_update(self, serializer):
        serializer.save(uploader=self.request.user.profile)
