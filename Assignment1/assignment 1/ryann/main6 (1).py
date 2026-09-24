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

"""
read tabular data set from file 
id format (csv, html)
parse accordingly
if not csv hmtl raise exception "Error, data must in valid CSV or HTML format"
student dat --> html
census --> csv 

stores tabular data as list of dictionarires

print out simple stat analysis --> print_stats() function
    text columns --> column name, most common value
    numerical column --> column name, avg of all values in column

formatted:
    Name1: average 2342342
    Name2: most common value is 'filler'

resaves data set in json format
"""
