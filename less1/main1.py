class Person:
    name = 'Samat'
    age = 22
    city = 'Bishkek'
    position = 'programmer'
    salary = 200000

    def info(self):
        return f"name: {self.name} age: {self.age} city: {self.city} position: {self.position} salary: {self.salary} "


p = Person()
print(p.name)
print(p.salary)
print(p.info())

