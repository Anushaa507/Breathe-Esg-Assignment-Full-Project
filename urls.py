from django.contrib import admin
from django.urls import path

from ingestion.views import UploadSAPView
from emissions.views import EmissionListView, ApproveRecordView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/upload/sap/', UploadSAPView.as_view()),

    path('api/emissions/', EmissionListView.as_view()),

    path(
        'api/emissions/<int:pk>/approve/',
        ApproveRecordView.as_view()
    ),
]