# logs/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from .models import LogEntry

@csrf_exempt
def ingest_logs(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        log_entry = LogEntry.objects.create(
            level=data['level'],
            message=data['message'],
            resourceId=data['resourceId'],
            timestamp=timezone.now(),
            traceId=data['traceId'],
            spanId=data['spanId'],
            commit=data['commit'],
            parentResourceId=data.get('metadata', {}).get('parentResourceId')
        )
        log_entry.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})
