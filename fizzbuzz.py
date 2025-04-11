# fizzbuzz.py

def run():
    """
    Fragt eine Zahl ab und führt FizzBuzz bis zu dieser Zahl aus.
    """
    print("\n--- Option 10: FizzBuzz ---")

    try:
        grenze = int(input("Bis zu welcher Zahl möchtest du FizzBuzz ausgeben? "))

        if grenze < 1:
            print("Bitte gib eine Zahl größer als 0 ein.")
            return

        for i in range(1, grenze + 1):
            if i % 3 == 0 and i % 5 == 0:
                print(f"{i}  Fizzbuzz")
            elif i % 3 == 0:
                print(f"{i}  Fizz")
            elif i % 5 == 0:
                print(f"{i}  Buzz")
            else:
                print(i)
    except ValueError:
        print("Ungültige Eingabe! Bitte gib eine ganze Zahl ein.")


