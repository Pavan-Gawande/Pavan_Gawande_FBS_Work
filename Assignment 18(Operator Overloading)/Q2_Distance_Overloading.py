class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
    
    def __str__(self):
        return f"{self.km} km, {self.m} m, {self.cm} cm"
    
    def __del__(self):
        print(f'Distance object of {self.km}, {self.m}, {self.cm} is deleted . .!!')
    
    def __add__(self, other):
        cm = self.cm + other.cm
        m = self.m + other.m
        km = self.km + other.km
        if(cm >= 100):
            m += cm // 100
            cm %= 100
        elif(m >= 1000):
            km += m // 1000
            km %= 1000
        return Distance(km, m, cm)
    
    def __sub__(self, other):
        a = self.km*100000 + self.m*100 + self.cm
        b = other.km*100000 + other.m*100 + other.cm
        res = a-b
        km = res // 100000
        res %=  100000
        m = res // 100
        res %= 100
        return Distance(km, m, res)

d1 = Distance(10, 12, 23)
print("d1 : ", d1)

d2 = Distance(9, 13, 24)
print("d2 : ", d2)

d3 = d1 + d2
print("d1 + d2 : ", d3)

d4 = d1 - d2
print("d1 - d2 : ", d4)