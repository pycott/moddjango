import os, shutil, json
from moddjango import settings
from moddjango.core import ModDjango


def add_fake_modules():
    print('adding fake modules')
    fake_infos = [{"name":"fake1","description":"fake1","version":"0.1.2","dependencies":[],"templates":"True","urls":"True"},
        {"name":"fake2","description":"fake2","version":"0.1","dependencies":["fake1"],"migrate":"True","templates":"True","urls":"True"}]
    name_info_dict = {'fake1':fake_infos[0], 'fake2':fake_infos[1]}
    for module_name in name_info_dict:
        fake_module_dir = os.path.join(settings.DOWNLOAD_DIR, module_name)
        if os.path.exists(fake_module_dir):
            shutil.rmtree(fake_module_dir)
        os.mkdir(os.path.join(settings.DOWNLOAD_DIR, module_name))
        info_file = os.path.join(fake_module_dir, 'info.txt')
        init_file = os.path.join(fake_module_dir, '__init__.py')
        urls_file = os.path.join(fake_module_dir, 'urls.py')
        with open(info_file, 'a') as f:
            json.dump(name_info_dict.get(module_name), f)
        open(init_file, 'a').close()
        open(urls_file, 'a').close()
        if os.path.exists(fake_module_dir+'.tar.gz'):
            os.remove(fake_module_dir+'.tar.gz')
        cmd = "tar czf {0}/{1}.tar.gz -C {2} info.txt __init__.py urls.py"\
            .format(settings.DOWNLOAD_DIR, module_name, fake_module_dir)
        os.system(cmd)
        if os.path.exists(fake_module_dir):
            shutil.rmtree(fake_module_dir)
        

def del_fake_modules():
    print('destroying fake modules')
    fake1 = ModDjango('fake1')
    fake2 = ModDjango('fake2')
    fake1.module.status = 'on'
    fake2.module.status = 'on'
    fake1.module.save()
    fake2.module.save()
    fake2.turn_off()
    fake1.turn_off()
    for module_name in ['fake1', 'fake2']:
        module_arc = module_name + '.tar.gz'
        path_module_arc = os.path.join(settings.DOWNLOAD_DIR, module_arc)
        path_installed_module = os.path.join(settings.BASE_DIR, module_name)
        if os.path.exists(path_module_arc):
            os.remove(path_module_arc)
        if os.path.exists(path_installed_module):
            shutil.rmtree(path_installed_module)

