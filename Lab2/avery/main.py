def load_stopwords(filename):
    with open(filename, 'r') as file:
        stopwords = {word.strip().lower() for word in file }
    return stopwords

'''
text = "Hello, world! How's it going?"

punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
translator = str.maketrans('', '', punctuation)

clean = text.translate(translator)
print(clean)  # "Hello world Hows it going"
'''

def load_words(filename, stopwords):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    words = []
    with open(filename, 'r') as input_file:
            for line in input_file:
                line = line.strip()
                if not line:
                    continue
                for word in line.split():
                    cleaned = word.strip(punctuation).lower()
                    if cleaned and cleaned not in stopwords:
                        words.append(cleaned)
    return words

def term_frequency(words):
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    total_words = len(words)
    freq_dict = {word: round(count / total_words, 5) for word, count in word_dict.items()}
    return freq_dict

def main():
    stopwords = load_stopwords('./test/stopwords4t1.txt')  

    print(f"Loaded {len(stopwords)} stopwords.")
    print(stopwords)
    print('------------------------------')

    wordA = load_words('./test/textA4t1.txt', stopwords)
    wordB = load_words('./test/textB4t1.txt', stopwords)

    print(f"Loaded {len(wordA)} words from textA file.")
    print(wordA)
    print(f"Loaded {len(wordB)} words from textB file.")
    print(wordB)
    print('------------------------------')

    freqA = term_frequency(wordA)
    freqB = term_frequency(wordB)

    print(f"Term frequencies for textA:")
    print(freqA)
    print(f"Term frequencies for textB:")
    print(freqB)
    print('------------------------------')
    print('------------------------------')

    common = freqA.keys() & freqB.keys()
    print(f"Common words between textA and textB: {common}")

    unique_a = {key:value for key, value in freqA.items() if key not in common}
    unique_b = {key:value for key, value in freqB.items() if key not in common}

    print(f"Unique words in textA: {unique_a}")
    print(f"Unique words in textB: {unique_b}")
main()