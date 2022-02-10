from controllers.review_controller import ReviewController


def view_reviews(review_controller: ReviewController):
    product_id = input("For which product do you want to see the  reviews?")
    product_id_int = int(product_id) if product_id.isdigit() else None
    if product_id_int is None:
        print("Product id not found")
        return

    reviews = review_controller.view_reviews(product_id_int)

    print("Here are the reviews for product:" + product_id)
    for num, review in enumerate(reviews, start=1):
        print("Review " + str(num) + ":")
        print("\033[4m" + "Review title: " + str(review.review_title) + "\033[0m")
        print("Review text: " + review.review_text)
        print("\n----------------------\n")


def add_review(review_controller: ReviewController):
    product_id = input("Which product do you want to review?")
    product_id_int = int(product_id) if product_id.isdigit() else None
    if product_id_int is None:
        print("Product id not found")
        return

    review_summary = input("Enter review summary")
    review_text = input("Enter review text")
    review_controller.add_review(product_id_int, review_summary, review_text)
