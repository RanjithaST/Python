class BookMyShow:
    def makePayment(self):
        print("Payment is successful")
b=BookMyShow()
print(b.__dict__)#{}
b.makePayment()#even if dict is empty this line is executing the instance method

##Internal working of b.makePayment()
print(b.__class__) #<class '__main__.BookMyShow'>
print(b.__class__.__dict__)#<class '__main__.BookMyShow'>{'__module__': '__main__', 'makePayment': <function BookMyShow.makePayment at 0x0000022C88D49DA0>, '__dict__': <attribute '__dict__' of 'BookMyShow' objects>, '__weakref__': <attribute '__weakref__' of 'BookMyShow' objects>, '__doc__': None}
print(b.__class__.__dict__['makePayment'])#dict is accessed using key makePayment -> <function BookMyShow.makePayment at 0x0000028ED8BC9DA0>