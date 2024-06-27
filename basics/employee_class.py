class Employee():

    default_salary = 100
    default_salary_increment = 10

    def __init__(self, last_name, first_name, salary=default_salary):
        self.last_name = last_name
        self.first_name = first_name
        self.salary = salary

    def give_raise(self,raisenum=default_salary_increment):
        self.salary += raisenum



