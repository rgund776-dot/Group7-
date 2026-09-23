def load_stopwords(filename):
    with open(filename, 'r') as file:
        stopwords = {word.strip().lower() for word in file }
    return stopwords

def load_words(filename, stopwords):
    pass

def term_frequency(words):
    pass

def main():
    pass


main()