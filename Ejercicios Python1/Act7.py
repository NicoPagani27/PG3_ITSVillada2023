def numero_step(numero):
    if numero < 10:
        return False
    
    anterior = numero % 10
    numero //= 10

    while numero > 0:
        actual = numero % 10
        if abs(actual - anterior) != 1:
            return False
        anterior = actual
        numero //= 10
    
    return True

while True:
    numero = int(input("Ingrese un número: "))

    if numero_step(numero):
        print("El número", numero, "es un número step.")
    else:
        print("El número", numero, "no es un número step.")