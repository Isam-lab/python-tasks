def run():
    print("Willkommen beim einfachen Taschenrechner!")

    try:
        zahl1 = float(input("Gib die erste Zahl ein: "))
        zahl2 = float(input("Gib die zweite Zahl ein: "))

        print(f"\nErgebnisse mit {zahl1} und {zahl2}:")
        print(f"Addition: {zahl1 + zahl2}")
        print(f"Subtraktion: {zahl1 - zahl2}")
        print(f"Multiplikation: {zahl1 * zahl2}")
        
        if zahl2 != 0:
            print(f"Division: {zahl1 / zahl2}")
        else:
            print("Division: Fehler – Division durch 0 ist nicht erlaubt!")

    except ValueError:
        print("Ungültige Eingabe! Bitte nur Zahlen eingeben.")



