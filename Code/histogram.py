from collections import Counter
import statistics

# A histogram() function which takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) 
# A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram. 
# For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.
# A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text. 
# For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.

def histogram (source_text):
    with open(source_text, 'r') as file:
        return file.read().split()

def unique_words (histogram):
    return len(set(histogram))
    print (unique_words)

def frequency (word, histogram):
    return histogram.count(word)
    print (frequency)
    
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
print(f"Unique words: {unique_words(text)}")
print(f"Most common word: {most_common(text)}")
print(f"Least common word: {least_common(text)}")
mean, median, mode = frequency_analysis(text)
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
