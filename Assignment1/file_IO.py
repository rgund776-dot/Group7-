

def load_from_html(filename: str) -> list[dict]:
    """
    reads a dataset in HTML format. converts numeric data to float.
    raises an AttributeError if the table rows do not all have the same number of values.
    :param filename: the file path of the html data to read
    :return: the dataset as a list of dictionaries - one dict per object in the file
            each dictionary should map column names to values
    """    
    with open(filename, 'r') as file:
        contents = file.read()
        all_rows = []

        head, body = contents.split('</thead>')

        # process the head first, pull out the column names
        head_parts = head.split('<td>')

        columns = []
        for column_name in head_parts[1:]:
            columns.append(
                column_name.replace('</td>', '').replace('</tr>', '').strip()
            )
        
        # strip off some unecessary tags
        body = body.replace('</tr>', '')
        body = body.replace('</tbody>\n</table>', '')

        # process the rest of the text: the table body
        rows_text = body.split('<tr>')
        for row_text in rows_text[1:]: # skip the first, which just has a <tbody> tag
            row_text = row_text.replace('</td>', '')
            values = row_text.split('<td>')
            values = values[1:]

            # check the row has the right number of values in it
            if len(values) != len(columns):
                raise AttributeError(f'wrong number of values in row: {row_text}')

            this_row_dict = dict()
            for i in range(len(columns)):
                this_column = columns[i]
                this_value = values[i].strip()

                # convert to float if the value is a number
                try:
                    this_value = float(this_value)
                except ValueError:
                    pass

                this_row_dict[this_column] = this_value
            
            all_rows.append(this_row_dict)
    
    return all_rows


# need to read a dataset in csv format, and convert numbers to float data 
#we need to raise an attributeError if the table rows do not have all the same number of values 
#return the dataset as a list of dicts, one per object in the file 

def load_from_csv(filename: str) -> list[dict]:
    with open(filename, 'r') as file:

        all_rows = []

        # first line contains the column names
        columns = file.readline().strip().split(',')

        # process each remaining row
        for row in file:
            row = row.strip()

            # skip empty lines
            if row == '':
                continue

            values = row.split(',')

            # check the row has the right number of values
            if len(values) != len(columns):
                raise AttributeError(f'wrong number of values in row: {row}')

            this_row_dict = dict()

            for i in range(len(columns)):
                this_column = columns[i].strip()
                this_value = values[i].strip()

                # convert to float if the value is a number
                try:
                    this_value = float(this_value)
                except ValueError:
                    pass

                this_row_dict[this_column] = this_value

            all_rows.append(this_row_dict)

    return all_rows

def save_to_json(data: list[dict], filename: str) -> None:
    """
    saves a dataset stored as a list of dictionaries in JSON format
    """

    with open(filename, 'w') as file:

        file.write('[\n')

        for i in range(len(data)):

            file.write('  {\n')

            columns = list(data[i].keys())

            for j in range(len(columns)):

                column = columns[j]
                value = data[i][column]

                if type(value) == float:
                    file.write(f'    "{column}": {value}')
                else:
                    file.write(f'    "{column}": "{value}"')

                if j < len(columns) - 1:
                    file.write(',')

                file.write('\n')

            file.write('  }')

            if i < len(data) - 1:
                file.write(',')

            file.write('\n')

        file.write(']\n')