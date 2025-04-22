def run():
    print("Willkommen zur Ziffernsumme bis einstellig!")
    
    try:
        zahl = int(input("Gib eine ganze Zahl ein: "))
        
        if zahl < 0:
            print("Bitte eine positive ganze Zahl eingeben.")
            return

        original = zahl  # Zur Anzeige am Ende

        while zahl >= 10:
            zahl = sum(int(ziffer) for ziffer in str(zahl))
            print(f"{zahl}")
        print(f"Die Ziffernsumme von {original} bis zur einstelligen Zahl ist: {zahl}")

    except ValueError:
        print("Ungültige Eingabe! Bitte nur ganze Zahlen eingeben.")



run()


