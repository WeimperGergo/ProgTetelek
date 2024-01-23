def szek_init(szin: str, labszam: int):
    print(f"Szín: {szin} Lábszám: {labszam}")


def szek_str(szin: str, labszam: int):
    return f"Szín: {szin} Lábszám: {labszam}"


szek_init("Kék", 3)
szek_init("Lila", 4)
szek_init("Zöld", 5)

print(szek_str("Kék", 4))
