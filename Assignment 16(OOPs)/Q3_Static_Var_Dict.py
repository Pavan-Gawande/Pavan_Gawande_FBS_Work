class Shirt:
    sizeMultiplier = {
        'small' : 1,
        'medium' : 1.1,
        'large' : 1.2,
        'xlarge' : 1.3
    }
    def __init__(self, sid=0, sname="", type="", price=0 ,size = "small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
    
    def showShirt(self):
        print(f"Shirt Id : {self.sid}, Shirt Name : {self.sname}, Shirt Type : {self.type}, Price : {self.price}, Size : {self.size}\n")
    
    def calcFinalPrice(self, forSize):
        basePrice = self.price/Shirt.sizeMultiplier[self.size]
        print(f'Final price for {self.sname} for size {forSize} is {basePrice*Shirt.sizeMultiplier[forSize]}')
    
    def __del__(self):
        print(f"Shirt with sid {self.sid} is removed\n")

        
S1 = Shirt()       #blank object
S1.showShirt()
del S1

S2 = Shirt(112,"raymond", "formal", 1000, 'small')
S2.showShirt()
S2.calcFinalPrice('medium')
S2.calcFinalPrice('xlarge')