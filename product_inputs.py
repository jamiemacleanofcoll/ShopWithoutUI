def input_name():
    name = input("What is the name of the product?")
    while len(name) < 3 or not name[0].isupper():
        name = input("Sorry, your product name must have at least 3 characters starting with a capital letter. "
                     "Please enter a new one")
    return name


def input_description():
    description = input("What is the product description?")
    while len(description) < 3:
        description = input(
            "Sorry, your product description must have at least 3 character."
            "Please enter a new one")
    return description


def input_price_before_tax():
    price_before_tax = input("What is the price before tax?")
    return price_before_tax


def input_price_after_tax():
    price_after_tax = input("What is the price after tax?")
    return price_after_tax


def input_stock():
    stock = input("What is the stock?")
    return stock


def input_category():
    category = input("What is the product category?")
    return category
