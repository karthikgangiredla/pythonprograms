sentence = "the quick brown fox jumps over the lazy dog"
d= {word: sentence.split().count(word) for word in sentence.split()}
print(d)