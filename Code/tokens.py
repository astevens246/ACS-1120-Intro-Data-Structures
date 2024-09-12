import re


def tokenize(text):
    return re.findall(r'\b\w+\b', text)

def remove_punctuation(text):
    no_punc_text = re.sub('[,.()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    return no_punc_text

