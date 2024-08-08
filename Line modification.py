#One sentence is passed to the input of the correct_sentence function. The string is not empty.
#The corrected copy must be returned so that it always begins with a capital letter and ends with a period.
#If the sentence already ends with a period, you do not need to add another period, it will be an error
#Input arguments: string.
#Output arguments: string.
#7.2
def correct_sentence(text: str) -> str:
    """
    Corrects the text by capitalizing the first letter of the sentence and adding a period at the end if it's missing.

    :param text: The input text to be corrected.
    :type text: str
    :return: The corrected text.
    :rtype: str
    """

    corrected_text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        corrected_text += '.'
    return corrected_text


if __name__ == "__main__":
    assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
    assert correct_sentence("hello") == "Hello.", 'Test2'
    assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
    assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
    assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
    print('OK')