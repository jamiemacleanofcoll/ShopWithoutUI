from controllers.order_controller import OrderController
from views.order_inputs import input_firstname, input_lastname, input_delivery_address, input_street, \
    input_house_number, input_zip_code, input_city, input_credit_card_details, input_credit_card_owner, \
    input_credit_card_number, input_cvv, input_valid_month, input_valid_year, input_order_completed


def add_to_cart(order_controller: OrderController, user_id):
    product_id = input("Please enter the product id you want to add to the cart")
    product_id_int = int(product_id) if product_id.isdigit() else None
    if product_id_int is None:
        print("Product id not found")
        return

    product_quantity = input("How many products of " + product_id + " do you want to add to the cart?")
    product_quantity_int = int(product_quantity) if product_quantity.isdigit() else None
    if product_quantity_int is None:
        print("Please enter a digit")
        return

    if order_controller.add_to_cart(user_id, product_id_int, product_quantity_int):
        print("Ok, we added " + product_quantity + " product(s) of product " + product_id + " to your cart!")
    else:
        print("Sorry, there is not enough stock for this product.")


def checkout(order_controller: OrderController, user_id):
    firstname = input_firstname()
    lastname = input_lastname()
    print("What is the delivery address?")
    street = input_street()
    house_number = input_house_number()
    zip_code = input_zip_code()
    city = input_city()
    print("Okay, now we need your Credit Card details:")
    credit_card_owner = input_credit_card_owner()
    credit_card_number = input_credit_card_number()
    cvv = input_cvv()
    valid_month = input_valid_month()
    valid_year = input_valid_year()
    print("Thanks for your order!")

    order_controller.checkout(user_id, valid_month, valid_year, credit_card_owner, credit_card_number, cvv,
                              firstname, lastname, street, house_number, zip_code, city)



