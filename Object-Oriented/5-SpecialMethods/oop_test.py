class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay): #__method__: dunder method, indicate special method
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    # an unambiguous represetation of the object, it should be used to debug, log, for developer
    # this is trying to print info which enable us to recreate the object
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    # a more readable represetation, for user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        # add two empolyees' salary
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)

#len is also a special method
print(len(test))
print('test'.__len__())

print(len(emp_1)) 
print(repr(emp_1))
print(str(emp_1))

print (1+2)
print ('a' + 'b')
print(int.__add__(1,2))
print(str.__add__('a', 'b'))
