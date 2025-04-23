def show_menu():
    print("\n--- Python Übungsmenü ---")
    print("1. Hallo, Welt!")
    print("2. Eingabe von Name und Alter")
    print("3. Einfacher Taschenrechner")
    print("4. Gerade oder ungerade Zahl")
    print("5. Temperaturumrechner")
    print("6. Zahlenratespiel")
    print("7. Liste und Schleifen")
    print("8. Wortzähler")
    print("9. Passwort-Checker")
    print("10. FizzBuzz")
    print("11. Ziffersumme bis einstellig")
    print("12. Zahlen-Dreieck")
    print("13. primzahlen bis zu einer bestimmten Zahl")
    print("14. Zeichenkette umkehren")
    print("Gib 'exit' ein, um das Programm zu beenden.")
    print("Gib 'm' ein, um das Menü erneut anzuzeigen.")
    print("-------------------------")

# Menü einmal zu Beginn zeigen
show_menu()

while True:
    choice = input("\nBitte wähle eine Option (1-14, 'm' für Menü, 'exit' zum Beenden): ").strip().lower()

    match choice:
        case "m":
            show_menu()
        case "1":
            import Hello_world
            Hello_world.run()
        case "2":
            import name_age
            name_age.run()
        case "3":
            import calculator
            calculator.run()
        case "4":
            import even_odd
            even_odd.run()
        case "5":
            import temperature
            temperature.run()
        case "6":
            import guess_number
            guess_number.run()
        case "7":
            import list_stats
            list_stats.run()
        case "8":
            import word_counter
            word_counter.run()
        case "9":
            import password_checker
            password_checker.run()
        case "10":
            import fizzbuzz
            fizzbuzz.run()
        case "11":
            import ziffersumme_bis_einstellig
            ziffersumme_bis_einstellig.run()
        case "12":
            import Zahlen_Dreieck
            Zahlen_Dreieck.run()
        case "13":
            import Primzahlen
            Primzahlen.run()
        case "14":
            import zeichenkette_umkehr
            zeichenkette_umkehr.run()
        case "exit":
            print("Programm ist beendet.")
            break
        case _:
            print("❌ Ungültige Eingabe. Bitte gib eine Zahl von 1 bis 14 ein, 'm' für das Menü oder 'exit' zum Beenden.")


















    
    
    
    
    
