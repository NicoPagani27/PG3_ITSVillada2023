def dibujo(ancho, largo, caracter):
    for i in range(largo):
        for j in range(ancho):
            print(caracter, end=" ")
        print()
     
def dibujo_triangular(altura, caracter1):
    for i in range(1, altura + 1):
        print(caracter1 * i) 

ancho = int(input("Ingresar el ancho del cuadrado: "))
largo = int(input("Ingresar el largo del cuadrado: "))
caracter = input("Ingresar el caracter del cuadrado: ")

dibujo(ancho, largo, caracter)

altura = int(input("Ingresar la altura del triángulo: "))
caracter1 = input("Ingresar el caracter: ")

dibujo_triangular(altura, caracter1)