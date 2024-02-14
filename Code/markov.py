import random 
from dictogram import Dictogram

# Learn a Markov chain from a corpus. 

# You’ve already written code to find how often a token appears in a corpus, 
# but now you need to find how often a token appears after another token.

# Do a random walk on a Markov chain. 
# This should be pretty simple if you pick a good way to store the Markov chain you learn.
    
corpus = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!"
# with open("great-gatsby.txt", "r") as file:
#     corpus = file.read()

def make_markov_chain(corpus):
    markov_chain = {}
    words = corpus.split()
    for i in range(len(words)-1):
        if words[i] in markov_chain:
            markov_chain[words[i]].add_count(words[i+1])
        else:
            markov_chain[words[i]] = Dictogram([words[i+1]])
    return markov_chain

pairs = make_markov_chain(corpus)

word_dict = {}

for word_1, word_2 in pairs.items():
    if word_1 in word_dict:
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]
        
first_word = random.choice(corpus.split())
chain = [first_word]
n_words = 10

for i in range(n_words):
    if chain[-1] in word_dict:
        dictogram = random.choice(word_dict[chain[-1]])
        next_word = dictogram.return_weighted_random_word()
        chain.append(next_word)
    else:
        break
    
print(' '.join(chain))






# Nouns = class needs to be made 
# class MarkovChain(dict):
#     def __init__(self):
#     #Empty dictionary to store markov chain 
#     # Key == word
#     # Value == list of words that follow the key-word
    
#     def walk(self, distance)
    
