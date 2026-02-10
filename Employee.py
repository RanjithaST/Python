class Employee:
    companyName="DCL"
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
print(Employee.companyName)
print(emp1.companyName)#not recomended