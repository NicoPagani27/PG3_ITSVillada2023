def dibujo(ancho, largo, caracter):
    for i in range(largo):
        for j in range(ancho):
            print(caracter, end=" ")
        print()

ancho = int(input("Ingresar el ancho: "))
largo = int(input("Ingresar el largo: "))
caracter = input("Ingresar el caracter: ")

dibujo(ancho, largo, caracter)

