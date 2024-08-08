#The find_unique_value function, which accepts a list of numbers, finds
#a unique number among them and return it.
#When there are several unique numbers in the same list, there is no need to check.
#8.3
def find_unique_value(some_list: list) -> list:
    """
    This function takes a list as input and returns the unique value that appears only once in the list.
    """
    count_dict = {}
    for num in some_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for num, count in count_dict.items():
        if count == 1:
            return num

if __name__ == "__main__":
    assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
    assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
    assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
    print("ОК")