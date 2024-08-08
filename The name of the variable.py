#Checks if this string can be a variable name.
#A variable cannot: start with a number, contain uppercase letters,
#contain a space, contain punctuation marks, be a registered word
#5.1
import keyword
def is_valid_variable_name(name):
    if name[0].isdigit() or any(char.isupper() for char in name) or ' ' in name \
            or any(char in "!\"#$%&'()*+,./:;<=>?@[\\]^`{|}~" for char in name) \
            or name in keyword.kwlist or (name != '_' and not name.islower()):
        return False
    return True
def print_result(is_valid):
    print("True" if is_valid else "False")
def main():
    name = input("Enter a string: ")
    result = is_valid_variable_name(name)
    print_result(result)

if __name__ == "__main__":
    main()