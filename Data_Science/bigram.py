def find_bigrams(sentence):
    # Tokenize the sentence by splitting on whitespace.
    # This simple approach doesn't remove punctuation or convert to lowercase.
    tokens = sentence.split()

    # Create bigrams by pairing each word with the next one.
    bigrams = [(tokens[i], tokens[i + 1]) for i in range(len(tokens) - 1)]

    return bigrams


# Example usage:
sentence = """
Have free hours and love children?
Drive kids to school, soccer practice and other activities.
"""

# Call the function and print the result
print(find_bigrams(sentence))
