def contar_vocales(frase):
    contador = 0
    vocales = {'a', 'e', 'i', 'o', 'u'} 
    for vocal in frase:
        if vocal in vocales:
            contador += 1
    return contador        

frase: str= input("Ingrese una frase: ")

cant_vocales = contar_vocales(frase)

print("La cantidad de vocales en la frase es:", cant_vocales)