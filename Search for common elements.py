#The common_elements function, which will generate two lists of elements.
#One list with numbers that are multiples of 3, the other with numbers that are multiples of 5. The number of elements in these lists can be different.
#Using sets, create a set with numbers that are in both sets (intersection).
#The function must return this set as the result of its operation.
#7.4
def common_elements() -> set:
    """
    Finds the common elements between the multiples of 3 and 5 in the range from 0 to 99.

    :return: The set of common elements.
    :rtype: set
    """

    multiples_of_3 = [num for num in range(0, 100) if num % 3 == 0]
    multiples_of_5 = [num for num in range(0, 100) if num % 5 == 0]

    set_multiples_of_3 = set(multiples_of_3)
    set_multiples_of_5 = set(multiples_of_5)

    common_elements_set = set_multiples_of_3.intersection(set_multiples_of_5)

    return common_elements_set


if __name__ == "__main__":
    assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
    print('OK')