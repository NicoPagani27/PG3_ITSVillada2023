def ordenamiento(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista = [12,67,32,56,2,1]
print("la lista desordenada es: ", lista)
lista_ordenada = ordenamiento(lista)
print("la lista ordenada es: ",ordenamiento(lista))
