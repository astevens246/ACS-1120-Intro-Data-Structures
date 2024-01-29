import random
import histogram

# Your first task is to write a function that takes a histogram (however you’ve structured yours) and returns a single word, at random.
 
# It should not yet take into account the distributions of the words.
# def random_word(word_list):
#     return random.choice(word_list)

# text = histogram.histogram('great-gatsby.txt')
# word = random_word(text)
# print(word)
# frequency weighting
# Create a list where each word appears as many times as its frequency

def create_histogram(word_list):
    histogram_dict = {}
    for word in word_list:
        histogram_dict[word] = histogram_dict.get(word, 0) + 1
    return histogram_dict

def random_word(histogram):
    """
    Selects a random word from the given histogram based on the word frequencies.

    Args:
        histogram (dict): A dictionary representing the word frequencies, where the keys are words and the values are their frequencies.

    Returns:
        str: A randomly selected word from the histogram.
    """
    frequency_list = []
    for word, frequency in histogram.items():
        frequency_list.extend([word] * frequency)
    return random.choice(frequency_list)

word_list = histogram.histogram('great-gatsby.txt')
histogram = create_histogram(word_list)
word = random_word(histogram)

word_without_punctuation = word.strip('.,;:?!-'"")
print(word_without_punctuation)