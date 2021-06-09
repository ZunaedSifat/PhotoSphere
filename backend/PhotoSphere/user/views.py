from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

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
