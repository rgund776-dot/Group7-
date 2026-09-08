# Read a record from the user
record = input("Enter a record: ")
# Split the record into its fields
date, stock_ticker, opening_price, percent_change = record.split(",")

# Extract year, month, and day
year, month, day = date.split("-")
year, month, day
# Convert numbers to floats
opening_price = float(opening_price)
percent_change = float(percent_change)
opening_price, percent_change 
# Calculate closing price
closing_price = opening_price * (1 + percent_change / 100)
# Print results
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Closing price: $", round(closing_price, 2))
print("this avery")
