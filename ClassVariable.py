class Employee:
    companyName="DCL"
    def __init__(self):
        self.empID=None
        self.empName=None #1st way to create instance variable
        print(self)
e1=Employee()
print(e1)
print("***Invoked from class object***",Employee.companyName)
print("***Invoked from object***",e1.companyName)
e1.companyName="Google" ##2nd way to create instance variable
print("***Invoked from object***",e1.companyName)
e1.salary=1000
print(e1.salary)

#Reading/accessing the class variable can be accessed by the class variable as well as object reference
#modifing/writing the class variable only by class name 
#while reading using object reference PVM searches in object dict if not found it searches in class dict and fake it and print
#while modifing using object reference PVM searches in object dict if not found it creates inside the object without modifying class variable
#while modifing using class variable it directly modifies the class variable 