from file_IO import load_from_html
#from file_IO import load_from_csv
from data_processing import print_stats

# load data
filename = './assignment 1/student_dataset.txt' #change to run different files

"""
def file_format(filename: str):
    if filename.startswith("<"):
        load_from_html(filename)
    else:
        try:
            # if #something here to id if csv or wrong format
            # load_from_csv(filename)
            print("test")
        except:
            raise Exception("Error, data must in valid CSV or HTML format")
        
#print(file_format(filename))
"""

table = load_from_html(filename)

# print table statistics 
print_stats(table)