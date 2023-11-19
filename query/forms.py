# query_interface/forms.py
from django import forms

class LogSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False)
    level = forms.CharField(required=False)
    message = forms.CharField(required=False)
    resourceId = forms.CharField(required=False)
    timestamp = forms.DateTimeField(required=False)
    traceId = forms.CharField(required=False)
    spanId = forms.CharField(required=False)
    commit = forms.CharField(required=False)
    parentResourceId = forms.CharField(required=False)

    class Meta:
        fields = '__all__'
