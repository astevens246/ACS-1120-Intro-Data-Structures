# # choose 3 data structures and implement a histogram with each
# # analyze the count operation's algorithm to identify the time complexity with Big O notation
# # benchmark the count operation's actual running time with small and large histogram sizes (for example, 100 and 1000 unique word types) 

# # Histogram as a of tuples (flat associative array)
# histogram = [
#     ('one', 1),
#     ('fish', 4),
#     ('two', 1),
#     ('red', 1),
#     ('blue', 1)
# ]
# # accessing the histogram
# for item, count in histogram:
#     print(f'{item}: {count}')


# # Sorted list of tuples (flat associative array)
# associative_array = [
#     ('blue', 1),
#     ('fish', 4),
#     ('one', 1),
#     ('red', 1),
#     ('two', 1)
# ]
# # sorted associative array
# sorted_array = sorted(associative_array)
# # accessing the associative array
# for item, count in sorted_array:
#     print(f'{item}: {count}')

# # Dictionary (Python’s built-in dict class)

# dictionary = {
#     'one': 1,
#     'fish': 4,
#     'two': 1,
#     'red': 1,
#     'blue': 1
# }

# # accessing the dictionary
# for item, count in dictionary.items():
#     print(f'{item}: {count}')