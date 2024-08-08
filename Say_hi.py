#The say_hi function, which will introduce a person according to the parameters passed.
#Input data: Two arguments a string (str) and a positive number (int)
#The function should return a string.
#7.1
def say_hi(name: str, age: int) -> str:
    """
    Generate a greeting message with the provided name and age.

    Args:
        name (str): The name of the person.
        age (int): The age of the person.

    Returns:
        str: A greeting message containing the name and age of the person.
    """
    return "Hi. My name is {} and I'm {} years old".format(name, age)


if __name__ == "__main__":
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
    print('ОК')