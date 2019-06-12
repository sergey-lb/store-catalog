class Catalog:
    def __init__(self):
        self.products = []

    def add_product(self, item):
        self.products.append(item)

    def search_by_name(self, name):
        return list(filter(lambda x: name.lower() in x.name.lower(), self.products))
