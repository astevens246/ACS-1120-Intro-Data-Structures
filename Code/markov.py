import random 
import string
from clean_text import clean_text
from tokens import tokenize, remove_punctuation
from clean_text import postprocess_sentence
# Learn a Markov chain from a corpus. 

# You’ve already written code to find how often a token appears in a corpus, 
# but now you need to find how often a token appears after another token.

# Do a random walk on a Markov chain. 
# This should be pretty simple if you pick a good way to store the Markov chain you learn.
    

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            raise Exception("Cannot dequeue from an empty queue")
        return self.items.pop(0)

    def __iter__(self):
        return iter(self.items)
class MarkovChain(dict):
    def __init__(self):
        super().__init__()
    #Empty dictionary to store markov chain 
    # Key == word
    # Value == list of words that follow the key-word

    def make_markov_chain(self, corpus, n):
        markov_chain = {}
        words = ['__START__'] * n + corpus.split() + ['__END__']  # Start with n __START__ tokens
        queue = Queue()
        try:
            for i in range(len(words)):
                if len(queue.items) == n:
                    queue.dequeue()
                queue.enqueue(words[i])
                if len(queue.items) == n:
                    key = tuple(queue.items)
                    if key not in markov_chain:
                        markov_chain[key] = []
                    if i + 1 < len(words):
                        markov_chain[key].append(words[i + 1])
        except Exception as e:
            print(f"Error while making Markov chain: {e}")
        finally:
            return markov_chain  # Always return markov_chain, even if there's an error
    
    def generate_sentence(self, markov_chain, n, n_words=10):
        # Start with a random state
        state = random.choice(list(markov_chain.keys()))
        chain = list(state)
        while len(chain) < n_words and chain[-1] != '__END__':
            state = tuple(chain[-n:])
            if state in markov_chain:
                next_word = random.choice(markov_chain[state])
                chain.append(next_word)
            else:
                break
        return ' '.join(chain)


# Define your corpus
with open("great-gatsby.txt", "r") as file:
    corpus = file.read()
# Clean and tokenize the text
cleaned_corpus = clean_text(corpus)
no_punc_corpus = remove_punctuation(cleaned_corpus)
tokens = tokenize(no_punc_corpus)

# Convert tokens back to string and feed into the Markov chain
corpus = ' '.join(tokens)
markov = MarkovChain()
n = 10 # Set the number of words to look at
n_words = 10
markov_chain = markov.make_markov_chain(corpus, n)

sentence = markov.generate_sentence(markov_chain, n, n_words)

sentence = postprocess_sentence(sentence)
print(sentence)

