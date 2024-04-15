while True:
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        print("La division es:", num1 / num2)
    except ZeroDivisionError:
        print("Error: No se peude dividir un numero por cero.")
    opcion = input("Desea seguir dividiendo valores? 1 = si, 2 = no: ")
    if opcion == '2':
        break