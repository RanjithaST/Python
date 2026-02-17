#Decorators add extra power to existing function and they mainly used for loggers-logging operation
#Eg:Graphana
class Test:
    def verifyUser(func_name):#step 2
        def wrapper_name(self): #need to pass self in new version
            print("Verifying user...")
            func_name(self)
            print("User has completed the operation,logged out successfully.")
        return wrapper_name
    
    @verifyUser #Decorator
    def startTest(self):
        print("User started the test")
    
    @verifyUser
    def applyForHallTicket(self):
        print("User applied for hallticket")
s=Test()
s.applyForHallTicket() #1 step
s.startTest()

'''
Output:
.
User applied for hallticket
User has completed the operation,logged out successfully.
Verifying user...
User started the test
User has completed the operation,logged out successfully.
'''