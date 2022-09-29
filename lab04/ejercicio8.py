max = 0 
min = 1000000000000000000000000000000000000000000000000000000000000000000
while True:
 try:
    entrada = input("typee su dato\n")
    if (entrada == "exit"):
        break
    else:
     if int(max) < int(entrada):
        max = entrada
     if int(min) > int(entrada):
        min = entrada
 except:
       print("invalido")
       continue
print("maximo es: "+ str(max))
print("minimo es: "+ str(min))