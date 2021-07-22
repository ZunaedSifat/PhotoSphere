import datetime

from django.db.models import Q
from rest_framework import generics, views, status, response, exceptions
from rest_framework.permissions import IsAuthenticated

from photos.serializers import PhotoSerializer, TagSerializer
from photos.models import Photo, Tag
from photos.permissions import PhotoDetailsPermission, ListCreatePermission


class PhotoListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (ListCreatePermission,)
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user.profile)

    def filter_queryset(self, queryset):
        query_params = self.request.query_params

        try:
            user = int(query_params['user'])
            queryset = queryset.filter(uploader__user=user)
        except:
            pass

        try:
            remove_my = query_params['remove_my'] != 'false'
            if remove_my:
                queryset = queryset.filter(~Q(uploader__user=self.request.user))
        except:
            pass

        try:
            for_sale = query_params['for_sale'] != 'false'
            queryset = queryset.filter(for_sale=for_sale)
        except:
            pass

        try:
            is_digital = query_params['is_digital'] != 'false'
            queryset = queryset.filter(is_digital=is_digital)
        except:
            pass

        try:
            time_low = datetime.datetime.fromisoformat(query_params['time_low'])
            queryset = queryset.filter(created_at__gte=time_low)
        except:
            pass

        try:
            time_hi = datetime.datetime.fromisoformat(query_params['time_hi'])
            queryset = queryset.filter(created_at__lte=time_hi)
        except:
            pass

        try:
            print('came here')
            print(self.request.user, self.request.user.profile.following_list.all())

            following = int(query_params['following'])
            print(following, self.request.user, self.request.user.profile.following_list.all())
            query = Q(uploader__user__in=self.request.user.profile.following_list.all())
            queryset = queryset.filter(query if following else ~query)
        except:
            pass

        try:
            queryset = queryset.order_by(query_params['order_by'])
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

class TagListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (ListCreatePermission,)
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

