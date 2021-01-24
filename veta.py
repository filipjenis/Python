"""
slova = input("Zadaj zoznam slov:").split(" ")
parne=0
neparne=0

for i in range(0,len(slova)):
    if i%2 == 0: parne=parne+len(slova[i])
    if i%2 == 1: neparne=neparne+len(slova[i])

if parne>=neparne:
    print("Najdlhšia možná veta:", (parne))
else:
    print("Najdlhšia možná veta:", (neparne))


slova = input("Zadaj zoznam slov:").split(" ")
cena = []
max_value=0

for i in range(0,len(slova)):
    cena.append(len(slova[i]))

for j in cena:
    if j>max_value: max_value=j

print(cena)
print(max_value)
"""

def wordCounter(cena,t,sucet):
    for j in cena:
        if cena[t - 1] > cena[t]:
            sucet = sucet + cena[t - 1]
            t += 2
            if t<=(len(cena)-1):
                wordCounter(cena,t,sucet)
            else:
                if (t-1)<=(len(cena)-1):sucet = sucet + cena[t-1]
                return sucet
        if cena[t - 1] < cena[t]:
            sucet = sucet + cena[t]
            t += 3
            if t<=(len(cena)-1):
                wordCounter(cena,t,sucet)
            else:
                if (t-1)<=(len(cena)-1):sucet = sucet + cena[t-1]
                return sucet
        if cena[t - 1] == cena[t]:
            if t+2 > (len(cena)-1) or t+1 > (len(cena)-1):
                sucet = sucet+cena[t]
                return sucet
            else:
                if cena[t + 1] < cena[t + 2]:
                    sucet = sucet + cena[t]
                    t += 3
                    if t <= (len(cena) - 1):
                        wordCounter(cena, t, sucet)
                    else:
                        if t - 1 <= (len(cena) - 1): sucet = sucet + cena[t - 1]
                        return sucet
                else:
                    sucet = sucet + cena[t-1]
                    t += 2
                    if t <= (len(cena) - 1):
                        wordCounter(cena, t, sucet)
                    else:
                        return sucet

slova = input("Zadaj zoznam slov:").split(" ")
suma = []
index = 1
sucet = 0
print(slova)
for i in range(0,len(slova)):
    suma.append(len(slova[i]))

print("Maximalny počet písmen:",(wordCounter(suma,index,sucet)))