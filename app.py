class App:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    def __str__(self):
        return f"{self.name} is a(a) {self.category} app that is {self.description}."