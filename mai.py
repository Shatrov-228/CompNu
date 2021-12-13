import math

class Complex():
    
    def __init__(self, re, im=0.0):    # im устанавливаем = 0 для гарантии, что
                                       # число передаваемое пользователем - мнимое
        self.re = re
        self.im = im
    
    
    def conj(self):
        return Complex(self.re, -self.im)
    
    
    def abs(self):
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
        return Complex((self.re*other.re + self.im*other.im)/((other.re)**2+(other.im)**2), 
                       (self.im*other.re - self.re*other.im)/((other.re)**2+(other.im)**2))
    
    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __ne__(self, other):
        return not self.__eq__(other)
        
    def arg(self):
        return math.atan(self.im / self.re)
    
    def __str__(self):
        if self.im == 0 and self.re != 0:
            return str(self.re)
	        
        elif self.re == 0 and self.im != 0:
            return str(self.im)+'i'
			
        elif self.im < 0:
            return '{}-{}i'.format(self.re, -self.im)
			
        elif self.im > 0:
            return '{}+{}i'.format(self.re, self.im)
			
        else:
            return '0'

    def __pow__(self, n):
        """
        Number to a power
        Formula:
            z**n = (r**n)*[cos(n*arg) + sin(n*arg)i], where
        """
        r = abs(self) ** n
        arg_mult = self.arg() * n

        re_p = round(r * math.cos(arg_mult))
        im_p = round(r * math.sin(arg_mult))

        return Complex(re_p, im_p)

if __name__ == '__main__':
    x = Complex(10,2)
    y = Complex(-10,0)
        