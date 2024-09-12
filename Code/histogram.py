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
    def __init__(self, source_text):
        with open(source_text, 'r') as file:
            self.words = file.read().split()

    def unique_words(self):
        return len(set(self.words))

    def frequency(self, word):
        return self.words.count(word)
        
    def most_common(self):
        return Counter(self.words).most_common(1)
        
    def least_common(self):
        counter = Counter(self.words)
        return counter.most_common()[-1]

    def different_words(self):
        return len(self.words)

    def frequency_analysis(self):
        counter = Counter(self.words)
        frequencies = list(counter.values())

        mean = statistics.mean(frequencies)
        median = statistics.median(frequencies)
        mode = statistics.mode(frequencies)

        return mean, median, mode

histogram = Histogram('great-gatsby.txt')
print(f"Unique words: {histogram.unique_words()}")
print(f"Most common word: {histogram.most_common()}")
print(f"Least common word: {histogram.least_common()}")
mean, median, mode = histogram.frequency_analysis()
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")

# # Generate a list of random words
# def generate_words(n):
#     words = []
#     for _ in range(n):
#         word = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))  # Generate a random 5-letter word
#         words.append(word)
#     return words

# # Benchmark the count operation
# def benchmark(n):
#     words = generate_words(n)
#     histogram = Histogram(words)  # Create a histogram with the words

#     start_time = time.time()
#     histogram.frequency(random.choice(words))  # Count a random word
#     end_time = time.time()

#     print(f'Count operation took {end_time - start_time} seconds for {n} unique word types')

# # Benchmark with small and large histogram sizes
# benchmark(100)
# benchmark(10000)


