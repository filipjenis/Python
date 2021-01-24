veta = input('Zadaj vetu:')
veta_upravena = ""

for i in veta:
    if i.isalpha() or i == " ":
        veta_upravena += i
print(veta_upravena)