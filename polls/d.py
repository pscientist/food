class Employee(object):
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
       self.first = first
       self.last = last
       self.email = first + '.' + last + '@email.com'
       self.pay = pay

       Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt

    @classmethod
    def from_string(cls, str):
        first, last, pay = str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        return day.weekday() != 5 or day.weekday != 6


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        # super(().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print("-->" + employee.fullname())


dev1 = Employee('John', 'Smith', 80000)
dev2 = Developer('Jan', 'Smith', 90000, 'Java')
mgr = Manager('Sue', 'Smith', 90000, [dev1, dev2])

# print(mgr.email)
# print(mgr.print_employees())
# print(isinstance(mgr, Manager))
# print(isinstance(mgr, Developer))
# print(isinstance(mgr, Employee))
print(issubclass(Manager, Employee))
#
# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
#
# print(dev2.pay)
# dev2.apply_raise()
# print(dev2.pay)
# dev2.prog_lang = 'C'
# print(dev2.prog_lang)
#




# emp1 = Employee('John', 'Smith', 80000)
# emp2 = Developer('Jan', 'Smith', 90000)
# Employee.set_raise_amt(1.06)
#
# emp_str_1 = 'John-Doe-700000'
# emp_str_2 = 'Jane-Doe-700000'
# emp_str_3 = 'David-Smith-700000'
#
# emp3 = Employee.from_string(emp_str_1)
#
# print(emp1.pay)
# print(emp2.pay)
# print(emp3.fullname())
# print(emp1.raise_amt)
# print(emp2.raise_amt)
# print(Employee.raise_amt)
#
# import datetime
# my_date = datetime.date(2017, 7, 22)
#
# print(Employee.is_workday(my_date))
