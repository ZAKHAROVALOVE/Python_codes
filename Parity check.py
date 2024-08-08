#The function returns True if the number is even, or False if the number is odd,
#without using division in the function, and the actions associated with it ( /, //, % and divmod).
#The solution does not depend on the size of the number.
#Input: Integer.
#Output: True or False
#11.3
def is_even(number: int) -> bool:
    """
    Checking if a number is even without using division.
    """
    return (number & 1) == 0


if __name__ == "__main__":
    assert is_even(2494563894038**2) == True, 'Test1'
    assert is_even(1056897**2) == False, 'Test2'
    assert is_even(24945638940387**3) == False, 'Test3'
    print('Ok')