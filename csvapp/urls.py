from django.urls import path
from .views import UploadCSVView, Top50RowsView

urlpatterns = [
    path('upload-csv/', UploadCSVView.as_view()),
    path('top-50-rows/', Top50RowsView.as_view()),
]
