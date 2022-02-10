from controllers.order_controller import OrderController
from controllers.review_controller import ReviewController
from views.main_view import menu
from controllers.product_controller import ProductController
from controllers.user_controller import UserController

product_controller = ProductController()
review_controller = ReviewController()
order_controller = OrderController(product_controller)
user_controller = UserController()

while True:
    menu(user_controller, product_controller, review_controller, order_controller)
