class Book:
    cnt = 0
    def __init__(self, bid=0, bname="", price=0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.cnt += 1
    
    def showBook(self):
        print(f"{self.bid} : {self.bname} written by {self.author} is for price {self.price}\n")
    
    def showCount(self):
        print(f"Total no. of books are : {Book.cnt}\n")
    
    def __del__(self):
        Book.cnt -= 1
        print(f"{self.bid} : {self.bname} is removed . .!!\n{Book.cnt} Books remains\n")

b1 = Book(101, "python", 200, 'G. Rossum')
b1.showBook()

b2 = Book(102, 'c++', 150, 'P. Gawande')
b2.showBook()
b2.showCount()

b3 = Book(103, 'Java', 230, 'Pavan')
b3.showBook()
b2.showCount()

del b2
b3.showCount()