import csv


class DataTable:
    def __init__(self, csv_path: str, reference_data=None):
        """
        Load CSV data into memory.
        Convert all values to float.
        """
        self.data = []
        self.column_names = []
        
        with open(csv_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            
            self.column_names = reader.fieldnames
            
            for row in reader:
                new_row = {}
                
                for column in self.column_names:
                    if row[column] == "?":
                        new_row[column] = None
                    else:
                        new_row[column] = float(row[column])
                
                self.data.append(new_row)
        #replace missing values with averages 
        for column in self.column_names:
            if column == "TumorType":
                continue
                
            if reference_data is None:
                values = [] 
                
                for row in self.data:
                    if row[column] is not None:
                        values.append(row[column])
                
                if len(values) == 0:
                    continue 
                
                average = sum(values) / len(values)
                
            else:
                average = reference_data.get_column_average(column)
            
            for row in self.data:
                if row[column] is None:
                    row[column] = average
            
            

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
        return self.column_names

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