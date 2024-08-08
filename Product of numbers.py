#A program that multiplies all digits entered by the user of an integer until it is less than or equal to 9.
#6.3
def multiply_digits(number):
    result = 1
    for digit in str(number):
        result *= int(digit)
    return result
user_input = int(input("Enter a number: "))
while user_input > 9:
    user_input = multiply_digits(user_input)
print("Result:", user_input)