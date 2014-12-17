# -*- coding: utf-8 -*-
from django import forms 
from django.core.exceptions import ObjectDoesNotExist
from moddjango.core import ModDjango
from moddjango.models import Module


class ChangeStatusForm(forms.Form):
    name = forms.CharField(max_length = 255)
    status = forms.CharField(max_length = 10)


    def clean_name(self):
        name = self.cleaned_data.get('name')
        try:
            module = ModDjango(name)
        except ObjectDoesNotExist:
            raise forms.ValidationError('данный модуль не найден в базе данных')
        return name


    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status not in ['on', 'off', 'install', 'uninstall', 'none']:
            raise forms.ValidationError('неизвестное действие над модулем')
        return status


    def change_status(self):
        status = self.cleaned_data.get('status')
        module = ModDjango(self.cleaned_data.get('name'))
        if status != 'none':
            
            if status == 'uninstall':
                module.uninstall()
            
            elif status == 'on':
                try:
                    module.turn_on()
                except Exception as e:
                    if str(e) == 'not satisfied depending':
                        self.add_error(None, 'Не все зависимости удовлетворены. Включите необходимые модули.')
            
            elif status == 'off':
                try:
                    module.turn_off()
                except Exception as e:
                    if str(e) == 'depending not disabled':
                        self.add_error(None, 'У этого модуля есть включеные зависимости. Отключите их.')

            elif status == 'install':
                try:
                    module.install()
                except Exception as e:
                    if str(e) == 'full path not found':
                        self.add_error(None, 'Не найден файл модуля. Возможно в moddjango/settings не настроена папка download или файл модуля в не правильном формате')

        else:
            return False
