from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from user.serializers import ProfileSerializer
from user.models import Profile


class ProfileListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class MyProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile
