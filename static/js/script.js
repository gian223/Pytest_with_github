'use strict';

const startButton = document.querySelectorAll('.start-screen-button');
const insertCustomersCoins = document.querySelector('.insert-customer-coins');
const insertVendingCoins = document.querySelector('.insert-vending-coins');
const vendingScreen = document.querySelector('.vending__right-screen-text');
const selectKeypad = document.querySelectorAll('.vending__right-keypad--button');
let purchasePrice = 0;

const products = {
    product: {
        coke: {name: 'Cola', price: 250, position: 'b1', quantity: 5},
        fanta: {name: 'Fanta', price: 550, position: 'b2', quantity: 5},
        pepsi: {name: 'Pepsi', price: 350, position: 'b3', quantity: 5},
        chipsVinegar: {name: 'Salt & Vinegar Chips', price: 450, position: 'a3', quantity: 5},
        chipsSalt: {name: 'Salted Chips', price: 350, position: 'a2', quantity: 5},
        chipsChicken: {name: 'Chicken Chips', price: 250, position: 'a1', quantity: 5},
        skittlesGummies: {name: 'Skittles Gummies', price: 550, position: 'c3', quantity: 5},
        skittlesFruits: {name: 'Skittles Fruits', price: 650, position: 'c2', quantity: 5},
        skittlesBerries: {name: 'Skittles Berries', price: 550, position: 'c1', quantity: 5}
    }
};
console.log(products.product.coke.price)

const customer = {
    name: 'Jack',
    money: {
        fiveDollar: {value: 500, quantity: 0, img: '5-dollar.png'},
        twoDollar: {value: 200, quantity: 0, img: '2-dollar.png'},
        oneDollar: {value: 100, quantity: 0, img: '1-dollar.png'},
        fifty: {value: 50, quantity: 0, img: '50-cent.png'},
        twenty: {value: 20, quantity: 0, img: '20-cent.png'},
        ten: {value: 10, quantity: 0, img: '10-cent.png'},
    },
};

const vendingMachineMoney = {
    name: 'Vending Machine',
    money: {
        fiveDollar: {value: 500, quantity: 0, img: '5-dollar.png'},
        twoDollar: {value: 200, quantity: 0, img: '2-dollar.png'},
        oneDollar: {value: 100, quantity: 0, img: '1-dollar.png'},
        fifty: {value: 50, quantity: 0, img: '50-cent.png'},
        twenty: {value: 20, quantity: 0, img: '20-cent.png'},
        ten: {value: 10, quantity: 0, img: '10-cent.png'},
    },
};

// INITIATE THE VENDING MACHINE EXPERIENCE!!!!
// Start machine by choosing one of the three customers
// 1: jack, 2: Jill, 3: Troy // Each customer has a different quantity of denominations
for (let i = 0; i < startButton.length; i++) {
    startButton[i].addEventListener('click', function () {
        theVendingMachine.getCustomersMoney(startButton[i].value)
        $('.start-screen').fadeOut(); // Remove the starting screen
    });
}

// SELECT BUTTONS ON KEYPAD AND CHECK IF PRODUCT EXISTS
for (let i = 0; i < selectKeypad.length; i++) {
    selectKeypad[i].addEventListener('click', function () {
        theVendingMachine.checkProductExists(selectKeypad[i].value);
        const myAudio = new Audio('static/sounds/click-button2.mp3').play();
        // myAudio.play();
        if (myAudio !== undefined) {
          myAudio.then(function() {
            // Automatic playback started!
          }).catch(function(error) {
            // Automatic playback failed.
            // Show a UI element to let the user manually start playback.
          });
        }
    });
}

// DRAG AND DROP MONEY TO GET VALUE
function onMoneyDrag(event) {
    event
        .dataTransfer
        .setData('text/plain', event.target.id);
    theVendingMachine.insertCoin(event.target.id);
}

// VENDING MACHINE CLASS
class VendingMachine {
    constructor(customerID) {
        this.getCustomersMoney(customerID)
        this.getVendingMoney()
        this.getVendingProducts()
        this.selectedProduct = '';
    }

    // CHECK IF THE PRODUCT EXISTS INSIDE THE PRODUCTS OBJECT
    checkProductExists(keypadEntered) {
        if (keypadEntered === "ok") {
            this.selectedProduct = vendingScreen.textContent.replace(/\s/g, '').toLowerCase(); // Customers selected product
            let selectProducts = Object.keys(products.product); // Get all vending machine products
            for (let i = 0; i < Object.keys(products.product).length; i++) {
                // IF PRODUCT EXISTS PRINT PRICE ON SCREEN
                if (this.selectedProduct === products.product[selectProducts[i]].position) {
                    vendingScreen.textContent = "$" + (products.product[selectProducts[i]].price / 100).toFixed(2);
                    purchasePrice = products.product[selectProducts[i]].price
                    break
                } else {
                    vendingScreen.textContent = "Invalid Product!";
                }
            }
        } else if (keypadEntered === "clr") {
            vendingScreen.textContent = "";
        } else {
            vendingScreen.textContent += keypadEntered;
        }
    }

    insertCoin(coinValue) {
        if (purchasePrice === 0) {
            vendingScreen.style.color = "red";
            vendingScreen.textContent = "Select Product!";
            setTimeout(function () {
                vendingScreen.style.color = "black";
                vendingScreen.textContent = "";
            }, 1000);

        } else {
            // PLAY AUDIO OF COIN BEING RELEASED
            const myAudio = new Audio('static/sounds/coin-inserted.wav').play();
            if (myAudio !== undefined) {
              myAudio.then(function() {
                // Automatic playback started!
              }).catch(function(error) {
                // Automatic playback failed.
                // Show a UI element to let the user manually start playback.
              });
            }

            // DISPLAY PRODUCT PRICE ON VENDING MACHINE SCREEN
            vendingScreen.textContent = "$" + ((purchasePrice -= coinValue) / 100).toFixed(2);
            // REMOVE DROPPED MONEY FROM CUSTOMERS WALLET
            let customersMoneyName = Object.keys(customer.money)
            for (let i = 0; i < Object.keys(customer.money).length; i++) {
                if (parseInt(coinValue) === parseInt(customer.money[customersMoneyName[i]].value)) {
                    customer.money[customersMoneyName[i]].quantity -= 1;
                    let removeCustMoney = document.querySelector("[data-name=" + customersMoneyName[i] + "]");
                    removeCustMoney.textContent = customer.money[customersMoneyName[i]].quantity;
                }
            }
            // ADD MONEY TO VENDING MACHINE (FROM CUSTOMER INSERTING COINS)
            let VendingMoneyName = Object.keys(vendingMachineMoney.money)
            for (let i = 0; i < Object.keys(vendingMachineMoney.money).length; i++) {
                if (parseInt(coinValue) === parseInt(vendingMachineMoney.money[VendingMoneyName[i]].value)) {
                    vendingMachineMoney.money[VendingMoneyName[i]].quantity += 1;
                    let removeVendMoney = document.querySelector("[data-name=" + "v-" + VendingMoneyName[i] + "]");
                    removeVendMoney.textContent = vendingMachineMoney.money[VendingMoneyName[i]].quantity;
                }
            }
            // IF CUSTOMER HAS ENTERED ENOUGH MONEY MOVE ON TO calculateChange()
            if (purchasePrice <= 0) {
                vendingScreen.style.color = "red";
                this.calculateChange(purchasePrice)
            }

        }

    }

    calculateChange(change) {
        let changeDue = Math.abs(change)

        // BUILD ARRAY WITH DENOMINATION VALUES FROM VENDINGMACHINEMONEY OBJECT, AND SORT
        let denominations = []
        let VendingMoneyName = Object.keys(vendingMachineMoney.money)
        for (let i = 0; i < Object.keys(vendingMachineMoney.money).length; i++) {
            denominations.push(vendingMachineMoney.money[VendingMoneyName[i]].value)
        }
        denominations.sort(function (a, b) { return b - a; });

        // MAP THE DENOMINATIONS ARRAY AND RETURN AN ARRAY OF ALL 0'S
        let i = 0, moneyCount = denominations.map(function () {
            return 0;
        });

        // LOOP THROUGH THE DENOMINATIONS ARRAY TO FIND THE BEST CHANGE POSSIBLE, FROM HIGHEST TO LOWEST DENOMINATIONS
        while (i < denominations.length) {
            while (denominations[i] <= changeDue) {
                changeDue -= denominations[i];
                moneyCount[i]++;
                moneyCount[i] >= denominations[i] ? i++ : null;
            }
            i++
        }

        // moneyCount NOW CONTAINS THE CORRECT AMOUNT OF DENOMINATIONS TO RETURN TO THE CUSTOMER
        //alert(moneyCount) // THIS RETURNS AN ARRAY OF COINS REQUIRED AS CHANGE
        // REMOVE MONEY FROM VENDING MACHINE
        vendingMachineMoney.money.fiveDollar.quantity -= moneyCount[0]
        vendingMachineMoney.money.twoDollar.quantity -= moneyCount[1]
        vendingMachineMoney.money.oneDollar.quantity -= moneyCount[2]
        vendingMachineMoney.money.fifty.quantity -= moneyCount[3]
        vendingMachineMoney.money.twenty.quantity -= moneyCount[4]
        vendingMachineMoney.money.ten.quantity -= moneyCount[5]
        let vendingMoneyName = Object.keys(vendingMachineMoney.money)
        for (let i = 0; i < Object.keys(vendingMachineMoney.money).length; i++) {
            let addVendMoney = document.querySelector("[data-name=" + "v-" + vendingMoneyName[i] + "]");
            addVendMoney.textContent = vendingMachineMoney.money[vendingMoneyName[i]].quantity;
        }

        // ADD CHANGE BACK TO CUSTOMER WALLET
        customer.money.fiveDollar.quantity += moneyCount[0]
        customer.money.twoDollar.quantity += moneyCount[1]
        customer.money.oneDollar.quantity += moneyCount[2]
        customer.money.fifty.quantity += moneyCount[3]
        customer.money.twenty.quantity += moneyCount[4]
        customer.money.ten.quantity += moneyCount[5]
        let customersMoneyName = Object.keys(customer.money)
        for (let i = 0; i < Object.keys(customer.money).length; i++) {
            let addCustMoney = document.querySelector("[data-name=" + customersMoneyName[i] + "]");
            addCustMoney.textContent = customer.money[customersMoneyName[i]].quantity;
        }

        // REMOVE CHANGE FROM SCREEN AND SET purchasePrice BACK TO 0.
        setTimeout(function () {
            vendingScreen.textContent = "";
            vendingScreen.style.color = "black";
        }, 3000)
        purchasePrice = 0;
        this.dispenseProduct()
    }

    dispenseProduct(){
        const selectedProduct = this.selectedProduct;
        const dispenseProduct = document.querySelectorAll('.vending__left-img');
        for (let i = 0; i < dispenseProduct.length; i++) {
            if(dispenseProduct[i].classList.contains(selectedProduct)){
                function animate(position, row){
                    document.querySelector(`.${position}`).classList.add(`product-${row}-dispense`);
                    setTimeout(function () {
                    document.querySelector(`.${position}`).classList.remove(`product-${row}-dispense`)
                    }, 4000);
                }
                animate(selectedProduct, selectedProduct[0])
                this.selectedProduct = '';
            }
        }
    }

    getCustomersMoney(customerID) {
        $.ajax({
            url: `${window.location}get-customers-money`, // the endpoint
            type: 'POST', // http method
            datatype: 'json',
            data: {
                'customer_id': customerID,
            },
            success: function (data) {
                const money = eval('({' + data + '})');
                let updateCustomerMoney = { money }
                for (Object.key in updateCustomerMoney) customer[Object.key] = updateCustomerMoney[Object.key];
                let customersMoneyName = Object.keys(customer.money)
                for (let i = 0; i < Object.keys(customer.money).length; i++) {
                    let html = ``;
                    html += `
                        <div class="customers-money">
                            <div class="customers-money-top">
                                <img alt="" draggable="true" ondragEnd="onMoneyDrag(event);"
                                id="${customer.money[customersMoneyName[i]].value}"
                                class="example-draggable"
                                src="static/images/${customer.money[customersMoneyName[i]].img}">
                            </div>
                            <div class="customers-money-bottom" data-name="${customersMoneyName[i]}">
                                ${customer.money[customersMoneyName[i]].quantity}
                            </div>
                        </div>
                `;
                    insertCustomersCoins.innerHTML += html;
                }
            }
        });
    }

    getVendingMoney() {
        $.ajax({
            url: `${window.location}get-vending-money`, // the endpoint
            type: 'POST', // http method
            datatype: 'json',
            success: function (data) {
                const money = eval('({' + data + '})');
                let updateVendingMoney = { money }
                for (Object.key in updateVendingMoney) vendingMachineMoney[Object.key] = updateVendingMoney[Object.key];
                const vendingMoneyName = Object.keys(customer.money)
                for (let i = 0; i < Object.keys(customer.money).length; i++) {
                    let html = ``;
                    html += `
                        <div class="customers-money">
                            <div class="customers-money-top">
                                <img alt="" src="static/images/${vendingMachineMoney.money[vendingMoneyName[i]].img}">
                            </div>
                            <div class="customers-money-bottom" data-name="v-${vendingMoneyName[i]}">
                                ${vendingMachineMoney.money[vendingMoneyName[i]].quantity}
                            </div>
                        </div>
                `;
                    insertVendingCoins.innerHTML += html;
                }
            }
        });
    }

    getVendingProducts() {
        $.ajax({
            url: `${window.location}get-vending-products`, // the endpoint
            type: 'GET', // http method
            datatype: 'json',
            success: function (data) {
                // CONVERT JSON STRING INTO AN OBJECT AND UPDATE products OBJECT WITH NEW VALUES
                const product = eval('({' + data + '})');
                let updateProducts = { product }
                // UPDATE JAVASCRIPT OBJECT KEYS WITH DATA FROM JSON RESPONSE
                for (Object.key in updateProducts) products[Object.key] = updateProducts[Object.key];
                const list = document.querySelector('.vending__left-item');
                let item = Object.keys(products.product);
                // RENDER IMAGES AND OTHER RELEVANT INFORMATION ON THE PAGE
                for (let i = 0; i < item.length; i++) {
                    console.log(products[item[i]])
                    let html = '';
                    html += `
                        <div class="col-1-of-3">
                            <img class="vending__left-img ${products.product[item[i]].position}"
                            src="static/images/product_${products.product[item[i]].position}.png" alt="">
                            <span class="vending__left-text">
                                QTY: ${products.product[item[i]].quantity} <span class="vending__left-text-span">&#10072;</span>
                                ${products.product[item[i]].position.toUpperCase()} <span class="vending__left-text-span">&#10072;</span>
                                $${(products.product[item[i]].price / 100).toFixed(2)}
                            </span>
                        </div>
                    `;
                    list.innerHTML += html;
                }
            }
        });
    }
}

const theVendingMachine = new VendingMachine

