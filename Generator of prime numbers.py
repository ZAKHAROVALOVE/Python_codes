#A function that returns prime numbers.
#11.1
from typing import Generator


def prime_generator(end: int) -> Generator[int, None, None]:
    """
    Generation of prime numbers up to and including the given end.
    """
    assert end >= 2, "End must be 2 or greater"

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in range(2, end + 1):
        if is_prime(num):
            yield num


if __name__ == "__main__":
    from inspect import isgenerator

    gen = prime_generator(1)
    assert isgenerator(gen) == True, 'Test0'
    assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
    assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
    assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
    print('Ok')