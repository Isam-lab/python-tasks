import random

def run():
    print("\n--- Option 6: Zahlenratespiel ---")
    
    geheimzahl = random.randint(1, 10)
    versuche = 0

    while True:
        try:
            tipp = int(input("Rate eine Zahl zwischen 1 und 10: "))
            versuche += 1

            if tipp < 1 or tipp > 10:
                print("Nur Zahlen zwischen 1 und 10 bitte!")
            elif tipp < geheimzahl:
                print("Zu niedrig!")
            elif tipp > geheimzahl:
                print("Zu hoch!")
            else:
                print(f"Richtig! Die Zahl war {geheimzahl}. Du hast {versuche} Versuche gebraucht.")
                break
        except ValueError:
            print("Bitte gib eine gültige ganze Zahl ein.")

