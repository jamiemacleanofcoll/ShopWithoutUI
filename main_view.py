from models.user import Role
from views.order_view import add_to_cart, checkout
from views.product_view import add_product, view_products
from views.review_view import view_reviews, add_review
from views.user_view import create_user, login, view_account, change_user, logout


def menu(user_controller, product_controller, review_controller, cart_controller):
    my_input = input("What do you want to do?")

    if my_input == "createAccount":
        create_user(user_controller)

    elif my_input == "login":
        login(user_controller)

    elif my_input == "logout":
        logout(user_controller)

    elif my_input == "viewAccount":
        view_account(user_controller)

    elif my_input == "changeUser":
        change_user(user_controller)

    elif my_input == "viewAccount":
        view_account(user_controller)

    elif my_input == "addProduct":
        current_user = user_controller.view_account()
        if current_user is not None:
            if current_user.role == Role.ADMIN:
                add_product(product_controller)
            else:
                print("You are not an admin!")
        else:
            print("You are not logged in!")

    elif my_input == "viewProducts":
        view_products(product_controller)

    elif my_input == "viewReviews":
        view_reviews(review_controller)

    elif my_input == "addReview":
        add_review(review_controller)

    elif my_input == "addToCart":
        current_user = user_controller.view_account()
        if current_user is not None:
            add_to_cart(cart_controller, current_user.user_id)
        else:
            print("You are not logged in!")

    elif my_input == "checkout":
        current_user = user_controller.view_account()
        if current_user is not None:
            checkout(cart_controller, current_user.user_id)
        else:
            print("You are not logged in!")

    else:
        print("Function not available!")
