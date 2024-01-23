from Szek import Szek


def beolvas():
    fajlbol = open("szekek.txt", "r", encoding="utf-8")
    fajlbol.readline()
    szekPeldanyok = fajlbol.readlines()
    fajlbol.close()
    return szekPeldanyok


def tisztitott():
    sorok = beolvas()
    szekLista = []
    for i in range(0, len(sorok)):
        szekLista.append(sorok[i].strip().split(";"))
    return szekLista


szekekListaja = tisztitott()


def listaKiir(lista):
    for i in range(0, len(szekekListaja)):
        print(szekekListaja[i])


listaKiir(szekekListaja)

