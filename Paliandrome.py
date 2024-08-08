#A function that will check if a string is a palindrome.
#A palindrome is a string that is read equally from the left
#to the right and from right to left without taking into account punctuation marks and the size of letters.
#The function takes a string as input and returns a Boolean value of True or False
#8.2
def is_palindrome(text: str) -> bool:
    """
    Check if a given text is a palindrome.

    Args:
        text: The text to be checked.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    reversed_text = cleaned_text[::-1]
    return cleaned_text == reversed_text


if __name__ == "__main__":
    assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
    assert is_palindrome('0P') == False, 'Test2'
    assert is_palindrome('a.') == True, 'Test3'
    assert is_palindrome('aurora') == False, 'Test4'
    print("ОК")