
def create_stop_words(file_path: str) -> set:
    try:
        stop_words = set()
        input_file = open(file_path, 'r')
        for line in input_file:
            stop_words.add(line.strip())
        return stop_words
    except Exception:
      raise Exception
    finally:
        input_file.close()

def parse_text(file_path: str, stop_words: set) -> list:
    try:
        input_file = open(file_path, 'r')
        words = []
        for line in input_file:
            # print(line.strip().split())
            for word in line.strip().split():
                if word not in stop_words:
                    words.append(word)
        return words
    except Exception:
          raise Exception
    finally:
        input_file.close()

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

def word_dict(words: dict, word_total:int) -> dict: 
    new_dict = {}
    # print(words)
    for key, value in words.items():
        # print(word)
        # print(words[word])
        freq = term_frequency(value, word_total)
        new_dict[key] = round(freq, 5)
    return new_dict

def common_words(dict1: dict, dict2: dict) -> set:
    common = dict1.keys() & dict2.keys()
    return common

def unique_words(dict1: dict, common: set) -> set:
    unique = {key:value for key, value in dict1.items() if key not in common}
    return unique

def create_word_freq(file_path:str, stop_words: set) -> dict:
    try:
        txt_list = parse_text(file_path, stop_words)
        txt_words_dict = word_count(txt_list)
# do we calc word freq with before or after we filter out the stop words (effect total word count)
        txt_freq = word_dict(txt_words_dict, len(txt_list))
        return txt_freq
    except Exception:
      raise Exception

def main():
    try:
        stop_words = create_stop_words('stopwords.txt')
        file_A = create_word_freq('textA.txt', stop_words)
        file_B = create_word_freq('textB.txt', stop_words)

        # print(txt2_freq)
        common = common_words(file_A, file_B)
        unique_A = unique_words(file_A, common)
        unique_B = unique_words(file_B, common)
        print(unique_A)
        print(unique_B)
        
    except Exception:
      print(Exception)

main()