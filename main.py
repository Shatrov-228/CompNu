
class Complex:
    
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
        
    def __add__(self, other):
        if (type(other) is float) or (type(other) is int):
            return Complex(self.re + other, self.im + other)
        else:
            return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)
    
    def __mul__(self, other):
        return Complex(self.re*other.re - self.im*other.im, self.re*other.im + self.im*other.re)
    
    def __truediv__(self, other):
        return Complex((self.re*other.re + self.im*other.im)/((other.re)**2+(other.im)**2), (self.im*other.re - self.re*other.im)/((other.re)**2+(other.im)**2))
    
    def __iadd__(self, other):
        self.re = self.re + other.re
        self.im = self.im + other.im
        return Complex (self.re, self.im)
    
    
    def __abs__(self):
        return ((self.re)**2 + (self.im)**2)**0.5
    
    def __str__(self):
        return (f'{self.re}{self.im:+}i')
    
    def __repr__(self):
        return (f'Complex({self.re},{self.im})')
    
A=Complex(23,8)
B=Complex(4,1)
