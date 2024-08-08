#Two arguments are passed to the input of the popular_words function.
# Text and list of words whose popularity needs to be determined.
#Words must be searched in all registers. That is, if you need to find the word "one",
# then the words "one", "One", "oNe", "ONE", etc. will be suitable for it.
#Searched words are always in lower case
#If the word is not found even once, it must be returned in the dictionary with a value of 0 (zero)
#Input parameters: Text and an array of words to be searched for.
#Output parameters: A dictionary in which the keys are the searched words
#and the values ​​are the number of times each word occurs in the original text.
#9.1
def popular_words(text: str, words: list) -> dict:
    """
    Counts the occurrence of each word from the list of words in the given text.

    :param text: text to search for.
    :param words: a list of words whose popularity needs to be determined.
    :return: a dictionary where keys are words from a list and values ​​are the number of occurrences of each word in the text.
    """
    word_list = text.lower().split()
    word_count = {word: 0 for word in words}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1

    return word_count


if __name__ == "__main__":
    assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                         ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
    print('OK')