# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from money import Money
from customer_money import CustomerMoney
from product import Product


class VendingMachine:
    def __init__(self):
        self.name = None
        self.location = None
        self.all_the_vending_money = []
        self.all_the_vending_products = []
        self.all_the_customers_money = []

    def add_machine(self, new_name, new_location):
        self.name = new_name
        self.location = new_location

    def add_money(self, new_name, new_value, new_quantity, new_image):
        add_money = Money(new_name, new_value, new_quantity, new_image)
        self.all_the_vending_money.append(add_money)

    def add_product(self, new_name, new_price, new_position, new_quantity):
        add_products = Product(new_name, new_price, new_position, new_quantity)
        self.all_the_vending_products.append(add_products)

    def add_customer_money(self, new_name, new_value, new_quantity, new_image):
        add_money = CustomerMoney(new_name, new_value, new_quantity, new_image)
        self.all_the_customers_money.append(add_money)

    def get_customers_money(self, customer_id):
        if int(customer_id) == 1:
            qty = 10
        elif int(customer_id) == 2:
            qty = 20
        else:
            qty = 30

        append_money = ""
        for money in self.all_the_vending_money:
            append_money += f"{money.name}: {{value: {money.value}, " \
                            f"quantity: {qty}, img: '{money.image}'}}, "
        return append_money

    def get_vending_product(self):
        append_product = ""
        for product in self.all_the_vending_products:
            append_product += f"{product.name}: {{name: '{product.name}', price: {product.price}," \
                              f" position: '{product.position}', quantity: {product.quantity}}}, "
        return append_product

    def get_vending_money(self):
        append_money = ""
        for money in self.all_the_vending_money:
            append_money += f"{money.name}: {{value: {money.value}, " \
                            f"quantity: {money.quantity}, img: '{money.image}'}}, "
        return append_money
