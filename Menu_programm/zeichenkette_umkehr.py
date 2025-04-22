def run():
    print("--- Option 15: Zeichenkette umkehren ---")
    text = input("Gib eine Zeichenkette ein, und ich werde sie umkehren.:\n")
    umgekehrt = ""

    for buchstabe in text:
        umgekehrt = buchstabe + umgekehrt

    print("Umgekehrte Zeichenkette:", umgekehrt)
