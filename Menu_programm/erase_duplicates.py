def run():
    print("--- Option 15: Duplikate aus einer Liste entfernen ---")
    print("gib eine Liste von Zahlen ein, getrennt durch Kommas.")
    print("Die Liste wird ohne Duplikate ausgegeben.")
    eingabe = input("Gib eine Liste von Zahlen ein (z. B. 1,2,2,3,4,3,5): ")

    try:
        # Eingabe in Liste umwandeln
        original_liste = [int(x.strip()) for x in eingabe.split(",")]
        neue_liste = []

        for element in original_liste:
            if element not in neue_liste:
                neue_liste.append(element)

        print("Original-Liste:", original_liste)
        print("Ohne Duplikate:", neue_liste)

    except ValueError:
        print("❌ Ungültige Eingabe! Bitte nur Zahlen getrennt durch Kommas eingeben.")