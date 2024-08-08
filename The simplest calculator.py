#The program performs simple mathematical operations (+, -, *, /).
#The user is asked alternately to enter numbers and an action on these numbers,
#and the program, based on the action, calculates and prints the result.
#3.1
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
        exit()

    print("Result:", result)

except ValueError:
    print("Please enter the numbers.")
except ZeroDivisionError as error:
    print(error)