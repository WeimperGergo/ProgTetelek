import math


def kivalasztas():
    prim = False
    n = 9999
    while not prim:
        n += 1
        i = 2  # a feltétel        b feltétel
        while i <= math.sqrt(n) and n % i != 0:
            i += 1
        prim = i > math.sqrt(n)
    print(n)
    # a = Sorozat hossza
    # b = Aktuáls elem prím-e?


def osztok(szam):
    szamok = []
    for i in range(2, int(math.sqrt(szam))):
        if szam % i == 0:
            szamok.append(i)
    return szamok


def osztok_while(szam):
    szamok = []
    i = 2
    while i < math.sqrt(szam):
        if szam % i == 0:
            szamok.append(i)
        i += 1
    return szamok


def kiiras(lista):
    if len(lista) > 0:
        for i in range(0, len(lista)-1):
            print(lista[i], end=" ; ")
        print(lista[-1])
    else:
        print("Nincs osztója!")


nSzam = 10007
# szamLista = osztok(nSzam)
# szamListaWhile = osztok_while(nSzam)
# kiiras(szamLista)
# kiiras(szamListaWhile)
kivalasztas()





