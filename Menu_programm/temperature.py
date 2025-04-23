def run():
    print("\n--- Option 5: Temperaturumrechner ---")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius") 
    choice = input("Bitte wähle (1 oder 2): ").strip()
    try:
        match choice:
            case "1":
                celsius = float(input("Temperatur in °C: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius}°C sind {fahrenheit:.2f}°F")
            case "2":
                fahrenheit = float(input("Temperatur in °F: "))
                celsius = (fahrenheit - 32) * 5/9
                print(f"{fahrenheit}°F sind {celsius:.2f}°C")
            case _:
                print("❌ Ungültige Auswahl. Bitte 1 oder 2 eingeben.")
    except ValueError:
        print("❌ Ungültige Eingabe! Bitte eine Zahl eingeben.")




