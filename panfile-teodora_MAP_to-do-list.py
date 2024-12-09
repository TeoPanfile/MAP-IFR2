def meniu():
    print("\nMeniu:")
    print("1. Adauga sarcina")
    print("2. Afiseaza sarcini")
    print("3. Sterge sarcina")
    print("4. Iesire")

def to_do_list():
    sarcini = []

    while True:
        meniu()
        optiune = input("Selecteaza o optiune: ")

        if optiune == "1":
            sarcina = input("Introdu sarcina: ")
            sarcini.append(sarcina)
            print("Sarcina adaugata!")
        elif optiune == "2":
            if sarcini:
                print("\nLista de sarcini:")
                for i, s in enumerate(sarcini, start=1):
                    print(f"{i}. {s}")
            else:
                print("Nu exista sarcini in lista.")
        elif optiune == "3":
            if sarcini:
                numar = int(input("Introdu numarul sarcinii de sters: "))
                if 0 < numar <= len(sarcini):
                    sarcini.pop(numar - 1)
                    print("Sarcina stearsa!")
                else:
                    print("Numar invalid.")
            else:
                print("Nu exista sarcini de sters.")
        elif optiune == "4":
            print("La revedere!")
            break
        else:
            print("Optiune invalida. Incearca din nou.")

to_do_list()