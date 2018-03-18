# regular method automatically take in the instance as the first argument - self
# class method automatically take in the class as the first argument - cls
# static method don't pass anything automatically, just like normal function

class Employee:

    num_of_emps = 0 # track how many employee we have in the database
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay 
        
        Employee.num_of_emps += 1
        # __init__ method runs every time we create a new employee
        # use Employee.num_of_emps instead of self.num_of_emps, since this number is connected with the whole dataset

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        # self.pay = int(self.pay * Employee.raise_amt) also works
    
    '''
    def apply_raise(self):
        self.pay = int(self.pay * raise_amt)
    # this will generate an error called name not defined
    # reason:
    # when we access the class variables, we need either access them through the class itself or an instance of the class
    '''
    
    # class method
    # working with the class instead of the instance
    # add decorator to the top
    @classmethod
    def set_raise_amt(cls, amount): # convention: first argument is cls
        cls.raise_amt = amount
    
    # why people say they useing class method as an alternative of constructor?
    @classmethod
    def from_string(cls, emp_str): 
        #the method which will be used as a constructor has a name convention - start with 'from'
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # creat the new employee object and return it

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # dates have weekday method, 5 <=> Saturday
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# all of the following yield the same result
# the instance doesn't have raise_amt attribute, so program will find class variables
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(emp_1.__dict__)
print(Employment.__dict__)

# assign new raise_amt value through the class will change the whole thing
Employee.raise_amt = 1.05
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# assign new raise_amt value through an instance will automatically generate an attribute called raise_amt to this instance
# and only change this instance's raise_amt value
emp_1.raise_amt = 1.05
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# after adding set_raise_amt class method
Employee.set_raise_amt(1.05) # instead of Employee.raise_amt = 1.05
emp_1.set_raise_amt(1.05) # does the same thing


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# user has to parse the string and put arguement to create the obj
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

# with from_string method, no need to do it themselves
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
