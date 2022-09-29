cuenta = 0
acumulado = 0 
while True:
    try:
        print("Ingrese un numero, para finalizar <exit>")
        dato = input(">>>")
        if (dato == "exit"):
            break
        else:
            cuenta = float(cuenta) +1
            acumulado = float(acumulado) + float(dato)
            average = float(acumulado) / float(cuenta)
    except:
            print("Invalido")
            cuenta = float(cuenta) -1
            continue
print("Numero de entradas: "+ str(cuenta))
print("Acumulado: "+ str(acumulado))
print("Media: "+ str(average))