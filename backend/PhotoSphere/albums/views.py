from rest_framework import generics
from albums.serializers import AlbumSerializer
from albums.models import Album
from photos.permissions import ListCreatePermission
from albums.permissions import AlbumDetailsPermission


class AlbumListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (ListCreatePermission, )
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)

    # todo: add privacy filter


class AlbumDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AlbumDetailsPermission, )
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user.profile)
