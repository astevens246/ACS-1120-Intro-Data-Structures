# clean up the text to make sure we parse and count only legitimate words, excluding any HTML tags or symbols.
# Removing unwanted punctuation (e.g. _ or * characters around words)
# Converting HTML character codes to their ASCII equivalent (e.g. &#8212; to —)
# Normalizing punctuation (e.g. convert both types of quotes – ‘’ and “” – to regular quotes '' and "")

import re
import html

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove unwanted punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Convert HTML character codes to ASCII equivalent
    text = html.unescape(text)
   # Normalize punctuation
    text = text.replace('‘', "'").replace('’', "'")
    text = text.replace('“', '"').replace('”', '"')
    
    # convert to lowercase
    text = text.lower()

    return text

def postprocess_sentence(sentence):
    words = sentence.split()
    for i in range(1, len(words)):
        # If a word starts with a punctuation mark, move the punctuation to the end of the previous word
        if words[i][0] in ',.!?':
            words[i - 1] += words[i][0]
            words[i] = words[i][1:]

    # Capitalize the first word
    words[0] = words[0].capitalize()

    # Add punctuation at the end if it's not there
    if words[-1][-1] not in '.!?':
        words[-1] += '.'

    return ' '.join(words)
