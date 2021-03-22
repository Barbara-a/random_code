import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def testDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        self.emp_1 = Employee('Ann', 'Sue', 50000)
        self.emp_2 = Employee('Bob', 'Smith', 60000)

    def testDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'Ann.Sue@email.com')
        self.assertEqual(self.emp_2.email, 'Bob.Smith@email.com')

        self.emp_1.first = 'Caren'
        self.emp_2.last = 'Doe'

        self.assertEqual(self.emp_1.email, 'Caren.Sue@email.com')
        self.assertEqual(self.emp_2.email, 'Bob.Doe@email.com')

    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'Ann Sue')
        self.assertEqual(self.emp_2.fullname, 'Bob Smith')

        self.emp_1.first = 'Caren'
        self.emp_2.last = 'Doe'

        self.assertEqual(self.emp_1.fullname, 'Caren Sue')
        self.assertEqual(self.emp_2.fullname, 'Bob Doe')

    def test_apply_raise(self):

        self.assertEqual(self.emp_1.pay, 50000)

        self.emp_1.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Sue/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Bob/June')
            self.assertEqual(schedule, 'Bad_Response')



if __name__ == '__main__':
    unittest.main()
