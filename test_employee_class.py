import unittest

from employee_class import Employee

class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee('Einstein','Albert')
        self.salincre = 34
        self.saldef = self.my_employee.default_salary
        self.saldefincre = self.my_employee.default_salary_increment

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, self.saldef+self.saldefincre)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(self.salincre)
        self.assertEqual(self.my_employee.salary, self.saldef+self.salincre)




unittest.main()