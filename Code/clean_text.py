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

    return text
