#Finds the index of the second occurrence of the searched string in the search string.
#The second_index function accepts 2 lines as parameters.
#The string to be found can consist of several characters.
#Input: Two lines (String).
#Output: Int or None
#7.3
def second_index(text: str, some_str: str) -> int or None:
    """
    Finds the second index of substring `some_str` in the text `text`.

    :param text: The input text.
    :type text: str
    :param some_str: The substring to find.
    :type some_str: str
    :return: The second index of the substring or None if the substring is not found or occurs only once.
    :rtype: int or None
    """

    first_index = text.find(some_str)
    if first_index == -1:
        return None

    second_index = text.find(some_str, first_index + 1)
    if second_index == -1:
        return None

    return second_index


if __name__ == "__main__":
    assert second_index("sims", "s") == 3, 'Test1'
    assert second_index("find the river", "e") == 12, 'Test2'
    assert second_index("hi", "h") is None, 'Test3'
    assert second_index("Hello, hello", "lo") == 10, 'Test4'
    print('OK')