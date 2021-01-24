veta = input("Zadaj vetu:").upper()
veta = list(veta)
pismena = [0] * 26
ls = []
c = 0

for i in veta:
    if i.isalpha():
        pismena[ord(i)-65] += 1
for i in range(26):
    ls.append(chr(65+i))
    ls.append(pismena[i])
for i in ls:
    if i == 0:
        ls.pop(c)
        ls.pop(c-1)
    c += 1

print(ls)