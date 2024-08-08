#The user enters a 5-digit positive integer.
#You need to "flip" this number backwards, that is,
#so that the result is also a 5-digit number, but with the reverse sequence of digits.
#2.2
x = input("Please input some integer: ")
y = int(x)
print("Result:", (y % 10) * 10000 + (y // 10 % 10) * 1000 + (y // 100 % 10) * 100 + (y // 1000 % 10) * 10 + (y // 10000))