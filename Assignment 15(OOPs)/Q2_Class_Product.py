# Create a class Product with members as pid,pname,price and quantity .Add following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:
    def __init__(self, pid=101, pname="Pen", price=25 ,quantity = 100):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print(f"Product with pid {self.pid} is destroyed")

    def showProduct(self):
        print(f"Product Id : {self.pid}, Product Name : {self.pname}, Price : {self.price}, Quantity : {self.quantity}")
        
pen = Product()
pen.showProduct()
del pen

pencil = Product(123, "Pencil", 10, 50)
pencil.showProduct()