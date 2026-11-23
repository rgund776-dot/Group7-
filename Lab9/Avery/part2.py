import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

def task1_load_explore():
    data_main = pd.read_csv(DATA_DIR /'modcloth_main.csv')
    data_prices = pd.read_csv(DATA_DIR /'modcloth_prices.csv')

    first_five_main  = data_main.head()
    first_five_price  = data_prices.head()

    main_shape = data_main.shape
    prices_shape = data_prices.shape

    main_info = data_main.info()
    prices_info = data_prices.info()

    main_na = data_main.isna().sum()
    prices_na = data_prices.isna().sum()

    common_cols = data_main.columns.intersection(data_prices.columns)

    return (data_main, data_prices)

    

def task2_merge_data(main_df, prices_df):
    common_cols = main_df.columns.intersection(prices_df.columns)
    if "item_id" not in common_cols:
        raise ValueError("Common column is not item_id")


    inner_merged =pd.merge(
            main_df,
            prices_df,
            on="item_id",
            how="inner"
        )

    left_merged = pd.merge(
            main_df,
            prices_df,
            on="item_id",
            how="left"
        )
    right_merged  = pd.merge(
            main_df,
            prices_df,
            on="item_id",
            how="right"
        )
    outer_merged = pd.merge(
            main_df,
            prices_df,
            on="item_id",
            how="outer"
        )

    return {
        "inner_merged":inner_merged,
        "left_merged":left_merged,
        "right_merged":right_merged,
        "outer_merged":outer_merged,
    }


def analyze_merges(merge_results):
    inner_merged, left_merged, right_merged, outer_merged = merge_results
    merges = {"inner": inner_merged, 
              "left": left_merged,
              "right": right_merged, 
              "outer": outer_merged
              }

    shapes = {"inner": inner_merged.shape, 
              "left": left_merged.shape,
              "right": right_merged.shape, 
              "outer": outer_merged.shape
              }

    missing = {"inner": inner_merged.isna().sum(), 
              "left": left_merged.isna().sum(),
              "right": right_merged.isna().sum(), 
              "outer": outer_merged.isna().sum()
              }
    main_keys = set(left_merged["item_id"])          
    price_keys = set(right_merged["item_id"])  

    in_both = main_keys & price_keys
    only_main = main_keys - price_keys
    only_prices = price_keys - main_keys

    # Row-level counts (a main item can have many reviews)
    both_rows = int(outer_merged["item_id"].isin(in_both).sum())
    only_main_rows = int(outer_merged["item_id"].isin(only_main).sum())
    only_prices_rows = int(outer_merged["item_id"].isin(only_prices).sum())
    
    pass

df1, df2 = task1_load_explore()

task2_merge_data(df1, df2)