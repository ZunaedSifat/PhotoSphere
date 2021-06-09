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


class PhotoDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (PhotoDetailsPermission, )
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    def perform_update(self, serializer):
        serializer.save(uploader=self.request.user.profile)
