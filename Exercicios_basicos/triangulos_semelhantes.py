class Triangulo:
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isósceles'
        else:
            return 'escaleno'
        
    def retangulo(self):
        l1,l2,hp = sorted([self.a,self.b,self.c])
        return abs(hp**2 - l1**2 - l2**2) < 0.000001
    
    def semelhantes(self,t):
        l1,l2,hp = sorted([self.a,self.b,self.c])
        l12,l22,hp2 = sorted([t.a,t.b,t.c])
        return (hp/hp2) == (l1/l12) == (l2/l22)
