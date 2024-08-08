#A program that returns all characters between them inclusively.
#"a-c" -> abc
#"a-a" -> a
#"s-H" -> stuvwxyzABCDEFGH
#"a-A" -> abcdefghijklmnopqrstuvwxyzA
#6.1
import string
def find_letters_between(dash_letters):
    start_index = min(string.ascii_letters.index(dash_letters[0]), string.ascii_letters.index(dash_letters[-1]))
    end_index = max(string.ascii_letters.index(dash_letters[0]), string.ascii_letters.index(dash_letters[-1]))
    return string.ascii_letters[start_index:end_index + 1]
dash_letters = input("Enter two letters separated by a hyphen: ")
print(find_letters_between(dash_letters))