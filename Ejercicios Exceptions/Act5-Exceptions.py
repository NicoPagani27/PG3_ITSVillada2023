while True:
    print("Elija una opcion: \n")
    print("1. Ingresar Texto")
    print("2. Exit")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        Texto=input("Ingrese el texto que desea: ")
        try:   
            with open("TextoEscrito.txt", "w") as archivo:
                archivo.write(Texto)
        except TypeError as e:
            print("Error: ", e) 
    elif opcion ==  "2":
        break