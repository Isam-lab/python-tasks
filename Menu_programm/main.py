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

    if choice == "m":
        show_menu()
    elif choice == "1":
        import Hello_world
        Hello_world.run()
    elif choice == "2":
        import name_age
        name_age.run()
    elif choice == "3":
        import calculator
        calculator.run()
    elif choice == "4":
        import even_odd
        even_odd.run()
    elif choice == "5":
        import temperature
        temperature.run()
    elif choice == "6":
        import guess_number
        guess_number.run()
    elif choice == "7":
        import list_stats
        list_stats.run()
    elif choice == "8":
        import word_counter
        word_counter.run()
    elif choice == "9":
        import password_checker
        password_checker.run()
    elif choice == "10":
        import fizzbuzz
        fizzbuzz.run()
    elif choice == "11":
        import ziffersumme_bis_einstellig
        ziffersumme_bis_einstellig.run()
    elif choice == "12":
        import Zahlen_Dreieck
        Zahlen_Dreieck.run()
    elif choice == "13":
        import Primzahlen
        Primzahlen.run()
    elif choice == "14":
        import zeichenkette_umkehr
        zeichenkette_umkehr.run()
    elif choice == "exit":
        print("Programm ist beendet.")
        break
    else:
        print("❌ Ungültige Eingabe. Bitte gib eine Zahl von 1 bis 10 ein, 'm' für das Menü oder 'exit' zum Beenden.")

















    
    
    
    
    
