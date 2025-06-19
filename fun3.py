def longest_word(sentence):
    words = sentence.split()
    max_word = ""
    for word in words:
        # Remove punctuation (optional)
        word = word.strip(".,!?;:'\"")
        if len(word) > len(max_word):
            max_word = word
    return max_word, len(max_word)

# Example usage
sentence = "The quick brown fox jumped over the lazy dog."
word, length = longest_word(sentence)
print("Longest word:", word)
print("Length:", length)


