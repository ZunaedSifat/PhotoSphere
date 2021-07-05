from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, views, response, status

from user.serializers import ProfileSerializer, ProfileCreationSerializer
from user.models import Profile
from user.permissions import ProfileListCreatePermission


class ProfileListAPIView(generics.ListCreateAPIView):
    permission_classes = (ProfileListCreatePermission, )
    queryset = Profile.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProfileSerializer
        return ProfileCreationSerializer


class ProfileRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class MyProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile


class FollowingListAPIView(views.APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        following = request.user.profile.following_list.all()
        return response.Response(
            data={'following': following},
            status=status.HTTP_200_OK
        )

class FollowerListAPIView(views.APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        followers = request.user.follower_list.all()
        return response.Response(
            data={'followers': followers},
            status=status.HTTP_200_OK
        )

class FollowAPIView(views.APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, pk, format=None):
        to_follow = int(self.kwargs.get('pk'))
        if to_follow == self.request.user.id:
            return response.Response(
                data={'msg': "Can't follow self."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            request.user.profile.following_list.add(to_follow)
            return response.Response(
                data={'msg': 'Added to following list'},
                status=status.HTTP_200_OK,
            )
        except:
            return response.Response(
                data={'msg': "Can't add non-existing user"},
                status=status.HTTP_404_NOT_FOUND
            )


    def delete(self, request, pk, format=None):
        to_follow = int(self.kwargs.get('pk'))
        if to_follow == self.request.user.id:
            return response.Response(
                data={'msg': "Can't unfollow self."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            request.user.profile.following_list.remove(to_follow)
            return response.Response(
                data={'msg': 'Removed from following list'},
                status=status.HTTP_200_OK,
            )
        except:
            return response.Response(
                data={'msg': "Can't add non-existing user"},
                status=status.HTTP_404_NOT_FOUND
            )

