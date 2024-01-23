from Szek import Szek


def peldanyokLista():
    peldany1 = Szek("Kék", 3)
    peldany2 = Szek("Lila", 4)
    peldany3 = Szek("Zöld", 5)

    lista: list[Szek] = [peldany1, peldany2, peldany3]
    return lista


def peldanyok_kiirasa(lista: list[Szek]):
    for i in range(0, len(lista)):
        print(f"{i+1}. szék: szín - {lista[i].szin} ; lábszám - {lista[i].labszam}")


# Összegzés tétele
def labak_szama(lista):
    print("Összesen hány db székláb van a teremben?")
    osszesLab = 0
    for i in range(0, len(lista)):
        osszesLab += lista[i].labszam
    print(f"{osszesLab} db van.")
    return osszesLab


# Maximum kiválasztás tétele
def maxLabSzin(lista):
    maxIndex = 0
    for i in range(1, len(lista)):
        if lista[i].labszam > lista[maxIndex].labszam:
            maxIndex = i
    return lista[maxIndex].szin


# Megszámlálás tétele
def labakszama(lista):
    print("Hány 4-nél több lábú szék van: ", end="")
    tobb4db = 0
    for i in range(0, len(lista)):
        if lista[i].labszam > 4:
            tobb4db += 1
    return tobb4db


# Eldöntés tétele
def vanpiros4labu_2(lista):
    print("Van-e piros 4 lábú szék: ", end="")
    vanP4lab = False
    kiir = "Nincs."
    for i in range(0, len(lista)):
        if lista[i].labszam == 4 and lista[i].szin == "Piros":
            vanP4lab = True
    if vanP4lab:
        kiir = "Van."
    return kiir

