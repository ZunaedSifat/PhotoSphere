import datetime

from django.db.models import Q
from rest_framework import generics, views, status, response, exceptions
from rest_framework.permissions import IsAuthenticated

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


class PhotoLikeView(views.APIView):
    permission_classes = (IsAuthenticated, )  # todo: privacy permission

    def get_photo(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except:
            raise exceptions.NotFound({'msg': 'No photo found with this ID'})

    def get(self, request, pk, format=None):
        photo = self.get_photo(pk=pk)
        likes = [user.id for user in photo.likes.all()]
        return response.Response(
            data={'likes': likes},
            status=status.HTTP_200_OK
        )

    def post(self, request, pk, format=None):
        photo = self.get_photo(pk=pk)
        photo.add_like(self.request.user)
        return response.Response(
            data={'msg': 'Liked the photo'},
            status=status.HTTP_200_OK
        )

    def delete(self, request, pk, format=None):
        photo = self.get_photo(pk=pk)
        photo.remove_like(self.request.user)
        return response.Response(
            data={'msg': 'Removed like from photo'},
            status=status.HTTP_200_OK
        )
