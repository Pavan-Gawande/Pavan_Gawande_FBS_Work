# Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:
    def __init__(self, bid=101, bname="python", price=200 ,author="pavan"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print(f"Book with Bid {self.bid} is destroyed")

    def showBook(self):
        print(f"Book Id : {self.bid}, Book Name : {self.bname}, Book Price : {self.price}, Author : {self.author}")
        
b1 = Book(112, "mysql", 320, "pavan")
b1.showBook()
del b1

b2 = Book()
b2.showBook()

