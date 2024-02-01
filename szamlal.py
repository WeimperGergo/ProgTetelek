def beker():
    szam = int(input("N = "))
    return szam


def legyen0():
    VEGE = 0
    db = 0
    minimum = 2147483647
    szam = minimum
    while szam := beker() and szam != VEGE:
        if szam > minimum:
            minimum = szam
        db += 1
    print(db+1, "alkalommal kért be számot amíg 0 nem lett.")


legyen0()
