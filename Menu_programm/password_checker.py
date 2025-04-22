def run():
    print("\n--- Option 9: Passwort-Checker ---")

    pw = input("Bitte gib ein Passwort ein: ")

    
    lang_genug = len(pw) >= 8
    hat_zahl = any(char.isdigit() for char in pw)

    if lang_genug and hat_zahl:
        print("✅ Starkes Passwort!")
    else:
        print("❌ Schwaches Passwort.")
        if not lang_genug:
            print("- Es muss mindestens 8 Zeichen lang sein.")
        if not hat_zahl:
            print("- Es muss mindestens eine Zahl enthalten.")

