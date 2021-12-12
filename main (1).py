from math import atan, sin, cos

class Complex():
    
    def __init__(self, re, im=0.0):    # im устанавливаем = 0 для гарантии, что
                                       # число передаваемое пользователем - мнимое
        self.re = re
        self.im = im
    
    
    def conjugate(self):
        return Complex(self.re, -self.im)
    
    
    def __abs__(self):
        return ((self.re)**2 + (self.im)**2)**0.5
    
        
    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            re_p = self.re + other
            im_p = self.im

        if isinstance(other, Complex):
            re_p = self.re + other.re
            im_p = self.im + other.im
            
        return Complex(re_p, im_p)


    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            re_p = self.re - other
            im_p = self.im

        if isinstance(other, Complex):
            re_p = self.re - other.re
            im_p = self.im - other.im
            
        return Complex(re_p, im_p)
    
    
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            re_p = self.re * other
            im_p = self.im * other

        if isinstance(other, Complex):
            re_p = (self.re * other.re) - (self.im * other.im)
            im_p = (self.re * other.im) + (self.im * other.re)
            
        return Complex(re_p, im_p)
    
    def __truediv__(self, other):
        return Complex((self.re*other.re + self.im*other.im)/((other.re)**2+(other.im)**2), (self.im*other.re - self.re*other.im)/((other.re)**2+(other.im)**2))
    
    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __str__(self):
        return (f'{self.re}{self.im:+}i')
    
    def __repr__(self):
        return (f'Complex({self.re},{self.im})')
        
    def arg(self):
        return atan(self.im / self.re)

    def __pow__(self, other):
        """
        Number to a power
        Formula:
            z**n = (r**n)*[cos(n*agr) + sin(n*arg)i], where
        """
        r = abs(self) ** other
        arg_mult = self.arg() * other

        re_p = round(r * cos(arg_mult))
        im_p = round(r * sin(arg_mult))

        return Complex(re_p, im_p)
    

