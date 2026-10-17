import csv


class DataTable:
    def __init__(self, csv_path: str, reference_table=None):
        """
        Load CSV data into memory.
        Convert all values to float.
        """
        self.data = []
        missing = []  # (row_idx, col_name) of cells that were '?'
        with open(csv_path, 'r') as file:
            data = csv.reader(file)
            header = next(data) 
            # print(header)
            for row in data:
                data_row = {}
                for index, item in enumerate(row):
                    if item =='?':
                        data_row[header[index]] = None
                        missing.append((len(self.data), header[index]))
                    else:
                        data_row[header[index]] = float(item)
                self.data.append(data_row)
        self._fill_missing(missing, reference_table)
    
    def _fill_missing(self, missing, reference_table=None):
        #mean of the VALID values of each column, before filling anything
        self.valid_means = {}
        for feature in (self.data[0].keys()):
            known = [row[feature] for row in self.data if row[feature] is not None]
            if known:
                self.valid_means[feature] = sum(known) / len(known)
        # pick whose means to use
        source = None
        if reference_table:
            source = reference_table.valid_means
        else:
            source = self.valid_means

        # (c) write the mean into every gap
        for row_idx, feature in missing:
            self.data[row_idx][feature] = source[feature]


    def get(self, row_idx: int, col_name: str):
        """
        Return a single value from a row and column.
        """
        return self.data[row_idx][col_name]

    def get_column(self, col_name: str) -> list:
        """
        Return all values in a column.
        """
        values = []
        
        for row in self.data:
            values.append(row[col_name])
            
        return values

    def get_row(self, row_idx: int) -> dict:
        """
        Return a row as {column_name: value}
        """
        return self.data[row_idx]

    def get_column_names(self) -> list:
        """
        Return list of column names.
        """
        return self.data[0].keys()

    def get_column_average(self, col_name: str) -> float:
        """
        Return average of a column.
        """
        values = self.get_column(col_name)
        return sum(values) / len(values)

    def get_column_min(self, col_name: str) -> float:
        """
        Return minimum value of a column.
        """
        values = self.get_column(col_name)
        return min(values)

    def get_column_max(self, col_name: str) -> float:
        """
        Return maximum value of a column.
        """
        values = self.get_column(col_name)
        return max(values)