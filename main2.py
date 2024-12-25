class Person:
    def __init__(self, name, age, city, position, salary):
        self.name = name
        self.age = age
        self.city = city
        self.position = position
        self.salary = salary

    def info(self):
        return f"name: {self.name} age: {self.age} city: {self.city} position: {self.position} salary: {self.salary} "


p = Person('Samat', 22, 'Bishkek', 'programmer', 200000)
print(p.name)
print(p.salary)
print(p.info())