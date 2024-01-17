class Szek:
    def __init__(self, sor: str):
        darabolt = sor.strip().split()
        self.szin = darabolt[0]
        self.labszam = darabolt[1]

    def __str__(self):
        print(f"Szín: {self.szin}\nLábszám: {self.labszam}")

    