from collections import Counter
import statistics

# Update the histogram with the frequency count of each
# word in a given list of words (like the update method on the Dictogram and Listogram classes).
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
# print(f"Unique words: {unique_words(text)}")
# print(f"Most common word: {most_common(text)}")
# print(f"Least common word: {least_common(text)}")
# mean, median, mode = frequency_analysis(text)
# print(f"Mean: {mean}, Median: {median}, Mode: {mode}")

# frequency('and', text)
# print(frequency('and', text))


