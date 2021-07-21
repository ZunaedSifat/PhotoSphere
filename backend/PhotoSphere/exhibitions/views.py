from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from exhibitions.permissions import ExhibitionPermission, ExhibitionEntryPermission
from exhibitions.serializers import ExhibitionSerializer, ExhibitionEntrySerializer
from exhibitions.models import Exhibition, ExhibitionEntry


class ExhibitionListCreateAPIView(ListCreateAPIView):
    permission_classes = (ExhibitionPermission, )
    serializer_class = ExhibitionSerializer
    queryset = Exhibition.objects.all()


class ExhibitionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (ExhibitionPermission,)
    serializer_class = ExhibitionSerializer
    queryset = Exhibition.objects.all()


class ExhibitionEntryListCreateAPIView(ListCreateAPIView):
    permission_classes = (ExhibitionEntryPermission, )
    serializer_class = ExhibitionEntrySerializer
    queryset = ExhibitionEntry.objects.all()


class ExhibitionEntryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (ExhibitionEntryPermission, )
    serializer_class = ExhibitionEntrySerializer
    queryset = ExhibitionEntry.objects.all()
