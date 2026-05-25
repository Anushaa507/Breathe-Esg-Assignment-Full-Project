from rest_framework.views import APIView
from rest_framework.response import Response

from .models import NormalizedEmissionRecord


class ApproveRecordView(APIView):

    def post(self, request, pk):
        record = NormalizedEmissionRecord.objects.get(id=pk)

        record.approval_status = 'APPROVED'
        record.save()

        return Response({'message': 'Approved'})