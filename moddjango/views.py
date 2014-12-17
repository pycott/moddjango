from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from moddjango.core import ModDjango
from moddjango.models import Module


def index(request):
    modules = Module.objects.filter(status='on')
    return render(request, 'moddjango/index.html', {
        'modules':modules})


def management(request):
    ModDjango().add_downloaded_to_db() 

    if request.POST:
        for key in request.POST:
            print(key)
            if key == 'submit' or key == 'csrfmiddlewaretoken':
                continue
            try:
                module = ModDjango(key)
            except ObjectDoesNotExist:
                print('not found ;(')
            if 'module' in locals():
                print(module)
                value = request.POST.get(key)
                if value == 'uninstall':
                    module.uninstall()
                elif value == 'on':
                    module.turn_on()
                elif value == 'off':
                    module.turn_off()
                elif value == 'install':
                    module.install()
                elif value == 'none':
                    continue
            else:
                continue


    modules = Module.objects.exclude(status='none')
    return render(request, 'moddjango/management.html', {
        'modules': modules})
