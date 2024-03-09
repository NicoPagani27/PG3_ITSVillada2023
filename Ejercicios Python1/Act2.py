def año_bisiesto (año):
    if año % 4  == 0:
        return 1
    else:
        return 2

while True:
    año = int(input("Ingrese un año: "))
    valor: int = año_bisiesto(año)
    if valor == 1:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")