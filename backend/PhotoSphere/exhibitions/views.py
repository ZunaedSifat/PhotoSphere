from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from exhibitions.permissions import ExhibitionPermission
from exhibitions.serializers import ExhibitionSerializer
from exhibitions.models import Exhibition


class ExhibitionListCreateAPIView(ListCreateAPIView):
    permission_classes = (ExhibitionPermission, )
    serializer_class = ExhibitionSerializer
    queryset = Exhibition.objects.all()


class ExhibitionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (ExhibitionPermission,)
    serializer_class = ExhibitionSerializer
    queryset = Exhibition.objects.all()
