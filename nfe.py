class NFe:

    def __init__(self):
        self._products = []

    def get_products(self):
        return self._products

    def set_products(self, product):
        self._products.append(product)
