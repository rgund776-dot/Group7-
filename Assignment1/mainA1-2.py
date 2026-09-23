from file_IO import load_from_html, load_from_csv
from data_processing import print_stats


# load data
filename = './student_dataset.txt'

try:
    table = load_from_html(filename)

except Exception:
    try:
        table = load_from_csv(filename)

    except Exception:
        raise Exception('Error, data must be in valid CSV or HTML format')


# print table statistics
print_stats(table)