import random

def random_words(user_input):
    words = user_input.split() #split words
    random.shuffle(words) #shuffle words
    return ' '.join(words) #join words

user_input = input("Enter a phrase: ")
print (random_words(user_input))


