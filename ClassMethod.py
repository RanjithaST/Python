class DMART:
    discountOnEachProduct=0.10

    def __init__(self):
        self.gstn=None
        self.location=None

    def calculatePrice(self,prodName,originalPriceOfProduct):
        actualPrice=originalPriceOfProduct-(originalPriceOfProduct*DMART.discountOnEachProduct)
        print("Actual Price of the product",prodName,"is--->",actualPrice)
    
    @classmethod
    def revisedPrice(cls):
        cls.discountOnEachProduct=0.20

d1=DMART()
d1.calculatePrice("Cooker",5000)
d2=DMART()
d2.calculatePrice("Airfryer",8000)
DMART.revisedPrice()
d1.calculatePrice("Cooker",5000)
d2.calculatePrice("Airfryer",8000)
