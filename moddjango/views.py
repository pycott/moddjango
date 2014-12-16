from django.shortcuts import render
from moddjango.core import ModDjango
from moddjango.models import Module


def index(request):
    return render(request, 'moddjango/index.html')


def management(request):
    ModDjango().add_downloaded_to_db() 
    modules = Module.objects.exclude(status='none')
    return render(request, 'moddjango/management.html', {
        'modules': modules})
