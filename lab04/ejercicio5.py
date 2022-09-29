print("Bienvenido!, ingrese sus parametros")
def calculopago(hr, pay):
    if float(hr) > 40:
        extra = float(hr) - 40
        sal = 40*float(pay) + 1.5*float(pay)*float(extra)
        print("Usted recibira "+ str(sal)+ " Lempiras")
    else:
        sal = float(hr)*float(pay)
        print("Usted recibira "+ str(sal)+ " Lempiras")
    return sal

try:
 hr = input("Ingrese el numero de Horas trabajadas\n")
 pay = input("Ingrese el pago por Hora\n")
 calculopago(hr, pay)
except:
    print("ingrese numeros")