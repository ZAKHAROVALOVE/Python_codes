#Calculator
#5.2
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Error: division by zero!")
            result = num1 / num2
        else:
            print("Incorrect operation!")
            continue

        print("Result:", result)

    except ValueError:
        print("Please enter the numbers.")
    except ZeroDivisionError as error:
        print(error)

    choice = input("Do you want to continue working? (y/n): ")
    if choice.lower() != 'y':
        break