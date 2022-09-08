
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

    def promote(self):
        """Method to promote an employee"""
        if self._level == "junior":
             self._level = "senior"
        elif self._level == "senior":
            self._level = "CEO"
        self._salary = self._compute_salary()


        

e1 = Employee ("Anthony", 38, "junior")
e2 = Employee ("Jessica", 39, "CEO")

print (f"Employee name is: {e2.get_name()}, Age is: {e2.get_age()}, Salary is: {e2._compute_salary()},  Level is: {e2._get_level()}, ID is: {id(e2)}\n")
print (f"Employee name is: {e1.get_name()}, Age is: {e1.get_age()}, Salary is: {e1._compute_salary()}, Level is: {e1._get_level()}, ID is: {id(e1)}\n")


e1.promote()
print (f"Employee name is: {e1.get_name()}, Age is: {e1.get_age()}, Salary is: {e1._compute_salary()}, Level is: {e1._get_level()}, ID is: {id(e1)}\n")

e1.promote()
print (f"Employee name is: {e1.get_name()}, Age is: {e1.get_age()}, Salary is: {e1._compute_salary()}, Level is: {e1._get_level()}, ID is: {id(e1)}\n")




#                       ~notes~
   """""Python will not prevent the end user from accessing methods or attributes you make private. 
So the moral of the story here is you as a programmer, you're going to be at one side of the table.
You're either the end user of other libraries or you are designing a library yourself.
And most of the time you're playing both roles at the same time. So think about this.
When you are designing a class, think about what the interface between you and the users of your class
is going to be. Think about the methods that you want to expose to them and the methods that you don't want to expose
to them. Think about the attributes that you want to expose to them and the attributes that you don't want to
expose to them.For the four things that are private to your class that you don't want to expose to them, make sure
that the names start with one underscore, OK, this is if you are the class designer, if you are someone
who are using other people's libraries, if you feel tempted to use private methods or private attributes,
think twice about it, because they are private for a reason.
You're not supposed to access them directly."""     
