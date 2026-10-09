import csv


class DataTable:
    def __init__(self, csv_path: str):
        """
        Load CSV data into memory.
        Convert all values to float.
        """
        self.data = []
        with open(csv_path, 'r') as file:
            data = csv.reader(file)
            header = next(data) 
            # print(header)
            for row in data:
                data_row = {}
                for index, item in enumerate(row):
                #    might need better handling for ? or missing values
                   try:
                    data_row[header[index]] = float(item)
                   except:
                     data_row[header[index]] = float(0)

                self.data.append(data_row)
            # print(self.data)       

    def get(self, row_idx: int, col_name: str):
        """
        Return a single value from a row and column.
        """
        return self.data[row_idx][col_name]

    def get_column(self, col_name: str) -> list:
        """
        Return all values in a column.
        """
        return [row[col_name] for row in self.data]

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
        total = sum(self.get_column(col_name))
        count = len(self.get_column(col_name))
        return total/count

    def get_column_min(self, col_name: str) -> float:
        """
        Return minimum value of a column.
        """
        return min(self.get_column(col_name))

    def get_column_max(self, col_name: str) -> float:
        """
        Return maximum value of a column.
        """
        return max(self.get_column(col_name))