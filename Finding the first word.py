#A function that finds the first word in a given string.
#There may be periods and/or commas in the line
#A string can start with a letter or, for example, a space or a period
#A word can have an apostrophe and it is part of the word
#The entire text can be represented by just one word and that's it
#Input parameters: String.
#Output parameters: String.
#10.2
def first_word(text: str) -> str:
    """
    Search for the first word in the given string.

    Input parameters:
    text: The string in which you want to find the first word.

    Output parameters:
    String: The first word from the transmitted text.
    """
    text = text.strip("., ")

    word = []
    for char in text:
        if char.isalnum() or char == "'":
            word.append(char)
        else:
            break
    return ''.join(word)


if __name__ == "__main__":
    assert first_word("Hello world") == "Hello", 'Test1'
    assert first_word("greetings, friends") == "greetings", 'Test2'
    assert first_word("don't touch it") == "don't", 'Test3'
    assert first_word(".., and so on ...") == "and", 'Test4'
    assert first_word("hi") == "hi", 'Test5'
    assert first_word("Hello.World") == "Hello", 'Test6'
    print('OK')