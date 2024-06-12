#ask 1: Stock Market Data Analysis
#Enhance your skills in data manipulation and analysis using tuples and loops.

#Problem Statement:
#You have been provided with stock market data, where each data point is a tuple containing a company's stock symbol, the date, and the 
# closing price. Your task is to analyze this data to find the average closing price of a specified stock over a given period.

#Sample Data:

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("MSFT", "2021-01-02", 225.0)
]

def average_stock_cost(stock_data, selected_stock):
    total_closing = 0
    count = 0
    for stock, _, closing_price in stock_data:
        if stock == selected_stock:
            total_closing += closing_price
            count += 1
    if count == 0:
        return "No data found for the selected stock."
    return total_closing / count
selected_stock = input("Enter the stock symbol you'd like to calculate: ").upper()
average_cost = average_stock_cost(stock_data, selected_stock)
print(f"Average cost for {selected_stock}: {average_cost}")
