import re


def input_firstname():
    firstname = input("What is your first name?")
    while len(firstname) < 3 or not firstname[0].isupper():
        firstname = input("Sorry, your first name must have at least 3 characters starting with a capital letter. "
                          "Please enter a new one.")
    return firstname


def input_lastname():
    lastname = input("What is your last name?")
    while len(lastname) < 3 or not lastname[0].isupper():
        lastname = input("Sorry, your last name must have at least 3 characters starting with a capital letter. "
                         "Please enter a new one.")
    return lastname



def input_street():
    street = input("Street: ")
    while len(street) < 3 or not street[0].isupper():
        street = input("Sorry, your street name must have at least 3 characters starting with a capital letter. "
                       "Please enter a new one.")
    return street


def input_house_number():
    house_number = input("House number: ")
    """[\d] ja oder nein?"""
    while not re.fullmatch(r"^(?=.*\d)[\d]{1,}", house_number):
        house_number = input("Sorry, your house number must have at least one number (no alphabetic characters). Please "
                            "enter a new one.")
    return house_number


def input_zip_code():
    zip_code = input("ZIP Code: ")
    """[\d] ja oder nein?"""
    while not re.fullmatch(r"^(?=.*\d)[\d]{5}", zip_code):
        zip_code = input("Sorry, your ZIP Code must consist of exactly five numbers! Please enter a new one.")
    return zip_code


def input_city():
    city = input("City: ")
    return city



def input_credit_card_owner():
    credit_card_owner = input("Credit Card Owner (first and last name): ")
    """WIE MACHT MAN SPACE MIT IN DIE FUNKTION UND MUSS ECKIGE KLAMMER REIN"""
    while not re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])[a-zA-Z]{6,}", credit_card_owner):
        credit_card_owner = input("Sorry, you need to include min. six alphabetic characters and at least one space. Please try again.")
    return credit_card_owner


def input_credit_card_number():
    credit_card_number = input("Credit Card Number: ")
    while not re.fullmatch(r"^(?=.*\d)[\d]{16}", credit_card_number):
        credit_card_number = input("Sorry, your Credit Card Number must constist of 16 numbers. Please try again.")
    return credit_card_number


def input_cvv():
    cvv = input("CVV: ")
    while not re.fullmatch(r"^(?=.*\d)[\d]{3}", cvv):
        cvv = input("Sorry, your CVV must consist of excatly three numbers. Please try again.")
    return cvv


def input_valid_month():
    valid_month = input("Credit Card valid until (month): ")
    while


def input_valid_year():
    valid_year = input("Credit Card valid until (year): ")
    while valid_year > 2020 and


