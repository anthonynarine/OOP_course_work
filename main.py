
print (" \n" + "Learning OOP concepts in Python" "\n")



# Creating classes and "Magic Methods"

class Employee:
    """Build a basic employee"""
    def __init__(self, name, age, annual_salary):
        self.name = name
        self.age = age
        self.salary = annual_salary

    def get_name (self):
        """Method to obtain an employee name"""
        return self.name

    def get_age(self):
        """Method to obtain an employee's age"""
        return self.age

    def get_salary(self):
        """ Method to obtain an employee salary"""
        return self.salary

    def get_raise(self, bonus):
        """Method to give an employee a raise"""
        self.salry += bonus

    
    


e1 = Employee ("Anthony", 38, 96_000)
e2 = Employee ("Jessica", 39, 100_000)
print (e1.get_name())
print (e1.get_age())
print (e1.get_salary())
print (id(e1))

print (e2.get_name())
print (e2.get_age())
print (e2.get_salary())
print (id(e2))

        

