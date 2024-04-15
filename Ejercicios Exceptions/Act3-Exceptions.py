meses_del_año = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

while True:
    try:
        numero_mes = int(input("Ingrese el número de mes (1-12): "))
        if 1 <= numero_mes <= 12:
            mes = meses_del_año[numero_mes - 1]
            print("El mes que corresponde al número", numero_mes, "es:", mes)
            break
        else:
            print("Error: El número de mes debe estar entre 1 y 12. Ya que son 12 meses")
    except IndexError:
        print("Error: El número de mes ingresado está fuera del rango (1-12).")