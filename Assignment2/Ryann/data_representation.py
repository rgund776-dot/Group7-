import csv


class DataTable:
    def __init__(self, csv_path: str):
        """
        Load CSV data into memory.
        Convert all values to float.
        """
        pass

    def get(self, row_idx: int, col_name: str):
        """
        Return a single value from a row and column.
        """
        pass

    def get_column(self, col_name: str) -> list:
        """
        Return all values in a column.
        """
        pass

    def get_row(self, row_idx: int) -> dict:
        """
        Return a row as {column_name: value}
        """
        pass

    def get_column_names(self) -> list:
        """
        Return list of column names.
        """
        pass

    def get_column_average(self, col_name: str) -> float:
        """
        Return average of a column.
        """
        pass

    def get_column_min(self, col_name: str) -> float:
        """
        Return minimum value of a column.
        """
        pass

    def get_column_max(self, col_name: str) -> float:
        """
        Return maximum value of a column.
        """
        pass