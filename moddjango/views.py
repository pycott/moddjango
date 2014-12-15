from django.shortcuts import render
from moddjango.core import ModDjango
from moddjango.models import Module


def index(request):
    return render(request, 'moddjango/index.html')


def management(request):
    ModDjango().db_update() 
    modules = Module.objects.all()
    return render(request, 'moddjango/management.html', {
        'modules': modules})
