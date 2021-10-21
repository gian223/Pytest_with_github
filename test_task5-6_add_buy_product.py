import unittest
from vending_machine import VendingMachine
from controller import setup
from product import Product


class TestVendingMachinePropertiesExist(unittest.TestCase):
    def test_name_property_exists(self):
        the_product = Product('Cola', 250, 'a1', 5)
        self.assertTrue(hasattr(the_product, 'name'))

    def test_price_property_exists(self):
        the_product = Product('Cola', 250, 'a1', 5)
        self.assertTrue(hasattr(the_product, 'price'))

    def test_position_property_exists(self):
        the_product = Product('Cola', 250, 'a1', 5)
        self.assertTrue(hasattr(the_product, 'position'))

    def test_quantity_property_exists(self):
        the_product = Product('Cola', 250, 'a1', 5)
        self.assertTrue(hasattr(the_product, 'quantity'))


class TestVendingMachineGetsCorrectValuesFromControllerSetup(unittest.TestCase):
    def test_vm_alloy_correct(self):
        the_product = Product('Cola', 250, 'a1', 5)
        self.assertEqual(the_product.name, 'Cola')

    def test_vm_diameter_correct(self):
        the_product = Product('Cola', 250, 'a1', 5)
        self.assertEqual(the_product.price, 250)

    def test_vm_weight_correct(self):
        the_product = Product('Cola', 250, 'a1', 5)
        self.assertEqual(the_product.position, 'a1')

    def test_vm_value_correct(self):
        the_product = Product('Cola', 250, 'a1', 5)
        self.assertEqual(the_product.quantity, 5)


if __name__ == '__main__':
    unittest.main(verbosity=3)
