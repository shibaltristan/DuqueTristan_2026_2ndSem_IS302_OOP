class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def display_info(self):
        return f"name: {self.name}, age: {self.age}"