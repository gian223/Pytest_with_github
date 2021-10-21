# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from vending_machine import VendingMachine


def setup():
    the_vending_machine = VendingMachine()
    the_vending_machine.add_machine('Ara Vending Machine', 'Madras Street')

    # Add vending machines money
    the_vending_machine.add_money('fiveDollar', 500, 10, '5-dollar.png')
    the_vending_machine.add_money('twoDollar', 200, 10, '2-dollar.png')
    the_vending_machine.add_money('oneDollar', 100, 10, '1-dollar.png')
    the_vending_machine.add_money('fifty', 50, 10, '50-cent.png')
    the_vending_machine.add_money('twenty', 20, 10, '20-cent.png')
    the_vending_machine.add_money('ten', 10, 10, '10-cent.png')

    # Add customers money
    the_vending_machine.add_customer_money('fiveDollar', 500, 0, '5-dollar.png')
    the_vending_machine.add_customer_money('twoDollar', 200, 0, '2-dollar.png')
    the_vending_machine.add_customer_money('oneDollar', 100, 0, '1-dollar.png')
    the_vending_machine.add_customer_money('fifty', 50, 0, '50-cent.png')
    the_vending_machine.add_customer_money('twenty', 20, 0, '20-cent.png')
    the_vending_machine.add_customer_money('ten', 10, 0, '10-cent.png')

    # Add vending machines products
    the_vending_machine.add_product('chipsChicken', 350, 'a1', 2)
    the_vending_machine.add_product('chipsSalt', 300, 'a2', 5)
    the_vending_machine.add_product('chipsVinegar', 220, 'a3', 9)
    the_vending_machine.add_product('coke', 250, 'b1', 5)
    the_vending_machine.add_product('fanta', 450, 'b2', 4)
    the_vending_machine.add_product('pepsi', 230, 'b3', 7)
    the_vending_machine.add_product('skittlesGummies', 300, 'c1', 3)
    the_vending_machine.add_product('skittlesBerries', 420, 'c2', 11)
    the_vending_machine.add_product('skittlesFruits', 400, 'c3', 2)

    return the_vending_machine


if __name__ == '__main__':
    vending_machine = setup()
    print(vending_machine.get_vending_money())
