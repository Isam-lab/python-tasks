
import Hello_world
import name_age
import calculator
import even_odd
import temperature
import guess_number
import list_stats
import word_counter
import password_checker
import fizzbuzz

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
    print("für das Beenden des Programms 'exit' eingeben")
    print("-------------------------")

while True:
    show_menu()
    choice = input("Bitte wähle eine Option: ")
    
    if choice == "exit":
        print("Programm ist beendet.")
        break
    elif choice == "1":
        Hello_world.run()
    elif choice == "2":
        name_age.run()
    elif choice == "3":
        calculator.run()
    elif choice == "4":
        even_odd.run()
    elif choice == "5":
        temperature.run()
    elif choice == "6":
        guess_number.run()
    elif choice == "7":
        list_stats.run()
    elif choice == "8":
        word_counter.run()
    elif choice == "9":
        password_checker.run()
    elif choice == "10":
        fizzbuzz.run()
    else:
        print("Ungültige Eingabe. Bitte wähle eine Zahl von 0 bis 10.")
