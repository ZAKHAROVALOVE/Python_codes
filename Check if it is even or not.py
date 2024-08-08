#The function returns True if the number is even, and False if the number is odd.
#Input: Integer.
#Output data: Boolean type.
#10.3
def is_even(digit: int) -> bool:
    """ Checking if a number is even. """
    return digit % 2 == 0


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

if __name__ == "__main__":
    print(is_even(2))
    print(is_even(5))
    print(is_even(0))