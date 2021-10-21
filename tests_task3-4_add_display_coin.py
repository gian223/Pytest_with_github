import unittest
from vending_machine import VendingMachine
from controller import setup
from money import Money


class TestVendingMachinePropertiesExist(unittest.TestCase):
    def test_name_property_exists(self):
        the_money = Money('fiveDollar', 500, 10, '5-dollar.png')
        self.assertTrue(hasattr(the_money, 'name'))

    def test_value_property_exists(self):
        the_money = Money('fiveDollar', 500, 10, '5-dollar.png')
        self.assertTrue(hasattr(the_money, 'value'))

    def test_quantity_property_exists(self):
        the_money = Money('fiveDollar', 500, 10, '5-dollar.png')
        self.assertTrue(hasattr(the_money, 'quantity'))


class TestVendingMachineGetsCorrectValuesFromControllerSetup(unittest.TestCase):
    def test_vm_name_correct(self):
        the_money = Money('fiveDollar', 500, 10, '5-dollar.png')
        self.assertEqual(the_money.name, 'fiveDollar')

    def test_vm_value_correct(self):
        the_money = Money('fiveDollar', 500, 10, '5-dollar.png')
        self.assertEqual(the_money.value, 500)

    def test_vm_quantity_correct(self):
        the_money = Money('fiveDollar', 500, 10, '5-dollar.png')
        self.assertEqual(the_money.quantity, 10)


class TestVendingMachineGetsCorrectTypesFromControllerSetup(unittest.TestCase):
    def test_vm_name_has_no_leading_spaces(self):
        the_vm = setup()
        self.assertFalse(the_vm.name.startswith(' '))

    def test_vm_name_has_no_trailing_spaces(self):
        the_vm = setup()
        self.assertFalse(the_vm.name.endswith(' '))


if __name__ == '__main__':
    unittest.main(verbosity=3)
