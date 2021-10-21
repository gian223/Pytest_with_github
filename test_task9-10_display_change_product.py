import unittest
from vending_machine import VendingMachine
from controller import setup
from product import Product


class TestVendingMachinePropertiesExist(unittest.TestCase):
    def test_name_property_exists(self):
        the_product = Product('Dilbert', 'Brown', 500, 150)
        self.assertTrue(hasattr(the_product, 'name'))

    def test_colour_property_exists(self):
        the_product = Product('Dilbert', 'Brown', 500, 150)
        self.assertTrue(hasattr(the_product, 'colour'))

    def test_weight_property_exists(self):
        the_product = Product('Dilbert', 'Brown', 500, 150)
        self.assertTrue(hasattr(the_product, 'weight'))

    def test_price_property_exists(self):
        the_product = Product('Dilbert', 'Brown', 500, 150)
        self.assertTrue(hasattr(the_product, 'price'))


class TestVendingMachineGetsCorrectValuesFromControllerSetup(unittest.TestCase):
    def test_vm_alloy_correct(self):
        the_product = Product('Dilbert', 'Brown', 500, 150)
        self.assertEqual(the_product.name, 'Dilbert')

    def test_vm_diameter_correct(self):
        the_product = Product('Dilbert', 'Brown', 500, 150)
        self.assertEqual(the_product.colour, 'Brown')

    def test_vm_weight_correct(self):
        the_product = Product('Dilbert', 'Brown', 500, 150)
        self.assertEqual(the_product.weight, 500)

    def test_vm_value_correct(self):
        the_product = Product('Dilbert', 'Brown', 500, 150)
        self.assertEqual(the_product.price, 150)


if __name__ == '__main__':
    unittest.main(verbosity=3)
