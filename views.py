import pandas as pd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import DataSource, RawRecord
from companies.models import Company


class UploadSAPView(APIView):

    def post(self, request):
        file = request.FILES['file']
        company_id = request.data.get('company_id')

        company = Company.objects.get(id=company_id)

        datasource = DataSource.objects.create(
            company=company,
            source_type='SAP',
            uploaded_by=request.user,
            file=file
        )

        df = pd.read_csv(file)

        for _, row in df.iterrows():
            RawRecord.objects.create(
                datasource=datasource,
                raw_payload=row.to_dict(),
                ingest_status='INGESTED'
            )

        return Response({'message': 'SAP upload complete'})