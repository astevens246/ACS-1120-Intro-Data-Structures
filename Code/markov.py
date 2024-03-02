import random 
import string
# Learn a Markov chain from a corpus. 

# You’ve already written code to find how often a token appears in a corpus, 
# but now you need to find how often a token appears after another token.

# Do a random walk on a Markov chain. 
# This should be pretty simple if you pick a good way to store the Markov chain you learn.
    
# with open("great-gatsby.txt", "r") as file:
#     corpus = file.read()

class MarkovChain(dict):
    def __init__(self):
        super().__init__()
    #Empty dictionary to store markov chain 
    # Key == word
    # Value == list of words that follow the key-word

    def make_markov_chain(self, corpus):
        markov_chain = {}
        words = corpus.split()
        for i in range(len(words)-1):
            if words[i] not in markov_chain:
                markov_chain[words[i]] = []
            markov_chain[words[i]].append(words[i+1])
        return markov_chain

    def generate_sentence(self, markov_chain, n_words=10):
        first_word = random.choice(list(markov_chain.keys()))
        chain = [first_word]
        for i in range(n_words):
            if chain[-1] in markov_chain:
                next_word = random.choice(markov_chain[chain[-1]])
                chain.append(next_word)
            else:
                break
        return ' '.join(chain)

corpus = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!"
markov = MarkovChain()
markov_chain = markov.make_markov_chain(corpus)
sentence = markov.generate_sentence(markov_chain)
print(sentence)