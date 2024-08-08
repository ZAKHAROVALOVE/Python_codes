#A function that returns one member at a time of a numeric sequence,
# the law of which is specified using a user function.
#The parameter of the generator function should be the value of the first term of the progression
# and the number of terms given to the sequence (n).
#The generator must stop its work upon reaching the nth term.
#10.1
def some_gen(begin, end, func):
    """
    begin: the first element of the sequence
    end: the number of elements in the sequence
    func: a function that generates a value for a sequence
    """
    current = begin
    count = 0
    while count < end:
        yield current
        current = func(current)
        count += 1

from inspect import isgenerator

def pow(x):
    return x ** 2

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')