#Converting a string to a hashtag.
#5.3
import string
def generate_hashtag(s):
    hashtag = ''.join(word.capitalize() for word in s.split() if word)
    hashtag = ''.join(char for char in hashtag if char not in string.punctuation + ' ')
    hashtag = hashtag[:140]
    if hashtag:
       hashtag = '#' + hashtag
    return hashtag
print(generate_hashtag(input("Enter a string: ")))