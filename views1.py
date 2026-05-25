from rest_framework.generics import ListAPIView
from .models import NormalizedEmissionRecord
from .serializers import EmissionSerializer


class EmissionListView(ListAPIView):
    serializer_class = EmissionSerializer

    def get_queryset(self):
        status_filter = self.request.GET.get('status')

        queryset = NormalizedEmissionRecord.objects.all()

        if status_filter:
            queryset = queryset.filter(approval_status=status_filter)

        return queryset