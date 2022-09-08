

from typing_extensions import Self


print (" \n" + "Learning OOP concepts in Python" "\n")



# Creating classes and "Magic Methods"

class Employee:
    """Build a basic employee"""
    def __init__(self, name, age, level ): # None makes the paramaters optional to the end user.
        self.name = name
        self.age = age
        self._level = level                          
        self._salary = self._compute_salary     # note the "_" at self_salary and self_level indicates end user should not directly call this

    def get_name (self):
        """Method to obtain an employee name"""
        return self.name

    def get_age(self):
        """Method to obtain an employee's age"""
        return self.age

    def _get_salary(self):
        """ Method to obtain an employee salary"""
        return self._salary

    def _get_level(self):
        """Method to obtain the employee's level"""
        return self._level

    def _compute_salary (self): 
        """Method to compute an employee's base salary based on level"""
        if self._level == "junior":
            return 10_000
        elif self._level == "senior":
            return 20_000
        elif self._level == "CEO":
            return 100_0000
        else:
            print ("unknown level")

    def promote (self):
        if self._level == "junior":
             self._level = "senior"
        elif self._level == "senior":
            self._level = "CEO"
        self._compute_salary()


        

e1 = Employee ("Anthony", 38, "senior")
e2 = Employee ("Jessica", 39, "CEO")

print (f"Employee name is: {e1.get_name()}, Age is: {e1.get_age()}, Salary is: {e1._compute_salary()}, Level is: {e1._get_level()}, ID is: {id(e1)}\n")
print (f"Employee name is: {e2.get_name()}, Age is: {e2.get_age()}, Salary is: {e2._compute_salary()},  Level is: {e2._get_level()}, ID is: {id(e2)}\n")



        

