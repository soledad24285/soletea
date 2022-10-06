try:
    fname = input("Ingrese el archivo\n>>>")
    file = open(fname, "r", encoding="UTF-8")

    for linea in file:
        print(linea.upper())
except:
    print("Intentelo nuevamente")