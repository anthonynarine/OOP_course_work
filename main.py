

print (" \n" + "Learning OOP concepts in Python" "\n")



# Creating classes and "Magic Methods"

class Employee:
    """Build a basic employee"""
    def __init__(self, name, age=None,  level = "junior"): # None makes the paramaters optional.
        self.name = name
        self.age = age
        self.salary = self._compute_salary (level)

    def get_name (self):
        """Method to obtain an employee name"""
        return self.name

    def get_age(self):
        """Method to obtain an employee's age"""
        return self.age

    def get_salary(self):
        """ Method to obtain an employee salary"""
        return self.salary

    def _compute_salary (self, level): 
        if level == "junior":
            return 10_000
        elif level == "senior":
            return 20_000
        elif level == "CEO":
            return 100_0000
        else:
            print ("unknown level")

    


    
    


e1 = Employee ("Anthony", 38, "senior")
e2 = Employee ("Jessica", 39, "junior")

print (f"Employee name is {e1.get_name()}, age is {e1.get_age()}, salary is {e1.get_salary()}\n")


        

