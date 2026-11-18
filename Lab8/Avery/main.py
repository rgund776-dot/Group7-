import pandas as pd

from Lab3.Avery import classes

def task1_load_explore():
    data = pd.read_csv('labor.csv')
    header  = data.head()
    column_name = data['wage-increase-first-year']
    dimensions = data.shape
    data_type = data.dtypes
    missing_rows = data[data.isna().any(axis=1)]

    # print("Header of the DataFrame:\n", header)
    # print("\nColumn 'wage-increase-first-year':\n", column_name)
    # print("\nDimensions of the DataFrame:", dimensions)
    # print("\nData Types of Each Column:\n", data_type)

    return data

data = task1_load_explore()


def task2_access_data(df):
    column_series = df['wage-increase-first-year']
    value_by_index = column_series.iloc[0]
    value_by_name = df.loc[0, 'wage-increase-first-year']
    first_five = column_series.iloc[0:5]

    subset = df[['wage-increase-first-year', 'wage-increase-second-year']]
    subset_value_name = subset.loc[1, 'wage-increase-second-year']
    multiple_rows = df.iloc[1:4]
    multiple_rows_by_name = df.loc[1:3]
    multiple_column_by_iloc = df.iloc[:, [1, 2]]
    multiple_columns = df.loc[:, ['wage-increase-first-year', 'wage-increase-second-year']]

    # return column_series, value_by_index, value_by_name, first_five, subset, subset_value_name, multiple_rows, multiple_rows_by_name, multiple_column_by_iloc, multiple_columns

    return {
        "column_series": column_series,
        "value_by_index": value_by_index,
        "value_by_name": value_by_name,
        "first_five": first_five,
        "subset": subset,
        "subset_value_name": subset_value_name,
        "multiple_rows": multiple_rows,
        "multiple_rows_by_name": multiple_rows_by_name,
        "multiple_column_by_iloc": multiple_column_by_iloc,
        "multiple_columns": multiple_columns
    }

    # print("Value by Index:", value_by_index)
    # print("Value by Name:", value_by_name)
    # print("First 5",column_series.iloc[:5])
    # print("Subset of DataFrame:\n", subset)
    # print("Value from Subset by Name:", subset_value_name)
    # print("Multiple Rows:\n", multiple_rows)
    # print("Multiple Rows by Name:\n", multiple_rows_by_name)
    # print("Multiple Columns by iloc:\n", multiple_column_by_iloc)
    # print("Multiple Columns:\n", multiple_columns)


column_series, value_by_index, value_by_name, first_five, subset, subset_value_name, multiple_rows, multiple_rows_by_name, multiple_column_by_iloc, multiple_columns = task2_access_data(data)
# task2_access_data(data)

def task3_filter_data(df):
    # clean data, check for missing string values
#   print(df["class"].dtype)
#   print(df["class"].value_counts(dropna=False))
#   print(df["class"].dropna().map(repr).unique())  # repr makes spaces visible
    classes = df["class"].astype("string").str.strip().str.casefold()
    good = df[classes == "good"]
    bad = df[classes == "bad"]
    first_year = df[df['wage-increase-first-year'] > 2.5]
    holidays = df[df['statutory-holidays'] > 10]
    first_year_holiday = df[(df['wage-increase-first-year'] > 2.5) & (df['statutory-holidays'] > 10)]
    avg_score = df["wage-increase-first-year"].mean()
    max_score = df["wage-increase-first-year"].max()
    # print(avg_score, max_score)

    # return good, bad, first_year, holidays, first_year_holiday, avg_score, max_score

    return{
        "good": good,
        "bad": bad,
        "first_year": first_year,
        "holidays": holidays,
        "first_year_holiday": first_year_holiday,
        "avg_score": avg_score,
        "max_score": max_score
    }

good, bad, first_year, holidays, first_year_holiday, avg_score, max_score = task3_filter_data(data)