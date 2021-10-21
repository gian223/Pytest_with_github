from controller import setup
from flask import Flask, render_template, request, json
from vending_machine import VendingMachine
my_test = VendingMachine()

# the Flask object works out where this file is running from
app = Flask(__name__, template_folder='templates')
# get data from controller
vending_machine = setup()

# format data into html f-string template
html = f"""
    <!DOCTYPE html> 
    <html lang="en"> 
    <head> 
    <title>Vending Machine</title> 
    <link rel="shortcut icon" href="#">
    <link rel="stylesheet" href='static/style.css' />
    </head> 
    <body>
    
    <table>
        <tr>
           <th>Vending Machine</th>
           <th>Location</th>
        </tr>
        <tr>
            <td>{vending_machine.name}</td>
            <td>{vending_machine.location}</td>
        </tr>
    <table>
    
    <table>
        <tr>
           <th>Value</th>
           <th>Weight</th>
           <th>Alloy</th>
           <th>Diameter</th>
        </tr>
        {vending_machine.get_coins()}
        <tr class="striped">
            <td></td>
            <td></td>
            <td>Total Coins:</td>
            <td>{len(vending_machine.all_my_coins)}</td>
        </tr>
    <table>
    
    <table>
        <tr>
           <th>Name</th>
           <th>Colour</th>
           <th>Weight</th>
           <th>Price</th>
        </tr>
        {vending_machine.get_products()}
        <tr class="striped">
            <td></td>
            <td></td>
            <td>Total Products:</td>
            <td>{len(vending_machine.all_my_products)}</td>
        </tr>
    <table>
    </body> 
    
    <input type="number" class="coin-value">
    <input type="submit" value="Insert Coin" class="submit">
    <div class="message"></div>
    
    <script src="static/js/script.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
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


# needs this to run in PyCharm
app.run(debug=True,
        port=5000,
        use_debugger=False,
        use_reloader=False,
        passthrough_errors=True)

# view in web-browser at http://127.0.0.1:5000/
# or at localhost:5000
