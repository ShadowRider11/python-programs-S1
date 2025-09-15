text=input("enter your text: ")

word_counts = {word: text.split().count(word) for word in set(text.split())}

print(word_counts)
