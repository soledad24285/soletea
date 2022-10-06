chain = "X-DSPAM-Confidence:0.8475"

p1 = chain.find(":")
print("Indice Inicial: "+ str(p1))

p2 = chain.find("5")
print("Termina en: "+ str(p2))

final = len(chain)
substring = chain[p1+1:final]
showit = float(substring)

print(showit)
print(type(showit))