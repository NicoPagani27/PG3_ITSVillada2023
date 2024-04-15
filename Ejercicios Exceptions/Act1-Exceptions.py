while True:
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        print("La suma es:", num1 + num2)
    except ValueError:
        print("Error: Debe ingresar números enteros.")
    opcion = input("Desea seguir sumando valores? 1 = si, 2 = no: ")
    if opcion == '2':
        break


