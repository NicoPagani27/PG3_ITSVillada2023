class Operaciones:
    def __init__(self):
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        self.hacer_operaciones(num1, num2)

    def hacer_operaciones(self, num1, num2):
        suma = num1 + num2
        print("la suma es: ", suma)
        resta = num1 - num2
        print("la resta es: ", resta)
        multi = num1 * num2
        print("la multiplicacion es: ", multi)

        if num2 != 0:
            div = num1 / num2
            print("La división es:", div)
        else:
            print("No se puede dividir por cero.")

operaciones = Operaciones()