import random
import histogram

# Your first task is to write a function that takes a histogram (however you’ve structured yours) and returns a single word, at random.
 
# It should not yet take into account the distributions of the words.
def random_word(histogram):
    return random.choice(histogram)

hist = histogram.histogram('great-gatsby.txt')
word = random_word(hist)
print(word)
