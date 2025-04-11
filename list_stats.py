def run():
    print("\n--- Option 7: Liste und Schleifen ---")
    
    zahlen = []

    while len(zahlen) < 5:
        try:
            eingabe = float(input(f"Gib Zahl {len(zahlen)+1} von 5 ein: "))
            zahlen.append(eingabe)
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

    summ = sum(zahlen)
    durchschnitt = summ / len(zahlen)
    maximum = max(zahlen)
    minimum = min(zahlen)

    print("\nErgebnisse:")
    print(f"Zahlen: {zahlen}")
    print(f"Summe: {summ}")
    print(f"Durchschnitt: {durchschnitt:.2f}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

