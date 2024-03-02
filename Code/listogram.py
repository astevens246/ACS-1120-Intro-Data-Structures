#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import random
import time
import string



class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.listogram = []  # List of distinct word types in this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)
    
    def __len__(self):
        """Return the number of entries in the listogram."""
        return len(self.listogram)

    def add_count(self, word, count=1):
        """Increase the frequency count of a word."""
        for item in self.listogram:
            if item[0] == word:
                item[1] += count
                self.tokens += count
                return
        self.listogram.append([word, count])
        self.types += 1
        self.tokens += count


    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        for item in self.listogram:
            if item[0] == word:
                return item[1]
        return 0
        
    


    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        return any(item[0] == word for item in self.listogram)

    def index_of(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        if target in self:
            for word in self:
                if word[0] == target:
                    index = self.index(word)
            return index 

    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        # Create a list where each word appears as many times as its frequency
        # Choose a random number between 0 and (n-1) where n is the total count of tokens
        random_num = random.randint(0, self.tokens - 1)
        # Iterate over each word-count pair in the listogram
        for word, count in self.listogram:
            # Subtract the count of the current word from the random number
            random_num -= count
            # If the random number is less than 0, return the current word
            if random_num < 0:
                return word

    



    def print_histogram(self):
        print()
        print('Histogram:')
        print('word list: {}'.format(self))
        print('listogram: {}'.format(self.listogram))
        print('{} tokens, {} types'.format(self.tokens, self.types))
        for word in self[-2:]:
            freq = self.frequency(word)
            print('{!r} occurs {} times'.format(word, freq))
        print()
        self.print_histogram_samples()


    def print_histogram_samples(histogram):
        print('Histogram samples:')
        # Sample the histogram 10,000 times and count frequency of results
        samples_list = [histogram.sample() for _ in range(10000)]
        samples_hist = Listogram(samples_list)
        print('samples: {}'.format(samples_hist))
        print()
        print('Sampled frequency and error from observed frequency:')
        header = '| word type | observed freq | sampled freq  |  error  |'
        divider = '-' * len(header)
        print(divider)
        print(header)
        print(divider)
        # Colors for error
        green = '\033[32m'
        yellow = '\033[33m'
        red = '\033[31m'
        reset = '\033[m'
        # Check each word in original histogram
        for word, count in histogram:
            # Calculate word's observed frequency
            observed_freq = count / histogram.tokens
            # Calculate word's sampled frequency
            samples = samples_hist.frequency(word)
            sampled_freq = samples / samples_hist.tokens
            # Calculate error between word's sampled and observed frequency
            error = (sampled_freq - observed_freq) / observed_freq
            color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
            print('| {!r:<9} '.format(word)
                + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
                + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
                + '| {}{:>+7.2%}{} |'.format(color, error, reset))
        print(divider)
        print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        histogram = Listogram(arguments)
        histogram.print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        histogram = Listogram(list(word))
        histogram.print_histogram()  
              
        fish_text = 'one fish two fish red fish blue fish'
        histogram = Listogram(fish_text.split())
        print(histogram.listogram)  # [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]    
        
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        histogram = Listogram(woodchuck_text.split())
        histogram.print_histogram()


if __name__ == '__main__':
    main()


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
    histogram = Listogram(words)

    start_time = time.time()
    histogram.count(random.choice(words))  # Count a random word
    end_time = time.time()

    print(f'Count operation took {end_time - start_time} seconds for {n} unique word types')

# Benchmark with small and large histogram sizes
benchmark(100)
benchmark(10000)