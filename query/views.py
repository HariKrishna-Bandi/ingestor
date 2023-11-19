# query_interface/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LogSearchForm
from logs.models import LogEntry

# views.py
import logging

logger = logging.getLogger(__name__)

def your_view(request):
    # Your view logic here

    logger.info('This is an informational message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')


def search_logs(request):
    form = LogSearchForm(request.GET)
    logs = LogEntry.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        if search_query:
            logs = logs.filter(message__icontains=search_query)

        for field in LogSearchForm.Meta.fields:
            value = form.cleaned_data.get(field)
            if value:
                logs = logs.filter(**{field: value})

    # Check if there is a search query; if not, display all logs
    if not form.cleaned_data or not any(form.cleaned_data.values()):
        return render(request, 'search_results.html', {'logs': logs, 'form': form})
    else:
        return render(request, 'search_results.html', {'logs': logs, 'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Create a log entry for successful login
            log_entry = LogEntry.objects.create(
                level='INFO',
                message=f'User {user.username} logged in',
                resourceId='auth',
            )

            return redirect('home')  # Adjust the redirect as needed
        else:
            # Create a log entry for failed login
            log_entry = LogEntry.objects.create(
                level='ERROR',
                message=f'Failed login attempt for username: {username}',
                resourceId='auth',
            )

            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def logout_view(request):
    # Create a log entry for logout
    log_entry = LogEntry.objects.create(
        level='INFO',
        message=f'User {request.user.username} logged out',
        resourceId='auth',
    )

    logout(request)
    return redirect('home')  # Adjust the redirect as needed
