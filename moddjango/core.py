import os
import json
from shutil import rmtree
from moddjango.settings import DOWNLOAD_DIR
from moddjango.models import Module


class ModDjango:
    def __init__(self, name = False):
        self.name = name
        self.filename = str(name)+'.tar.gz' if name else False
        self.downloaded_modules = os.listdir(DOWNLOAD_DIR)


    def db_update(self):
        if self.downloaded_modules:
            down_names = {file_n.split('.')[0] for file_n in self.downloaded_modules}
            db_names = {db_module.name for db_module in Module.objects.all()}
            no_in_db = down_names.difference(db_names)
            for module_name in no_in_db:
                self.name = module_name
                self.filename = str(module_name)+'.tar.gz'
                Module(**self.info()).save()


    def __full_path(self):
        if self.name:
            return os.path.join(DOWNLOAD_DIR, self.filename) 
        else:
            return False


    def info(self):
        full_path = self.__full_path() 
        if full_path:
            cmd = 'tar xzvf {0} info.txt -O'.format(full_path)
            data = json.load(os.popen(cmd))
            return data
        return False


    def satisfied_depending_for(self, name):
        installed_modules = Module.objects.all()    
        depending = info_for(name).get('depending')
        for dependence in depending:
            for module in installed_modules:
                if not dependence in module.name:
                    return False
        return True


    def install(self, name):
        info = info_for(name)
        if not satisfied_depending_for(name):
            return False
        module_files = unpack(name)
        

    def delete(self, module_files):
        for f in module_files:
            if os.path.isdir(f):
                try: rmtree(f)
                except: pass
            else:
                try: os.remove(f)
                except: pass


    def unpack(self, name):
        full_path = full_path_for(name) 
        if full_path:
            cmd = 'tar xzvf {0}'.format(full_path)
            files = []
            for file_name in os.popen(cmd):
                file_full_path = os.path.join(os.path.abspath('.'), file_name)
                files.append(file_full_path)
            module_files = [module_file.replace('\n', '') for module_file in files]
            return module_files
        return False
