

def load_from_html(filename: str) -> list[dict]:
    """
    reads a dataset in HTML format. converts numeric data to float.
    raises an AttributeError if the table rows do not all have the same number of values.
    :param filename: the file path of the html data to read
    :return: the dataset as a list of dictionaries - one dict per object in the file
            each dictionary should map column names to values
    """    
    print(f'loading html file: {filename}')
    with open(filename, 'r') as file:
        contents = file.read()
        all_rows = []

        head, body = contents.split('</thead>')
        # print(f'body: {body}')

        # process the head first, pull out the column names
        head_parts = head.split('<td>')
        # print(f'head_parts: {head_parts}')

        columns = []
        for column_name in head_parts[1:]:
            columns.append(
                column_name.replace('</td>', '').replace('</tr>', '').strip()
            )
        # print(f'columns: {columns}')
        
        # strip off some unecessary tags
        body = body.replace('</tr>', '')
        body = body.replace('</tbody>\n</table>', '')
        # print(f'body: {body}')

        # process the rest of the text: the table body
        rows_text = body.split('<tr>')
        for row_text in rows_text[1:]: # skip the first, which just has a <tbody> tag
            row_text = row_text.replace('</td>', '')
            values = row_text.split('<td>')
            values = values[1:]

            # check the row has the right number of values in it
            if len(values) != len(columns):
                # raise Exception(f'wrong number of values in row: {row_text}')
                raise AttributeError(f'wrong number of values in row: {row_text}')

            this_row_dict = dict()
            for i in range(len(columns)):
                this_column = columns[i]
                this_value = values[i].strip()

                # convert to float if the value is a number
                try:
                    this_value = float(this_value)
                except ValueError:
                    raise ValueError(f'invalid number in row: {row_text}')
                    # pass

                this_row_dict[this_column] = this_value
            
            all_rows.append(this_row_dict)
    
    return all_rows


def load_from_csv(filename: str) -> list[dict]:
    print(f'loading csv file: {filename}')
    with open(filename, 'r') as file:
        contents = file.read().split('\n')
        # print(f'contents: {contents}')
        header = contents[0]
        body = [line for line in contents[1:] if line.strip()]
        # print(f'header: {header}')
        # print(f'body: {body}')

        all_rows = []
        columns = []
        for column_name in header.split(','):
            columns.append(
                column_name.strip()
            )
        # print(f'columns: {columns}')

        for row_text in body:
            values = row_text.split(',')
            # print(f'row_text: {row_text}')

            # check the row has the right number of values in it
            print(f'len(values): {len(values)}, len(columns): {len(columns)}')
            if len(values) != len(columns):
                # raise Exception(f'wrong number of values in row: {row_text}')
                raise AttributeError(f'wrong number of values in row: {row_text}')

            this_row_dict = dict()
            for i in range(len(columns)):
                this_column = columns[i]
                this_value = values[i].strip()

                # convert to float if the value is a number
                try:
                    this_value = float(this_value)
                except ValueError:
                    raise ValueError(f'invalid number in row: {row_text}')
                    # pass

                this_row_dict[this_column] = this_value
            
            all_rows.append(this_row_dict)
        return all_rows





