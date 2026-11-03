import numpy as np

def main():
    stocks = np.genfromtxt('stock_prices_intro.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

    dates = stocks['Date']
    opennp = stocks['Open']
    closep = stocks['Close']
    vol = stocks['Volume']

    print("Stock Data:", stocks)
    print("-----------dates----------\n")
    print(dates)
    print("-----------open prices----------\n")
    print(opennp)
    print("-----------close prices----------\n")
    print(closep)
    print("-----------volume----------\n")
    print(vol)


    rate = (closep - opennp) / opennp * 100
    print("-----------rate----------\n")
    for i in range(5):
        print(f"Date: {dates[i]}, Rate: {rate[i]:.2f}%")

    mean = np.mean(rate)
    print(f"Mean Rate: {mean:.2f}%")
    median = np.median(rate)
    print(f"Median Rate: {median:.2f}%")
    std_dev = np.std(rate)
    print(f"Standard Deviation: {std_dev:.2f}%")

    max_index = np.argmax(rate)
    print(f"Date with Maximum Rate: {dates[max_index]}, Opening Price: {opennp[max_index]}, Closing Price: {closep[max_index]},  Rate: {rate[max_index]:.2f}%")

    min_index = np.argmin(rate) 
    print(f"Date with Minimum Rate: {dates[min_index]}, Opening Price: {opennp[min_index]}, Closing Price: {closep[min_index]},  Rate: {rate[min_index]:.2f}%")

    postive_days = np.sum(rate > 0)
    print(f"Number of Positive Rate Days: {postive_days}")
    negative_days = np.sum(rate < 0)
    print(f"Number of Negative Rate Days: {negative_days}")

    factor = 1 + rate / 100
    cum_return = (np.prod(factor) - 1) * 100
    print(f"Cumulative Return: {cum_return:.2f}%")


if __name__ == "__main__":
    main()
    