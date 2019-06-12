import uuid


class Option:
    def __init__(self, name, value):
        self.id = str(uuid.uuid4())
        self.name = name
        self.value = value
