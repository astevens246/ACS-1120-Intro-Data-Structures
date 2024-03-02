import time
import random
import string
from collections import Counter
import statistics

# Update the histogram with the frequency count of each
# word in a given list of words (like the update method on the Dictogram and Listogram classes).
def read_file(source_text):
    with open(source_text, 'r') as file:
        words = file.read().split()
    return words
class Histogram:
    def __init__(self, words):
        self.words = words
    
    def histogram (source_text):
        with open(source_text, 'r') as file:
            return file.read().split()

    def unique_words (histogram):
        return len(set(histogram))
        print (unique_words)

    def frequency (self, word):
        return self.words.count(word)
        
    def most_common (histogram):
        return Counter(histogram).most_common(1)
        print (most_common)
        
    def least_common (histogram):
        counter = Counter(histogram)
        return counter.most_common()[-1]

    def different_words (histogram):
        return len(histogram)
        print (different_words)
        

    def frequency_analysis(histogram):
        counter = Counter(histogram)
        frequencies = list(counter.values())

        mean = statistics.mean(frequencies)
        median = statistics.median(frequencies)
        mode = statistics.mode(frequencies)

        return mean, median, mode

    text = histogram('great-gatsby.txt')
    # print(f"Unique words: {unique_words(text)}")
    # print(f"Most common word: {most_common(text)}")
    # print(f"Least common word: {least_common(text)}")
    # mean, median, mode = frequency_analysis(text)
    # print(f"Mean: {mean}, Median: {median}, Mode: {mode}")

    # frequency('and', text)
    # print(frequency('and', text))


# Generate a list of random words
def generate_words(n):
    words = []
    for _ in range(n):
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))  # Generate a random 5-letter word
        words.append(word)
    return words

# Benchmark the count operation
def benchmark(n):
    words = generate_words(n)
    histogram = Histogram(words)  # Create a histogram with the words

    start_time = time.time()
    histogram.frequency(random.choice(words))  # Count a random word
    end_time = time.time()

    print(f'Count operation took {end_time - start_time} seconds for {n} unique word types')

# Benchmark with small and large histogram sizes
benchmark(100)
benchmark(10000)


