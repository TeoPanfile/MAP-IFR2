def celsius_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_celsius(f):
    return (f - 32) * 5/9

def metri_kilometri(m):
    return m / 1000

def kilometri_metri(k):
    return k * 1000

def kilograme_livre(kg):
    return kg * 2.20462

def livre_kilograme(l):
    return l / 2.20462

def conversie_unitati():
    while True:
        print("\nMeniu Conversie:")
        print("1. Celsius -> Fahrenheit")
        print("2. Fahrenheit -> Celsius")
        print("3. Metri -> Kilometri")
        print("4. Kilometri -> Metri")
        print("5. Kilograme -> Livre")
        print("6. Livre -> Kilograme")
        print("7. Iesire")

        optiune = input("Alege o optiune: ")

        if optiune == "1":
            c = float(input("Introdu temperatura in Celsius: "))
            print(f"{c} °C = {celsius_fahrenheit(c)} °F")
        elif optiune == "2":
            f = float(input("Introdu temperatura in Fahrenheit: "))
            print(f"{f} °F = {fahrenheit_celsius(f)} °C")
        elif optiune == "3":
            m = float(input("Introdu distanta in metri: "))
            print(f"{m} metri = {metri_kilometri(m)} kilometri")
        elif optiune == "4":
            k = float(input("Introdu distanta in kilometri: "))
            print(f"{k} kilometri = {kilometri_metri(k)} metri")
        elif optiune == "5":
            kg = float(input("Introdu greutatea in kilograme: "))
            print(f"{kg} kilograme = {kilograme_livre(kg)} livre")
        elif optiune == "6":
            l = float(input("Introdu greutatea in livre: "))
            print(f"{l} livre = {livre_kilograme(l)} kilograme")
        elif optiune == "7":
            print("La revedere!")
            break
        else:
            print("Optiune invalida.")

conversie_unitati()