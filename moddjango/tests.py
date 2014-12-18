import os
from django.test import TestCase
from moddjango.core import ModDjango
from moddjango import test_utils
from main.settings import BASE_DIR
from django.core.exceptions import ObjectDoesNotExist


class ModDjangoTestCase(TestCase):
    def test_get_module(self):
        with self.assertRaises(ObjectDoesNotExist):
            ModDjango('asdfsdf')
        self.assertEqual(ModDjango('fake1').name, 'fake1')
        
    def test_add_downloaded_to_db(self):
        ModDjango('fake1').module.delete()
        ModDjango('fake2').module.delete()
        with self.assertRaises(ObjectDoesNotExist):
            ModDjango('fake1')
            ModDjango('fake2')
        ModDjango().add_downloaded_to_db()
        self.assertEqual(ModDjango('fake1').module.status, 'downloaded')
        self.assertEqual(ModDjango('fake2').module.status, 'downloaded')
        
    def test_install_uninstall(self):
        installed_module_dir = os.path.join(BASE_DIR, 'fake1')
        test_utils.del_fake_modules()
        with self.assertRaises(Exception):
            ModDjango('fake1').install()
        test_utils.add_fake_modules()            
        ModDjango('fake1').install()
        self.assertTrue(os.path.exists(installed_module_dir))
        status = ModDjango('fake1').module.status
        self.assertEqual(status, 'installed')
        answer = ModDjango('fake1').uninstall()
        self.assertTrue(answer)
        self.assertFalse(os.path.exists(installed_module_dir))
        status = ModDjango('fake1').module.status
        self.assertEqual(status, 'downloaded')

    def test_turn_on_off_dependence(self):
        ModDjango('fake2').install()
        with self.assertRaises(Exception):
            ModDjango('fake2').turn_on()
        status = ModDjango('fake2').module.status
        self.assertEqual(status, 'installed')
        ModDjango('fake1').turn_on()
        status = ModDjango('fake1').module.status
        self.assertNotEqual(status, 'on')
        ModDjango('fake1').install()
        ModDjango('fake1').turn_on()
        status = ModDjango('fake1').module.status
        self.assertEqual(status, 'on')
        ModDjango('fake2').turn_on()
        status = ModDjango('fake2').module.status
        self.assertEqual(status, 'on')
        with self.assertRaises(Exception):
            ModDjango('fake1').turn_off()
        ModDjango('fake2').turn_off()
        status = ModDjango('fake2').module.status
        self.assertEqual(status, 'installed')


def setUpModule():
    test_utils.add_fake_modules()            
    ModDjango().add_downloaded_to_db()
    
def tearDownModule():
    test_utils.del_fake_modules()
