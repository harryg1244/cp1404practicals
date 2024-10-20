"""
Word Occurrences
Estimate: 30 minutes
Actual:   38 minutes
"""

word_to_count = {}
text = input("Text: ")
# input = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
