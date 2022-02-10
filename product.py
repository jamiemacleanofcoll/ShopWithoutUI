class Product:
    product_id: int
    name: str
    description: str
    price_before_tax: float
    price_after_tax: float
    stock: int
    category: str

    def __init__(self, product_id, name, description, price_before_tax, price_after_tax, stock, category):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price_before_tax = price_before_tax
        self.price_after_tax = price_after_tax
        self.stock = stock
        self.category = category
