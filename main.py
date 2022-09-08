
print (" \n" + "Learning OOP concepts in Python" "\n")



# Creating classes and "Magic Methods"

class Employee:
    """Build a basic employee"""
    def __init__(self, name, age, annual_salary):
        self.name = name
        self.age = age
        self.salary = annual_salary

    def get_name (self):
        return self.name

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary
    


e1 = Employee ("Anthony", 38, 96_000)
e2 = Employee ("Jessica", 39, 100_000)
print (e1.get_name())
print (e1.get_age())
print (e1.get_salary())

print (e2.get_name())
print (e2.get_age)
print (e2.get_salary())

        

