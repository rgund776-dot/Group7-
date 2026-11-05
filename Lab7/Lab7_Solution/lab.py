
import numpy as np


def load_data(filename):
    # Load the CSV file
    data = np.genfromtxt(
        filename,
        delimiter=",",
        names=True,
        dtype=None,
        encoding="utf-8"
    )

    # Extract the four columns
    date = data["Date"]
    openp = data["Open"]
    closep = data["Close"]
    vol = data["Volume"]

    # print("Task 1 - Loaded Stock Data")
    print("Dates:", date)
    print("Opening Prices:", openp)
    print("Closing Prices:", closep)
    print("Trading Volumes:", vol)

    return date, openp, closep, vol



def calculate_returns(date, openp, closep):
    # Calculate daily return rates
    rate = (closep - openp) / openp * 100

    # print("\nTask 2 - First Five Daily Returns")

    for i in range(5):
        print(date[i], ":", round(rate[i], 2), "%")

    return rate


def calculate_statistics(rate):
    # Calculate statistical measures
    mean_rate = np.mean(rate)
    median_rate = np.median(rate)
    std_rate = np.std(rate)

    # print("\nTask 3 - Basic Statistics")
    print("Mean:", round(mean_rate, 2), "%")
    print("Median:", round(median_rate, 2), "%")
    print("Standard Deviation:", round(std_rate, 2), "%")

    return mean_rate, median_rate, std_rate


def find_best_worst_days(date, openp, closep, rate):
    # Find the highest and lowest returns
    best_day = np.argmax(rate)
    worst_day = np.argmin(rate)

    # print("\nTask 4 - Best Trading Day")
    print("Date:", date[best_day])
    print("Opening Price:", openp[best_day])
    print("Closing Price:", closep[best_day])
    print("Daily Return:", round(rate[best_day], 2), "%")

    return best_day, worst_day


def count_trading_days(rate):
    # Create Boolean masks
    positive_days = rate > 0
    negative_days = rate < 0

    # Count positive and negative days
    up_days = np.sum(positive_days)
    down_days = np.sum(negative_days)

    # print("\nTask 5 - Up and Down Trading Days")
    print("Positive trading days:", up_days)
    print("Negative trading days:", down_days)

    return up_days, down_days


def calculate_cumulative_return(rate):
    # Convert daily rates into return factors
    f = 1 + rate / 100

    # Calculate cumulative return
    cum_return = (np.prod(f) - 1) * 100

    # print("\nTask 6 - Cumulative Return")
    print("Estimated Cumulative Return:", round(cum_return, 2), "%")

    return cum_return