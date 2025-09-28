
# A very simple calculator in Python
# Does addition, subtraction, multiplication and division.

def calculator():
    print("Simple Calculator")
    print("-----------------")

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("That doesn’t look like a number.")
        return

    print("\nWhat do you want to do?")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Pick 1, 2, 3 or 4: ")

    if choice == "1":
        print(f"\nResult: {a} + {b} = {a + b}")
    elif choice == "2":
        print(f"\nResult: {a} - {b} = {a - b}")
    elif choice == "3":
        print(f"\nResult: {a} * {b} = {a * b}")
    elif choice == "4":
        if b == 0:
            print("\nYou can’t divide by zero.")
        else:
            print(f"\nResult: {a} / {b} = {a / b}")
    else:
        print("\nThat wasn’t a valid option.")

# run it once
calculator()
