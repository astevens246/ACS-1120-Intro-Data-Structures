import random 
import string
import clean_text 
# Learn a Markov chain from a corpus. 

# You’ve already written code to find how often a token appears in a corpus, 
# but now you need to find how often a token appears after another token.

# Do a random walk on a Markov chain. 
# This should be pretty simple if you pick a good way to store the Markov chain you learn.
    
# with open("great-gatsby.txt", "r") as file:
#     corpus = file.read()
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
        words = corpus.split()
        queue = Queue()
        for word in words:
            if len(queue.items) == n:
                queue.dequeue()
            queue.enqueue(word)
            if len(queue.items) == n:
                key = tuple(queue.items)
                if key not in markov_chain:
                    markov_chain[key] = []
                if words.index(word) + 1 < len(words):
                    markov_chain[key].append(words[words.index(word) + 1])
        return markov_chain

    def generate_sentence(self, markov_chain, n, n_words=10):
        first_word = random.choice(list(markov_chain.keys()))
        chain = list(first_word)
        for i in range(n_words):
            if tuple(chain[-n:]) in markov_chain:
                next_word = random.choice(markov_chain[tuple(chain[-n:])])
                chain.append(next_word)
            else:
                break
        return ' '.join(chain)

corpus = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!"
markov = MarkovChain()
n = 6
markov_chain = markov.make_markov_chain(corpus, n)
sentence = markov.generate_sentence(markov_chain, n)
cleaned_sentence = clean_text.clean_text(sentence)
print(cleaned_sentence)