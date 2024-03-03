from flask import render_template, Flask
from clean_text import clean_text, postprocess_sentence
from tokens import tokenize, remove_punctuation

import string
from markov import MarkovChain  # Import the MarkovChain class

app = Flask(__name__)

@app.route('/')
def home():
    with open("great-gatsby.txt", "r") as file:
        corpus = file.read()
    # Clean and tokenize the text
    cleaned_corpus = clean_text(corpus)
    no_punc_corpus = remove_punctuation(cleaned_corpus)
    tokens = tokenize(no_punc_corpus)

    # Convert tokens back to string and feed into the Markov chain
    corpus = ' '.join(tokens)
    markov = MarkovChain()
    n = 2 # Set the number of words to look at
    markov_chain = markov.make_markov_chain(corpus, n)
    sentence = markov.generate_sentence(markov_chain, n)
    sentence = postprocess_sentence(sentence)
    return render_template('index.html', sentence=sentence)  # Return the sentence with punctuation