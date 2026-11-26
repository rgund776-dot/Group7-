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

    # main_info = data_main.info()
    # prices_info = data_prices.info()

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

    return inner_merged, left_merged, right_merged, outer_merged


def task3_analyze_merges(merge_results):

    inner_merged, left_merged, right_merged, outer_merged = merge_results

    shapes = {"inner": inner_merged.shape,
              "left": left_merged.shape,
              "right": right_merged.shape,
              "outer": outer_merged.shape
              }

    inner_missing = inner_merged.isna().sum()
    left_missing = left_merged.isna().sum()
    right_missing = right_merged.isna().sum()
    outer_missing = outer_merged.isna().sum()

    missing = pd.DataFrame({"inner": inner_missing,
                            "left": left_missing,
                            "right": right_missing,
                            "outer": outer_missing})

    price_missing = {"inner": int(inner_merged["price"].isna().sum()),
                     "left": int(left_merged["price"].isna().sum()),
                     "right": int(right_merged["price"].isna().sum()),
                     "outer": int(outer_merged["price"].isna().sum())
                     }

    main_keys = set(left_merged["item_id"])
    price_keys = set(right_merged["item_id"])

    in_both = main_keys & price_keys
    only_main = main_keys - price_keys
    only_prices = price_keys - main_keys

    both_rows = int(outer_merged["item_id"].isin(in_both).sum())
    only_main_rows = int(outer_merged["item_id"].isin(only_main).sum())
    only_prices_rows = int(outer_merged["item_id"].isin(only_prices).sum())

    row_counts = {"inner": inner_merged.shape[0],
                  "left": left_merged.shape[0],
                  "right": right_merged.shape[0],
                  "outer": outer_merged.shape[0]}

    smallest = []
    largest = []
    for name, rows in row_counts.items():
        if rows == min(row_counts.values()):
            smallest.append(name)
        if rows == max(row_counts.values()):
            largest.append(name)

    num_main = len(left_merged)  

    keeps_all_main = []
    if inner_merged["item_id"].isin(main_keys).sum() == num_main:
        keeps_all_main.append("inner")
    if left_merged["item_id"].isin(main_keys).sum() == num_main:
        keeps_all_main.append("left")
    if right_merged["item_id"].isin(main_keys).sum() == num_main:
        keeps_all_main.append("right")
    if outer_merged["item_id"].isin(main_keys).sum() == num_main:
        keeps_all_main.append("outer")

    keeps_all_prices = []
    if price_keys <= set(inner_merged["item_id"]):
        keeps_all_prices.append("inner")
    if price_keys <= set(left_merged["item_id"]):
        keeps_all_prices.append("left")
    if price_keys <= set(right_merged["item_id"]):
        keeps_all_prices.append("right")
    if price_keys <= set(outer_merged["item_id"]):
        keeps_all_prices.append("outer")

    # print("Dimensions (rows, columns):", shapes)
    # print("\nMissing values per column:\n", missing)
    # print("\nMissing price:", price_missing)
    # print("\nUnique item_id -> in both:", len(in_both),
    #       "| only main:", len(only_main), "| only prices:", len(only_prices))
    # print("Rows -> matched:", both_rows, "| main only:", only_main_rows,
    #       "| prices only:", only_prices_rows)
    # print("\nSmallest:", smallest, "| Largest:", largest)
    # print("Keeps all main:", keeps_all_main)
    # print("Keeps all prices:", keeps_all_prices)

    analysis = {
        "shapes": shapes,
        "missing_values": missing,
        "price_missing": price_missing,
        "unique_in_both": len(in_both),
        "unique_only_main": len(only_main),
        "unique_only_prices": len(only_prices),
        "only_prices_ids": sorted(only_prices),
        "rows_matched": both_rows,
        "rows_main_only": only_main_rows,
        "rows_prices_only": only_prices_rows,
        "smallest": smallest,
        "largest": largest,
        "keeps_all_main": keeps_all_main,
        "keeps_all_prices": keeps_all_prices,
    }
    return inner_merged, left_merged, right_merged, outer_merged, analysis


# df1, df2 = task1_load_explore()

# data_merge = task2_merge_data(df1, df2)

# # data_merge["inner_merged"].shape

# df_analyze = task3_analyze_merges(data_merge)