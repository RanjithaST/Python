class Employee:
    def __init__(self):
        self.empName=None
        self.empID=None
emp=Employee()
print(emp)
print("**********BEFORE DATA ASSIGN**************")
print(emp.empName)
print(emp.empID)
emp.empName="John"
emp.empRoll=101
print("**********AFTER DATA ASSIGN**************")
print(emp.empName)
print(emp.empID)
emp1=Employee()
print(emp1)