class BookMyShow:
    def __init__(self):
        self.movieName=None
        print(self)
    def assignMovieName(self):
        self.movieName="DRNDR"
        print(self)
print("***OBJ1***")
b=BookMyShow()
print(b)
print(b.movieName)#None
b.movieName="TOXIC"
print(b.movieName)#TOXIC
b.assignMovieName()
print(b.movieName)#DRNDR

print("***OBJ2***")
b1=BookMyShow()
print(b1)
print(b1.movieName)#None
b1.movieName="TOXIC"
print(b1.movieName)#TOXIC
b1.assignMovieName()
print(b1.movieName)#DRNDR

#same variable b can be used but 1st one will be overridden by snd variable
