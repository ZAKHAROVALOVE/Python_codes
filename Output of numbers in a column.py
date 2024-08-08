#The program asks the user to enter a 4-digit number from the keyboard,
#after which it prints on the screen the column of numbers that this number consists of.
#2.1
user_input = input("Enter a 4-digit number: ")
number = int(user_input)
print(number % 10000 // 1000)
print(number % 1000 // 100)
print(number % 100 // 10)
print(number % 10 // 1)