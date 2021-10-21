# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from controller import setup
from flask import Flask, render_template, request, json
from vending_machine import VendingMachine
from flask import jsonify

# the Flask object works out where this file is running from
app = Flask(__name__, template_folder='templates')
# get data from controller
vending_machine = setup()

# format data into html f-string template
html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <meta http-equiv="X-UA-Compatible" content="ie=edge"/>
    <title>Vending Machine</title>
    <link rel="stylesheet" href="static/style.css">
    
</head>
<body>
<div class="start-screen">
    <h1 class="start-screen-heading">Please select a customer to start</h1>
    <button class="start-screen-button" value="1">Jack</button>
    <button class="start-screen-button" value="2">Jill</button>
    <button class="start-screen-button" value="3">Troy</button>
    <span class="start-screen-note"><b>Note:</b> Each customer starts with a different quantity of denominations</span>
</div>
<div style="padding-top:25px !important"></div>
<div class="row">
    <div class="col-1-of-4">
        <div class="row">
            <div class="col-1-of-1">
                <img class="customer-image" src="static/images/customer.png" alt="">
                <div class="customer-text">
                    <h5 class="customer-title">Customer</h5>
                </div></br>
                <img class="customers-wallet-img" src="static/images/wallet.png" alt="">
                <h5 class="customers-wallet-title">Customer's Wallet</h5>
                <div class="insert-customer-coins"></div>
            </div>
            <div class="col-1-of-1">
                <img class="customers-products-img" src="static/images/bag.jpg" alt="">
                <h5 class="customers-products-title">Customer's Products</h5>
                <div class="insert-customer-products"></div>
            </div>
        </div>
    </div>
    <div class="col-2-of-4">
        <div class="vending">
            <div class="vending__left">
                <div class="vending__left-top">
                    <div class="row row-padding vending__left-item">
                    </div>
                </div>
                <div class="vending__left-bottom">
                    <div class="vending__left-dispenser">
                        <div class="vending__left-dispenser-title">Collect your products</div>
                    </div>
                </div>
            </div><!--
            --><div class="vending__right">
                <div class="row">
                    <div class="col-1-of-1">
                        <div class="vending__right-screen">
                            <div class="vending__right-screen-text">
                            </div>
                        </div>
                    </div>
                    <div class="col-1-of-1">
                        <div class="vending__right-keypad">
                            <button class="vending__right-keypad--button" value="A">A</button>
                            <button class="vending__right-keypad--button" value="B">B</button>
                            <button class="vending__right-keypad--button" value="C">C</button>
                            <button class="vending__right-keypad--button" value="1">1</button>
                            <button class="vending__right-keypad--button" value="2">2</button>
                            <button class="vending__right-keypad--button" value="3">3</button>
                            <button class="vending__right-keypad--button" value="4">4</button>
                            <button class="vending__right-keypad--button" value="5">5</button>
                            <button class="vending__right-keypad--button" value="6">6</button>
                            <button class="vending__right-keypad--button" value="7">7</button>
                            <button class="vending__right-keypad--button" value="8">8</button>
                            <button class="vending__right-keypad--button" value="9">9</button>
                            <button class="vending__right-keypad--button" value="clr">Clear</button>
                            <button class="vending__right-keypad--button" value="ok">Ok</button>
                        </div>
                    </div>
                    <div class="col-1-of-1">
                        <div class="vending__right-insert">
                            <img src="static/images/insert-coin.png" class="vending__right-insert-img" alt="">
                        </div>
                    </div>
                    <div class="col-1-of-1">
                        <div class="vending__right-change">
                            <div class="vending__right-change-title">Change Dispenser</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-1-of-4">
        <h1>Vending Machine</h1>
        <div class="insert-vending-coins"></div>
    </div>
    <div class="col-1-of-4">
        <h3>Instructions</h3>
        <ul>
            <li>1. Use the key pad to select the desired product and press "OK"</li>
            <li>2. Drag and drop your money on the insert coin slot</li>
            <li>3. Change will be returned to your wallet and product will be dispensed</li>
        </ul>
    </div>
</div>
</body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="static/js/script.js"></script>
</html>
"""


# some magic to connect the app to the web
@app.route('/')
def index():
    return html


@app.route('/purchase', methods=['GET', 'POST'])
def get_purchase():
    coin_value = request.form['coin_value']
    check_purchase = vending_machine.purchase_product(coin_value)
    return str(check_purchase)


@app.route('/get-customers-money', methods=['GET', 'POST'])
def get_customer_money():
    customer_id = request.form['customer_id']
    get_customers_money = vending_machine.get_customers_money(customer_id)
    return jsonify(get_customers_money)


@app.route('/get-vending-money', methods=['GET', 'POST'])
def get_money():
    get_vending_money = vending_machine.get_vending_money()
    return jsonify(get_vending_money)


@app.route('/get-vending-products', methods=['GET', 'POST'])
def get_products():
    get_vending_products = vending_machine.get_vending_product()
    return jsonify(get_vending_products)


# needs this to run in PyCharm
app.run(debug=True,
        port=5000,
        use_debugger=False,
        use_reloader=False,
        passthrough_errors=True)

# view in web-browser at http://127.0.0.1:5000/
# or at localhost:5000
