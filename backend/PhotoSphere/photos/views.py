from rest_framework import generics

from photos.serializers import PhotoSerializer
from photos.models import Photo
from photos.permissions import PhotoDetailsPermission, PhotoListCreatePermission


class PhotoListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (PhotoListCreatePermission, )
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

        return queryset


class PhotoDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (PhotoDetailsPermission, )
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    def perform_update(self, serializer):
        serializer.save(uploader=self.request.user.profile)
