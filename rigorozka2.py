#Filip Jenis, kvinta B
#Úloha: Rigorózka bez itertools

def permutations(lst):
  if len(lst) == 0:
    return []
  elif len(lst) == 1:
    return [lst]
  else:
    l = []
    for i in range(len(lst)):
      x = lst[i]
      xs = lst[:i] + lst[i+1:]
      for p in permutations(xs):
        l.append([x]+p)
    return l

veta = input("Zadaj vetu:").split(" ")
for j in permutations(veta):
  print(" ".join(j))