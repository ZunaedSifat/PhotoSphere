from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from exhibitions.permissions import ExhibitionPermission, ExhibitionEntryPermission
from exhibitions.serializers import ExhibitionSerializer, ExhibitionEntrySerializer, ThemeSerializer
from exhibitions.models import Exhibition, ExhibitionEntry, Theme


class ExhibitionListCreateAPIView(ListCreateAPIView):
    permission_classes = (ExhibitionPermission, )
    serializer_class = ExhibitionSerializer
    queryset = Exhibition.objects.all()

    def filter_queryset(self, queryset):
        try:
            organizer_id = int(self.request.query_params['organizer'])
            queryset = queryset.filter(organizer__id=organizer_id)
        except:
            pass

        return queryset


class ExhibitionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (ExhibitionPermission,)
    serializer_class = ExhibitionSerializer
    queryset = Exhibition.objects.all()


class ExhibitionEntryListCreateAPIView(ListCreateAPIView):
    permission_classes = (ExhibitionEntryPermission, )
    serializer_class = ExhibitionEntrySerializer
    queryset = ExhibitionEntry.objects.all()

    def filter_queryset(self, queryset):
        try:
            exhibition_id = int(self.request.query_params['exhibition'])
            queryset = queryset.filter(exhibition__id=exhibition_id)
        except:
            pass

        try:
            queryset = queryset.order_by(self.request.query_params['order_by'])
        except:
            pass

        return queryset


class ExhibitionEntryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (ExhibitionEntryPermission, )
    serializer_class = ExhibitionEntrySerializer
    queryset = ExhibitionEntry.objects.all()


class ThemeListCreateAPIView(ListCreateAPIView):
    permission_classes = (ExhibitionEntryPermission, )
    serializer_class = ThemeSerializer
    queryset = Theme.objects.all()


class ThemeRetrieveAPIView(RetrieveAPIView):
    permission_classes = (ExhibitionEntryPermission,)
    serializer_class = ThemeSerializer
    queryset = Theme.objects.all()
