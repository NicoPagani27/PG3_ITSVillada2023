def buscar_valor (lista, elemento_buscado):
    if elemento_buscado in lista:
        return lista.index(elemento_buscado)
    else:
        return -1

lista = [8, 12, 9, 45]
while True:
    elemento_buscado = int(input("Ingrese el valor para buscar: "))

    indice = buscar_valor(lista, elemento_buscado)

    if indice != -1:
        print(f"El valor {elemento_buscado} se encuentra en el índice {indice} de la lista.")
    else:
        print(f"El valor {elemento_buscado} no se encuentra en la lista.")

