class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        if self.lado1 < self.lado2 and self.lado2 > self.lado3:
            print("El lado mayor del triángulo es:", self.lado2)
        elif self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado mayor del triángulo es:", self.lado1)
        elif self.lado3 > self.lado2 and self.lado3 > self.lado1:
            print("El lado mayor del trianulo es:", self.lado3)

    def equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            return True
        else:
            return False
        
lado1 = float(input("Ingrese el largo del primer lado del triángulo: "))
lado2 = float(input("Ingrese el largo del segundo lado del triángulo: "))
lado3 = float(input("Ingrese el largo del tercer lado del triángulo: "))
    
triangulo = Triangulo(lado1, lado2, lado3)
triangulo.lado_mayor() 

if triangulo.equilatero():
    print("El triángulo es equilátero.")
else:
    print("El triángulo no es equilátero.")

    
        


        