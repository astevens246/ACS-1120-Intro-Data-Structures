import random
import sys
# read in the words file
with open('/usr/share/dict/words', 'r') as file:
    words = file.read().split()

# select a random set of words from the file and store in a data type
# Check if the command-line argument is provided
if len(sys.argv) > 1: # sys.argv is a list of command-line arguments
    num_words = int(sys.argv[1]) # Convert the argument to an integer
else:
    num_words = 5  # Default number of words

random_words = random.sample(words, num_words)
# put the number of words requested together into a “sentence”
random_sentence = ' '.join(random_words)
# output your sentence
print(random_sentence)