class Product:
    discount = 10              # 10%
    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
    
    def showProduct(self):
        print(f'{self.pid}:{self.pname} for rs.{self.price} available in quantity : {self.quantity}\n')
    
    def calcFinalPrice(self):
        finalPrice = self.price*((100-Product.discount)/100)
        print(f"Final price for {self.pid}:{self.pname} after {Product.discount}% discount : {finalPrice}\n")
    
    def changeDiscount(self, newDiscount):
        Product.discount = newDiscount
        print(f"updates discount is {Product.discount}")
    
    def __del__(self):
        print(f'{self.pid}:{self.pname} is removed . . !!')
        

p1 = Product(101, 'pen', 10, 130)
p1.showProduct()

p2 = Product(102, 'pencil', 5, 150)
p2.showProduct()

p3 = Product(103, 'divider', 20, 90)
p3.showProduct()
p3.calcFinalPrice()