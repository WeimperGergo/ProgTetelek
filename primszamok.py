import math

print("\nnszám: ", end="")
n = int(input())
prim: bool
if n < 2:
    prim = False
else:
    i = 2
    while i <= math.sqrt(n) and n % i != 0:
        i += 1
    prim = bool(i > math.sqrt(n))

if prim:
    print("Prím")
else:
    print("Nem prím")
