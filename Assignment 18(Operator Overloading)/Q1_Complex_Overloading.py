class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
    def __del__(self):
        print(f"Complex number {self.real} + {self.imag}i is destroyed . . !!")
    
    def __add__(self, another):
        return Complex(self.real+another.real, self.imag+another.imag)
    
    def __sub__(self, another):
        return Complex(self.real-another.real, self.imag-another.imag)


A = Complex(10, 15)
print("A : ", A)

B = Complex(2, 7)
print("B : ", B)

C = A + B
print("A + B : ", C)

D = A - B
print("A - B : ", D)