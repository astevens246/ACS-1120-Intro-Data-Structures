import re


def tokenize(text):
    return re.findall(r'\b\w+\b', text)

def remove_punctuation(text):
    no_punc_text = re.sub('[,.()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    return no_punc_text

corpus = "One night--it was on the twentieth of March, 1888--I was returning from a journey to a patient (for I had now returned to civil practice), when my way led me through Baker Street. As I passed the well-remembered door, which must always be associated in my mind with my wooing, and with the dark incidents of the Study in Scarlet, I was seized with a keen desire to see Holmes again, and to know how he was employing his extraordinary powers."

tokens = tokenize(corpus)

print(tokens)
print(remove_punctuation(corpus))
