def palindromo(palabra):
    palabra_palindroma = palabra[::-1]
    if palabra == palabra_palindroma:
        return True
    else:
        return False
while True:
    palabra = input("Ingrese la palabra: ")
    if palindromo(palabra):
        print("La palabra es palindroma")
    else:
        print("la palabra no es palindrma")
