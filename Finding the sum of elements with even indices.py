#Finding the sum of elements with even indices [0, 2, 4, etc.],
#multiplying this sum by the last element of the input array.
#4.2
def multiply_sum_even_indices_last_element(arr):
    return sum(arr[::2]) * arr[-1] if arr else 0
print(multiply_sum_even_indices_last_element([0, 1, 7, 2, 4, 8]))
print(multiply_sum_even_indices_last_element([1, 3, 5]))
print(multiply_sum_even_indices_last_element([6]))
print(multiply_sum_even_indices_last_element([]))