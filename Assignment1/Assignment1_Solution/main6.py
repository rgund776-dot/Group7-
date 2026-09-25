from file_IO import load_from_csv, load_from_html
from data_processing import print_stats, to_json, save_to_json_file

def count_delim(line, delim):
    # count delimiters outside of double quotes
    count, in_quotes = 0, False
    for ch in line:
        if ch == '"':
            in_quotes = not in_quotes
        elif ch == delim and not in_quotes:
            count += 1
    return count


def detect_file_type(filename: str) -> str:
    CHUNK = 8192
    with open(filename, "r") as f:
        text = f.read(CHUNK)

    head = text.lstrip().lower()
    html_tags = ("<!doctype html", "<html", "<head", "<body", "<div",
                 "<p>", "<p ", "<table", "<span", "<a ", "<br")
    if head.startswith("<") and any(t in head[:2000] for t in html_tags):
        return "html"

    lines = text.splitlines()
    if len(text) == CHUNK:      # last line may be cut off mid-row
        lines = lines[:-1]
    lines = [l for l in lines if l.strip()][:15]

    if len(lines) >= 2:
        counts = [count_delim(l, ",") for l in lines]
        if counts[0] > 0 and all(c == counts[0] for c in counts):
            return "csv"

    raise ValueError('Error, data must be in valid CSV or HTML format')

def main(filename):

    try:
        file_type = detect_file_type(filename)
        # print(f'file {filename} is {file_type}')
        if file_type == 'html':
            table = load_from_html(filename)
            # print(f'table: {table}')
            # print_stats(table)
        elif file_type == 'csv':
            table = load_from_csv(filename)
            # print(f'table: {table}')
        print_stats(table)
        json = to_json(table)
        save_to_json_file(json, filename)
    except ValueError as e:
        raise ValueError(e)
    except AttributeError as e:
        raise AttributeError(e)
    except FileNotFoundError:
        raise FileNotFoundError('File not found')
    except Exception:
        raise Exception('Unexpected error loading file') 


# main('./test/not_data.txt')
# main('./test/census_err.txt')
main('./test/student_test.txt')
# main('./test/census_test.txt')

# main('./data/student_dataset.txt')
# main('./data/student_dataset_corrupted.txt')
# main('./data/census_dataset.txt')
