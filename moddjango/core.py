import os
import time
import json
import shutil
from moddjango.settings import DOWNLOAD_DIR, MODDJANGO_DIR
from moddjango.models import Module


class ModDjango:
    def __init__(self, name = False):
        self.name = name
        self.filename = str(name)+'.tar.gz' if name else False
        self.downloaded_modules = os.listdir(DOWNLOAD_DIR)
        if self.name:
            self.module = Module.objects.get(name=self.name)
        self.__SETTINGS = os.path.join(MODDJANGO_DIR, 'settings.py')
        self.__NEW_SETTINGS = os.path.join(MODDJANGO_DIR, 'new_settings.py')
        self.__URLSCONF = os.path.join(MODDJANGO_DIR, 'urls.py')


    def add_downloaded_to_db(self):
        if not self.downloaded_modules:
            return False
        down_names = {file_n.split('.')[0] \
            for file_n in self.downloaded_modules}
        db_names = {db_module.name \
            for db_module in Module.objects.exclude(status='none')}
        down_not_in_db = down_names.difference(db_names)
        for module_name in down_not_in_db:
            self.name = module_name
            self.filename = str(module_name)+'.tar.gz'
            module_info = self.__info()
            dependencies = set(module_info.pop('dependencies'))
            new_module, created = Module.objects.update_or_create(
                name = module_info.get('name'),
                defaults = module_info)
            dependencies_not_in_db = dependencies.difference(db_names)
            for module_name in dependencies_not_in_db:
                depend_module, created = Module.objects.get_or_create(
                    name = module_name,
                    defaults = {'status':'none'})
                new_module.dependence.add(depend_module)


    def install(self):
        __info = self.__info()
        if not self.__is_satisfied_depending():
            raise Exception('not satisfied depending')
        if not self.__unpack():
            raise Exception('full path not found')
        self.module.status = 'installed'
        self.module.save()
        return True


    def uninstall(self):
        shutil.rmtree(self.name)
        if not os.path.exists(self.name):
            self.module.status = 'downloaded'
            self.module.save()
            return True
        return False


    def turn_on(self):
        if self.module.status != 'installed':
            return False
        if not self.__is_satisfied_depending():
            raise Exception('not satisfied depending')
        in_file = self.__SETTINGS
        #add in installed apps
        add_line = "'{0}',{1}".format(self.name, os.linesep)
        after_line = 'INSTALLED_APPS += ('
        self.__add_line_in_file(add_line, after_line, in_file)
        #add in template dirs
        if self.module.templates:
            add_line = "os.path.join(BASE_DIR, '{0}/templates/'),{1}"\
                .format(self.name, os.linesep)
            after_line = 'TEMPLATE_DIRS += ('
            self.__add_line_in_file(add_line, after_line, in_file)
        #add in urls
        if self.module.urls:
            add_line = \
                "url(r'^{0}/', include('{0}.urls', namespace='{0}', app_name='{0}')),{1}"\
                .format(self.name, os.linesep)
            after_line = "urlpatterns += patterns('',"
            in_file = self.__URLSCONF
            self.__add_line_in_file(add_line, after_line, in_file)
        #migrate
        if self.module.migrate:
            os.system('python manage.py makemigrations {0}'.format(self.name))
            os.system('python manage.py migrate')
        #change status
        self.module.status = 'on'
        self.module.save()
        self.__reboot_server()


    def turn_off(self):
        if self.module.status != 'on':
            return False
        if not self.__is_depending_disabled():
            raise Exception('depending not disabled')
        #del from installed apps
        from_file = self.__SETTINGS
        del_line = "'{0}',{1}".format(self.name, os.linesep)
        self.__del_line_from_file(del_line, from_file)
        #del in template dirs
        if self.module.templates:
            del_line = "os.path.join(BASE_DIR, '{0}/templates/'),{1}"\
                .format(self.name, os.linesep)
            self.__del_line_from_file(del_line, from_file)
        #del urls
        if self.module.urls:
            from_file = self.__URLSCONF
            del_line = \
                "url(r'^{0}/', include('{0}.urls', namespace='{0}', app_name='{0}')),{1}"\
                .format(self.name, os.linesep)
            self.__del_line_from_file(del_line, from_file)
        #change status
        self.module.status = 'installed'
        self.module.save()
        self.__reboot_server()

                        
    def __add_line_in_file(self, add_line, after_line, in_file):
        with \
        open(in_file) as old, \
        open(self.__NEW_SETTINGS, 'w') as new:
            for index, line in enumerate(old):
                new.write(line)
                if after_line in line:
                    need_index = index
                if 'need_index' in locals():
                    if need_index == index:
                        new.write(add_line)
        shutil.move(self.__NEW_SETTINGS, in_file) 


    def __del_line_from_file(self, del_line, from_file):
        with \
        open(from_file) as old, \
        open(self.__NEW_SETTINGS, 'w') as new:
            for line in old:
                if not del_line in line:
                    new.write(line)
        shutil.move(self.__NEW_SETTINGS, from_file) 


    def __full_path(self):
        if self.name:
            return os.path.join(DOWNLOAD_DIR, self.filename) 
        else:
            return False


    def __info(self):
        full_path = self.__full_path() 
        if full_path:
            cmd = 'tar xzvf {0} info.txt -O'.format(full_path)
            data = json.load(os.popen(cmd))
            return data
        return False


    def __is_satisfied_depending(self):
        turn_on_modules = Module.objects.filter(status='on')    
        dependencies = self.module.dependence.all()
        if dependencies and not turn_on_modules:
            return False
        for depend in dependencies:
            for module in turn_on_modules:
                if not depend.name in module.name:
                    return False
        return True


    def __is_depending_disabled(self):
        related_dependence = self.module.related_dependence.all()
        if not related_dependence:
            return True
        for module in related_dependence:
            if module.status == 'on':
                return False
        return True


    def __unpack(self):
        full_path = self.__full_path() 
        if full_path:
            os.mkdir(self.name)
            cmd = 'tar xzvf {0} -C {1}'.format(full_path, self.name)
            os.popen(cmd)
            return True
        return False


    def __reboot_server(self):
        touch_file = os.path.join(MODDJANGO_DIR, 'models.py')
        os.utime(touch_file, (0, time.time()))
