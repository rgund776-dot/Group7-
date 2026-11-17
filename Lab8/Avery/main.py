import pandas as pd

def task1_load_explore():
    data = pd.read_csv('labor.csv')
    header  = data.head()
    column_name = data['wage-increase-first-year']
    dimensions = data.shape
    data_type = data.dtypes

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
    first_five = column_series.iloc[:5]

    subset = df[['wage-increase-first-year', 'wage-increase-second-year']]
    subset_value_name = subset.loc[1, 'wage-increase-second-year']
    multiple_rows = df.iloc[1:4]
    multiple_rows_by_name = df.loc[1:3]
    multiple_column_by_iloc = df.iloc[:, [1, 2]]
    multiple_columns = df.loc[:, ['wage-increase-first-year', 'wage-increase-second-year']]

    # print("Value by Index:", value_by_index)
    # print("Value by Name:", value_by_name)
    # print("First 5",column_series.iloc[:5])
    # print("Subset of DataFrame:\n", subset)
    # print("Value from Subset by Name:", subset_value_name)
    # print("Multiple Rows:\n", multiple_rows)
    # print("Multiple Rows by Name:\n", multiple_rows_by_name)
    # print("Multiple Columns by iloc:\n", multiple_column_by_iloc)
    # print("Multiple Columns:\n", multiple_columns)



task2_access_data(data)

def task3_filter_data(df):
    good = df[df['class'] == "good"]
    bad = df[df['class'] == "bad"]
    first_year = df[df['wage-increase-first-year'] > 2.5]
    holidays = df[df['statutory-holidays'] > 10]
    first_year_holiday = df[(df['wage-increase-first-year'] > 2.5) & (df['statutory-holidays'] > 10)]
    avg_score = df["wage-increase-first-year"].mean()
    max_score = df["wage-increase-first-year"].max()
    # print(avg_score, max_score)

task3_filter_data(data)