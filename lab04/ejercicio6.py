def calQ(notes):
 if notes >= 0 and notes <= 100:
    if notes > 90:
        grade = print("sobresaliente")
    elif notes >80 and notes <=90:
        grade = print("notable")
    elif notes >70 and notes <=80:
        grade = print("Bien")
    elif notes >60 and notes <=70:
        grade = print("Suficiente")
    elif notes <=60:
        grade = print("Insuficiente")
    return grade

print("welcome!")
try:
 notes = float(input("Ingrese la calificacion\n"))
 calQ(notes)
except:
    print("Ingrese un numero entre el 1 y 100")