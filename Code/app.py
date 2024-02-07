# create a flask app that will display the random sentence generated in sentence.py 
# when the user visits the home page

from flask import Flask
import sentence
import string

app = Flask(__name__)


@app.route('/')
def home():
    word_list = sentence.histogram.histogram('great-gatsby.txt')
    histogram_data = sentence.create_histogram(word_list)
    
    sentence_data = sentence.generate_sentence(histogram_data, 25)
    sentence_without_punctuation = ''.join(sentence_data).translate(str.maketrans('', '', string.punctuation))
    return sentence_without_punctuation  # Return the sentence without punctuation
