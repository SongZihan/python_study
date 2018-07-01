class Employee():
    '''计算雇员年薪'''
    def __init__(self,first_name,last_name,annual_pay):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_pay = int(annual_pay)

    def get_raise(self,pay_raise=''):
        '''如果有年薪增加量，则加上；如果没有提供，则默认加5000'''
        while pay_raise:
            self.annual_pay += int(pay_raise)
            break
        else:
            self.annual_pay += 5000
        return self.annual_pay

em = Employee("song","zihan","8000")
em.get_raise()

