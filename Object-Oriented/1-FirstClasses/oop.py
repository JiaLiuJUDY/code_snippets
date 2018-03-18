
class Employee:

    def __init__(self, first, last, pay): 
        # this is a special method which can be treated as a constructor
        # the first arg of this __init__ is always self
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
