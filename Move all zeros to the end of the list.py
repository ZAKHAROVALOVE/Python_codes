#A program that moves all zeros to the end of a list.
#4.1
input_list = [0, 1, 0, 12, 3]
input_list.sort(key=lambda x: (x == 0, x))
print(input_list)
