from controllers.user_controller import UserController
from views.user_inputs import input_firstname, input_lastname, input_date_of_birth, input_username, input_password


def create_user(user_controller: UserController):
    firstname = input_firstname()
    lastname = input_lastname()
    date_of_birth = input_date_of_birth()
    username = input_username()
    password = input_password()

    user_controller.create_user(
        firstname=firstname,
        lastname=lastname,
        date_of_birth=date_of_birth,
        username=username,
        password=password
    )


def login(user_controller: UserController):
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    if user_controller.login(username, password):
        print("You are logged in")

    else:
        print("Your username and password did not match")


def change_user(user_controller: UserController):
    current_user = user_controller.view_account()
    if current_user is None:
        print("You are not logged in")
        return
    attribute = input("Which attribute do you want to change? (firstname, lastname, date of birth, username, password)")

    if attribute == "firstname":
        value = input_firstname()
    elif attribute == "lastname":
        value = input_lastname()
    elif attribute == "date of birth":
        value = input_date_of_birth()
    elif attribute == "username":
        value = input_username()
    elif attribute == "password":
        value = input_password()
    else:
        print("Your attribute does not exist")

        return

    if user_controller.change_attribute(attribute, value):
        print("Your " + attribute + " has been changed!")
    else:
        print("You are not logged in")


def view_account(user_controller: UserController):
    current_user = user_controller.view_account()
    if current_user is not None:
        print("Your account: ")
        print("First name: ", current_user.firstname)
        print("Last name: ", current_user.lastname)
        print("Date of birth: ", current_user.date_of_birth)
        print("Username: ", current_user.username)
        print("Password: ", current_user.password)

    else:
        print("You are not logged in")


def logout(user_controller):
    user_controller.logout()
    print("You are logged out")
