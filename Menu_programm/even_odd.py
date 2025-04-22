def run():

    print("Hier kannst du überprüfen, ob eine Zahl gerade oder ungerade ist.")
    try:
        zahl = int(input("Bitte gib eine ganze Zahl ein: "))
        
        if zahl % 2 == 0:
            print(f"{zahl} ist eine gerade Zahl.")
        else:
            print(f"{zahl} ist eine ungerade Zahl.")

    except ValueError:
        print("Ungültige Eingabe! Bitte gib eine ganze Zahl ein.")
