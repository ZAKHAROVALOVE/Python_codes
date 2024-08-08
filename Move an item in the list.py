#The program must move the last element of the list from the end to the beginning,
#that is, the last element of the list must become the first.
#The sequence of other elements should not change.
#3.2
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.insert(0, my_list.pop())
print(my_list)