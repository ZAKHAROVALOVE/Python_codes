#It is necessary to get a number from the set of numbers included in the list, add it to 1
#and the received amount, again split it into a list of numbers.
#As a result, the function returns a list of numbers that make up the sum value.
#So from the list with numbers [1, 2, 3, 4], the number 1234 should come out.
#We add 1 to it, and we get 1235.
#After that, you need to divide the received number into its constituent digits.
#The result should be the list [1, 2, 3, 5] returned by the function.
#8.1
def add_one(some_list: list) -> list:
    """
    Increment the number represented by a list of digits by one.

    Args:
        some_list: A list of integers representing digits of a number.

    Returns:
        A list of integers representing digits of the incremented number.
    """
    num = int(''.join(map(str, some_list))) + 1
    result_list = [int(digit) for digit in str(num)]
    return result_list


if __name__ == "__main__":
    assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
    assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
    assert add_one([0]) == [1], 'Test3'
    assert add_one([9]) == [1, 0], 'Test4'
    print("ОК")