def run():
    print("\n--- Option 12: Zahlen-Dreieck ---")
    print("Hier wird ein Zahlen-Dreieck erstellt.")
    
    try:
        n = int(input("Wie viele Zeilen soll das Zahlen-Dreieck haben? "))
    except ValueError:
        print("Ungültige Eingabe. Bitte eine ganze Zahl eingeben.")
        return

    zahl = 1

    for zeile in range(1, n + 1):
        for _ in range(zeile):
            print(zahl, end=' ')
            zahl += 1
        print()

