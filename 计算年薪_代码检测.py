import unittest
from experence import Employee

class Test_Payed(unittest.TestCase):
    '''测试Employee类'''
    def setUp(self):
        self.employee_01 = Employee("li", "lianjie", "10000")
        self.pay = [15000,30000,20000]


    def test_none_payraise_input(self):
        '''测试没有payraise输入时程序的运行情况'''

        self.assertEqual(self.employee_01.get_raise(),self.pay[0])

    def  test_payraise_input(self):
        '''测试有payraise输入时程序运行'''

        self.assertEqual(self.employee_01.get_raise(self.pay[2]),self.pay[1])

unittest.main()
