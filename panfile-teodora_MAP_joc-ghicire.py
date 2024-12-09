import random

def joc_ghicire():
    numar_secret = random.randint(1, 100)
    incercari = 0
    ghicit = False

    print("Ghiceste numarul intre 1 si 100!")

    while not ghicit:
        incercare = int(input("Introdu un numar: "))
        incercari += 1

        if incercare == numar_secret:
            print(f"Felicitari! Ai ghicit numarul in {incercari} incercari!")
            ghicit = True
        elif incercare < numar_secret:
            print("Prea mic!")
        else:
            print("Prea mare!")

joc_ghicire()