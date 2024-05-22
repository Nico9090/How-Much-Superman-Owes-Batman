#!/usr/bin/env python3

#Manage employee information

class Employee:
        def __init__(self,emp_id,emp_name,emp_salary,emp_dept):
                self.emp_id=emp_id
                self.emp_name=emp_name
                self.emp_salary=emp_salary
                self.emp_dept=emp_dept
        def calc_emp_salary(self,overtime):
                return  self.emp_name+ ' makes ' + '$'+str((overtime * (self.emp_salary / 50)))
        def change_assignment(self,department):
                return '%s now works at %s' % (self.emp_name,department)
if __name__ == "__main__":
        emp1=Employee('1572132','Clark Kent',90,'Journalism')
        print(emp1.calc_emp_salary(10))
        print(emp1.change_assignment('Daily Planet'))

