def ist_primzahl(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def run():
    print("\n--- Option 13: Primzahlen zwischen bis zu einem bestimmten Zahl ---")
    print("Gib eine positive ganze Zahl ein, um alle Primzahlen bis zu dieser Zahl anzuzeigen.")
    print("Die Eingabe muss größer oder gleich 2 sein.")
    try:
        eingabe = input("Gib eine ganze Zahl ein, bis zu der Primzahlen angezeigt werden sollen: ")
        grenze = int(eingabe)

        if grenze < 2:
            print("Bitte eine Zahl größer oder gleich 2 eingeben.")
            return

        print(f"Primzahlen von 2 bis {grenze}:")
        for zahl in range(2, grenze + 1):
            if ist_primzahl(zahl):
                print(zahl)

    except ValueError:
        print("❌ Ungültige Eingabe! Bitte gib eine ganze Zahl ein.")
