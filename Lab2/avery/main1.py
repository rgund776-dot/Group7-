# def create_stop_words(file_path: str) -> set:
#     try:
#         stop_words = set()
#         input_file = open(file_path, 'r')
#         for line in input_file:
#             word = line.strip().lower()
#             if word:
#                 stop_words.add(word)
#         return stop_words
#     # except Exception:
#     #     raise Exception
#     finally:
#         input_file.close()

# def parse_text(file_path: str, stop_words: set) -> list:
#     punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
#     try:
#         input_file = open(file_path, 'r')
#         words = []
#         for line in input_file:
#             line = line.strip()
#             if not line:
#                 continue
#             for word in line.split():
#                 cleaned = word.strip(punctuation).lower()
#                 if cleaned and cleaned not in stop_words:
#                     words.append(cleaned)
#         return words
#     # except Exception:
#     #     raise Exception
#     finally:
#         input_file.close()

def create_stop_words(file_path: str) -> set:
    stop_words = set()
    with open(file_path, 'r') as input_file:
        for line in input_file:
            word = line.strip().lower()
            if word:
                stop_words.add(word)
    return stop_words

def parse_text(file_path: str, stop_words: set) -> list:
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    words = []
    with open(file_path, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            for word in line.split():
                cleaned = word.strip(punctuation).lower()
                if cleaned and cleaned not in stop_words:
                    words.append(cleaned)
    return words

def term_frequency(word: int, total_words: int) -> float:
    return word / total_words

def word_count(words: list) -> dict:
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def compute_frequencies(word_counts: dict, word_total: int) -> dict:
    new_dict = {}
    for key, value in word_counts.items():
        freq = term_frequency(value, word_total)
        new_dict[key] = round(freq, 5)
    return new_dict

def common_words(dict1: dict, dict2: dict) -> set:
    common = dict1.keys() & dict2.keys()
    return common

def unique_words(dict1: dict, common: set) -> set:
    unique = {key: value for key, value in dict1.items() if key not in common}
    return unique

def create_word_freq(file_path: str, stop_words: set) -> dict:
    txt_list = parse_text(file_path, stop_words)
    txt_words_dict = word_count(txt_list)
    # do we calc word freq with before or after we filter out the stop words (effect total word count)
    txt_freq = compute_frequencies(txt_words_dict, len(txt_list))
    return txt_freq

def main():
    try:
        stop_words = create_stop_words('stopwords.txt')
        file_A = create_word_freq('textAwwe.txt', stop_words)
        file_B = create_word_freq('textB.txt', stop_words)

        common = common_words(file_A, file_B)
        unique_A = unique_words(file_A, common)
        unique_B = unique_words(file_B, common)

        return unique_A, unique_B

    except Exception as e:
        print(f"Error: {e}")

print(main())