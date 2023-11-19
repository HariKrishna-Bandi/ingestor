# logs/urls.py
from django.urls import path
from .views import ingest_logs

urlpatterns = [
    path('ingest_logs/', ingest_logs, name='ingest_logs'),
]
