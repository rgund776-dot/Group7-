import pandas as pd

def task1_load_explore():
    data = pd.read_csv('labor.csv')
    header  = data.head()
    column_name = data['wage-increase-first-year']
    dimensions = data.shape
    data_type = data.dtypes
    missing_rows = data[data.isna().any(axis=1)]

    return data

data = task1_load_explore()


def task2_access_data(df):
    column_series = df['wage-increase-first-year']
    first_by_index = column_series.iloc[0]
    first_by_name = df.loc[0, 'wage-increase-first-year']
    first_five = column_series.iloc[0:5]
    col_first_second_year = df[['wage-increase-first-year', 'wage-increase-second-year']]

    # These values will be changes when running the test cases
    specific_value_loc = df.loc[1, 'wage-increase-second-year']
    multiple_rows_iloc = df.iloc[1:4]
    multiple_rows_loc = df.loc[1:3]
    multiple_column_iloc = df.iloc[:, [1, 2]]
    multiple_columns_loc = df.loc[:, ['wage-increase-first-year', 'wage-increase-second-year']]

    # return column_series, first_by_index, first_by_name, first_five, col_first_second_year, specific_value_loc, multiple_rows_iloc, multiple_rows_loc, multiple_column_iloc, multiple_columns_loc

    return {
        "column_series": column_series,
        "first_by_index": first_by_index,
        "first_by_name": first_by_name,
        "first_five": first_five,
        "col_first_second_year": col_first_second_year,
        "specific_value_loc": specific_value_loc,
        "multiple_rows_iloc": multiple_rows_iloc,
        "multiple_rows_loc": multiple_rows_loc,
        "multiple_column_iloc": multiple_column_iloc,
        "multiple_columns_loc": multiple_columns_loc
    }

def task3_filter_data(df):
    # clean data, check for missing string values
    classes = df["class"].astype("string").str.strip().str.casefold()
    good = df[classes == "good"]
    bad = df[classes == "bad"]
    first_year = df[df['wage-increase-first-year'] > 2.5]
    holidays = df[df['statutory-holidays'] > 10]

    mask1 = df['wage-increase-first-year'] > 2.5
    mask2 = df['statutory-holidays'] > 10
    first_year_holiday = df[(mask1) & (mask2)]
    
    avg_score = df["wage-increase-first-year"].mean()
    max_score = df["wage-increase-first-year"].max()

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
