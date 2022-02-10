from controllers.product_controller import ProductController
from views import product_inputs


def add_product(product_controller: ProductController):
    name = product_inputs.input_name()
    description = product_inputs.input_description()
    price_before_tax = product_inputs.input_price_before_tax()
    price_after_tax = product_inputs.input_price_after_tax()
    stock = product_inputs.input_stock()
    category = product_inputs.input_category()

    product_controller.add_product(name, description, price_before_tax, price_after_tax, stock, category)


def view_products(product_controller: ProductController):
    products = product_controller.view_products()

    print("Ok here is a list of all available products:")

    for num, product in enumerate(products, start=1):
        print("Product " + str(num) + ":")
        print("ID: " + str(product.product_id))
        print("Name: " + product.name)
        print("Description: " + product.description)
        print("Price exl. tax: " + str(product.price_before_tax))
        print("Price incl. tax: " + str(product.price_after_tax))
        print("Stock: " + str(product.stock))
        print("Category: " + product.category)
        print("\n----------------------\n")
