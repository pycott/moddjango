import os
from shutil import rmtree
from moddjango.settings import DOWNLOAD_DIR
from moddjango.models import Module


def full_path_for(module_name):
    modules = os.listdir(DOWNLOAD_DIR)
    full_path = os.path.join(DOWNLOAD_DIR, module_name) 
    if module_name in modules:
        return full_path
    else:
        return False


def info_for(module_name):
    full_path = full_path_for(module_name) 
    if full_path:
        cmd = 'tar xzvf {0} info.txt -O'.format(full_path)
        data = json.load(os.popen(cmd))
        return data
    return False


def satisfied_depending_for(module_name):
    installed_modules = Module.objects.all()    
    depending = info_for(module_name).get('depending')
    for dependence in depending:
        for module in installed_modules:
            if not dependence in module.name:
                return False
    return True


def install(module_name):
    info = info_for(module_name)
    if not satisfied_depending_for(module_name):
        return False
    module_files = unpack(module_name)
    

def delete(module_files):
    for f in module_files:
        if os.path.isdir(f):
            try: rmtree(f)
            except: pass
        else:
            try: os.remove(f)
            except: pass


def unpack(module_name):
    full_path = full_path_for(module_name) 
    if full_path:
        cmd = 'tar xzvf {0}'.format(full_path)
        files = []
        for file_name in os.popen(cmd):
            file_full_path = os.path.join(os.path.abspath('.'), file_name)
            files.append(file_full_path)
        module_files = [module_file.replace('\n', '') for module_file in files]
        return module_files
    return False
