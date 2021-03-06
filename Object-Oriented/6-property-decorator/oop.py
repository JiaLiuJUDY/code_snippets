
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
        
emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim' # originally, full name will be fine, but email will not

emp_1.fullname = 'Corey Schafer' # will get error without the setter function

print(emp_1.first)
print(emp_1.email) # with @property, no need to add () after email
print(emp_1.fullname)
