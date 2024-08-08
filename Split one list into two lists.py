#The program splits one list into two and puts them into a new list.
#3.3
def divide_list(input_list):
    lst2 = []
    if len(input_list) % 2 == 0:
        index = len(input_list) // 2
        lst2.append(input_list[:index])
        lst2.append(input_list[index:])
    else:
        index = len(input_list) // 2 + 1
        lst2.append(input_list[:index])
        lst2.append(input_list[index:])
    return lst2

print(divide_list([1, 2, 3, 4, 5, 6]))
print(divide_list([1, 2, 3]))
print(divide_list([1]))
print(divide_list([]))
