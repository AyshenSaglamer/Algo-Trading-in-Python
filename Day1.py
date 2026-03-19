# Day_1_Python_Basics/Day_1_Task_Basics_Of_Python_Mini_Project_1.ipynb

# 1.Write a Python print statement that shows a message saying, "Starting the trading session."
print("Starting the trading session.")
# 2.Create a variable stock_price that stores the current price of a stock as a floating-point number.
stock_price = 360.50
# 3.Assign the symbol AAPL to a variable named stock_symbol.
stock_symbol = "AAPL"
# 4.Add a comment explaining that the following code will initialize a trading balance variable with 10000.
# Initializing a trading balance variable with 10000
trading_balance = 10000
# 5.Identify and fix the syntax error in the following code snippet: total_return = final_price - initial_price print(total_return)
final_price = 450.25
initial_price = 400.67
total_return = final_price - initial_price
print(total_return)
# 6.Write a program that asks the user for the quantity of a stock to buy and prints "Buying X shares," where X is the input quantity.
quantity = input("What is the number of quantity of a stock to buy? ")
print("Buying " + quantity + " shares.")
# 7.Convert a string variable price_str holding the value "89.50" into a floating-point number.
price_str = "89.50"
price_float = float(price_str)
# 8.Define a list literal containing the stock symbols "AAPL", "TSLA", and "GOOGL".
stock_symbols = ["AAPL", "TSLA", "GOOGL"]
# 9.Write a print statement that outputs "Stock XYZ is trading at $PRICE", where XYZ is a variable symbol, and PRICE is a floating-point variable price.
stock = "GOOGL"
price = 1854.50
print("Stock " + stock + " is trading at " + "$" + str(price))
# 10.Write a Python Program print_trade_summary(symbol, quantity, price) that accepts a stock symbol, the number of shares, and the price per share. It should print out a formatted summary of the total trade cost.


def print_trade_summary(symbol, quantity, price):
    total_cost = quantity * price
    print("Stock Symbol: " + str(symbol))
    print("Quantity: " + str(quantity))
    print("Price per Share: " + "$" + str(price))
    print("Total Trade Cost: " + "$" + str(total_cost))

# 11. Calculate the Daily Return on Investment (ROI)


initial_price = float(input(" What is the purchase price of the stock?"))
final_price = float(input("What is the selling price of the stock?"))


def roi (initial_price, final_price):
    roi_cal = (final_price - initial_price) / initial_price
    return roi_cal


# 12. Determine the Average Price from User Inputs
price1 = float(input("Enter the first price: "))
price2 = float(input("Enter the second price: "))
price3 = float(input("Enter the third price: "))


def average_price(price1, price2, price3):
    average = (price1 + price2 + price3) / 3
    return average


# 13. Compare Two Stock Prices
price1 = float(input("What is the price of the first stock?"))
price2 = float(input("What is the price of the second stock?"))
if price1 > price2:
    print(price1)
elif price2 > price1:
    print(price2)
else:
    print("Both stock prices are equal.")

# 14. Break-Even Price Calculator


def break_even_price(total_cost, quantity):
    if quantity == 0:
        return "Quantity cannot be zero."
    break_even = total_cost / quantity
    return break_even
# 15. Display Stock Price Change
current_price = float(input("What is the today's stock price?"))
yesterday_price = float(input("What was the yesterday's stock price?"))
def display_stock_price(current_price, yesterday_price):
    change_price = current_price - yesterday_price
    return change_price

# 16. Calculate Required Margin

position_size = float(input("What is the position size?"))
leverage = float(input("What is the leverage?"))

def required_margin (position_size, leverage):
    required_margin_cal = position_size / leverage
    return required_margin_cal

# 17. Convert Currency from User Input

usd_dollar = float(input("What is the usd dollar amount?"))
conversion_rate = float(input("What is the conversion rate?"))

def converter(usd_dollar, conversion_rate):
    conversion_rate_cal = usd_dollar * conversion_rate
    return conversion_rate_cal

#18. Calculate the Weighted Average Price
average_cost = float(input("What is the average cost?"))
sum_quantity = float(input("What is the total number of quantity of shares?"))

def weighted_average_price(average_cost, sum_quantity):
    weighted_average_price_cal = average_cost/ sum_quantity
    return weighted_average_price_cal

#19. User Input to Adjust Stock Quantity

current_no_stock = float(input("What is the number of current number of stocks?"))
how_many_buy = float(input("How many number of stocks to buy?"))
how_many_sell = float(input("How many number of stocks to sell?"))
def total (current_no_stock, how_many_buy, how_many_sell):
     total = current_no_stock + how_many_buy - how_many_sell
     return total














