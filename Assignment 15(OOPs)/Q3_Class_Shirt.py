# Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc).
# Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:
    def __init__(self, sid=101, sname="polo", type="casual", price=1000 ,size = "medium"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print(f"Shirt with sid {self.sid} is destroyed")

    def showShirt(self):
        print(f"Shirt Id : {self.sid}, Shirt Name : {self.sname}, Shirt Type : {self.type}, Price : {self.price}, Size : {self.size}")
        
S1 = Shirt()
S1.showShirt()
del S1

S2 = Shirt(112,"raymond", "formal", 1500, 'small')
S2.showShirt()