from django.shortcuts import render
from moddjango.core import ModDjango
from moddjango.forms import ChangeStatusForm
from moddjango.models import Module


def index(request):
    modules = Module.objects.filter(status='on')
    return render(request, 'moddjango/index.html', {
        'modules':modules})


def management(request):
    ModDjango().add_downloaded_to_db() 
    form = ChangeStatusForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.change_status()
    modules = Module.objects.exclude(status='none')
    return render(request, 'moddjango/management.html', {
        'modules': modules,
        'form':form})