import re


def input_firstname():
    firstname = input("What is your first name?")
    while len(firstname) < 3 or not firstname[0].isupper():
        firstname = input("Sorry, your first name must have at least 3 characters starting with a capital letter. "
                          "Please enter a new one")
    return firstname


def input_lastname():
    lastname = input("What is your last name?")
    while len(lastname) < 3 or not lastname[0].isupper():
        lastname = input("Sorry, your last name must have at least 3 characters starting with a capital letter. "
                         "Please enter a new one")
    return lastname


def input_date_of_birth():
    date_of_birth = input("What is your date of birth?")
    return date_of_birth


def input_username():
    username = input("What is your username?")
    return username


def input_password():
    password = input("What is your password?")
    # regex muss folgende bedingungen erfüllen
    while not re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}", password):
        password = input("Sorry, your password is not strong enough. Please enter a new one (must contain at least 8 "
                         "characters, one uppercase letter, one lowercase letter and one number)")
    return password
