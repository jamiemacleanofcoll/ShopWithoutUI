class Review:
    review_id: int
    review_title: str
    review_text: str
    product_id: int

    def __init__(self, review_id, review_title, review_text, product_id):
        self.review_id = review_id
        self.review_title = review_title
        self.review_text = review_text
        self.product_id = product_id

