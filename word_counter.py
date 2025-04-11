def run():
    print("\n--- Option 8: Wortzähler ---")
    
    satz = input("Bitte gib einen Satz ein: ")

    
    woerter = satz.split()

    anzahl = len(woerter)

    print(f"Anzahl der Wörter: {anzahl}")

