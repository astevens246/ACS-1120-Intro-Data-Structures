# module for generating a sentence from a histogram

import random
import histogram

def create_histogram(word_list):
    # Creates a histogram of word frequencies in a given list of words. 
    # Returns a dictionary where the keys are words and the values are the frequencies of those words.
   
    histogram_dict = {}
    for word in word_list:
        histogram_dict[word] = histogram_dict.get(word, 0) + 1
    return histogram_dict

def random_word(histogram):
        
        # Selects a random word from the given histogram based on the word frequencies.
        # Returns: A randomly selected word from the histogram.
    
        frequency_list = []
        for word, frequency in histogram.items():
            frequency_list.extend([word] * frequency)
        return random.choice(frequency_list)
    
def generate_sentence(histogram, num_words):
    words = [random_word(histogram) for _ in range(num_words)]
    sentence = ' '.join(words)
    return sentence

if __name__ == "__main__":
    word_list = histogram.histogram('great-gatsby.txt')
    histogram_data = create_histogram(word_list)
    sentence = generate_sentence(histogram_data, 10)
    # print(sentence)
    # print(' '.join(sentence))
    print(''.join(sentence).strip('.,;:?!-\'"'))
