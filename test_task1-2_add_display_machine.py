import unittest
from vending_machine import VendingMachine
from controller import setup


class TestVendingMachinePropertiesExist(unittest.TestCase):
    def test_vm_name_exists(self):
        the_vm = VendingMachine()
        self.assertTrue(hasattr(the_vm, 'name'))

    def test_vm_location_exists(self):
        the_vm = VendingMachine()
        self.assertTrue(hasattr(the_vm, 'location'))


class TestVendingMachineGetsCorrectValuesFromControllerSetup(unittest.TestCase):
    def test_vm_name_correct(self):
        the_vm = setup()
        self.assertEqual(the_vm.name, 'Ara Vending Machine')

    def test_vm_location_correct(self):
        the_vm = setup()
        self.assertEqual(the_vm.location, 'Madras Street')


class TestVendingMachineGetsCorrectTypesFromControllerSetup(unittest.TestCase):
    def test_vm_name_has_no_leading_spaces(self):
        the_vm = setup()
        self.assertFalse(the_vm.name.startswith(' '))

    def test_vm_name_has_no_trailing_spaces(self):
        the_vm = setup()
        self.assertFalse(the_vm.name.endswith(' '))


if __name__ == '__main__':
    unittest.main(verbosity=3)
