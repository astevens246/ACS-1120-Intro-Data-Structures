# def create_histogram(text):
#     words = text.split()
#     histogram = {}
#     for word in words:
#         if word in histogram:
#             histogram[word] += 1
#         else:
#             histogram[word] = 1
#     return histogram

# text = "I like dogs and you like dogs. I like cats but you hate cats."
# histogram = create_histogram(text)
# print(histogram)

word_frequency = {}
sample_text = "I like dogs and you like dogs. I like cats but you hate cats."

words = sample_text.replace('.', '').split()

for word in words: 
    word_frequency[word] = word_frequency.get(word, 0) + 1

print(word_frequency)