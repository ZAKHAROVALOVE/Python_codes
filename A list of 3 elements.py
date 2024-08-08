#Creating a new list with 3 elements:
#the first, the third from the beginning and the second from the end of the random list of numbers
#4.3
import random

random_count = random.randint(3, 10)
random_list = [random.randint(1, 10) for _ in range(random_count)]
print("A random list of numbers from 3 to 10:", random_list)

new_list = [random_list[0], random_list[2], random_list[-2]]
print("New list:", new_list)
