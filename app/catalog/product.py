import uuid


class Product:
    def __init__(self, name, category, options=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.category = category
        if options is None:
            self.options = []
        else:
            self.options = options

    def add_option(self, option):
        self.options.append(option)
