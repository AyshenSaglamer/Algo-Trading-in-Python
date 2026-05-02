'''
Q1) Operators and Logical Expressions

You have a list of stock prices over 30 days. Write a logical expression that identifies whether there are consecutive price drops over three days or more.
For example, the sequence [120, 118, 115, 110] qualifies, but [120, 118, 120, 110] does not.
'''
# Logic --> price[i] > price[i+1] > price[i+2] > price[i+3]
prices = [120,118,115,110]
found = False  # This means it is not found yet.
for i in range(len(prices) - 3): # In python, range(1) means only index 0, in order i to be 0 and loop all the array.
if prices[i] > prices[i+1] and prices[i+1] > prices[i+2] and prices[i+2] > prices[i+3]:
        found = True
        break

print(found)
'''
Second Method:
prices = [120, 118, 115, 110]

result = any(
    prices[i] > prices[i+1] > prices[i+2] > prices[i+3]
    for i in range(len(prices) - 3)
)

print(result)
# any => ... and ... and ... and ... and
'''
'''
Q2) If - else statement

You are designing an algorithm to trade stocks. If the current price of a stock is above the 30-day moving average, print "Buy Signal"; 
otherwise, print "Sell Signal". Assume you have a list of daily prices and that the moving average can be calculated.
'''
def trading_signal(prices): # not enough data
    if len(prices) < 30:
        print("Not enough data to calculate moving average.")
        return

    moving_average = sum(prices[-30:]) / 30 # prices[-30:] slices the last 30 elements to compute the moving average
    # The -30 means "start 30 positions from the end of the list"
    # The : with nothing after it means "go all the way to the end"
    # So together, it grabs the last 30 elements
    current_price = prices[-1] # prices[-1] gets the most recent (current) price

    if current_price > moving_average:
        print("Buy Signal")
    else:
        print("Sell Signal")

# Example usage
daily_prices = [102, 105, 98, 110, 107, 103, 99, 115, 112, 108,
                106, 104, 109, 113, 111, 100, 97, 116, 120, 118,
                114, 119, 122, 117, 115, 121, 125, 123, 119, 130]

trading_signal(daily_prices)  # Output: Buy Signal (130 > 111.4)
'''
Q3) Modules (pandas)

Use the `pandas` library to load a CSV file containing historical trading data and calculate the daily percentage change of closing prices 
over a period of time.       
'''
'''
A CSV (Comma-Separated Values) file is a plain text file that stores data in a table format, where each line is a row and each value 
is separated by a comma.
Date,Open,High,Low,Close,Volume
2024-01-01,150.00,155.00,148.00,153.00,1000000
2024-01-02,153.00,158.00,151.00,156.50,1200000
2024-01-03,156.50,160.00,154.00,154.00,980000
'''
import pandas as pd # import the pandas library, but let me refer to it as pd instead of typing pandas every time.
# --- Load the CSV ---
df = pd.read_csv('trading_data.csv', parse_dates=['Date'])
'''
df -> A variable name — short for DataFrame (a table of rows & columns). You could name it anything, but df is the convention.
pd.read_csv(...) -> A pandas function that opens and reads a CSV file
'trading_data.csv'The name of the file to open (must be in the same folder as your script)
parse_dates=['Date']Tells pandas to treat the Date column as actual dates, not plain text
'''
df.sort_values('Date', inplace=True)
'''
df ->  The DataFrame (table) you loaded from the CSV 
.sort_values(...) ->  A pandas function that **sorts the rows** of the table 
'Date' -> The column to sort by — in this case, sort by date 
`inplace=True` -> **Modify the original** `df` directly, don't create a new one |

Why sort by date?
CSV files aren't always in order. Your data might look like this when loaded:
```
Date        Close
2024-01-03  154.00   ← out of order!
2024-01-01  153.00
2024-01-02  156.50
```

After `sort_values('Date')` it becomes:
```
Date        Close
2024-01-01  153.00   ← now in order ✓
2024-01-02  156.50
2024-01-03  154.00

What does inplace=True mean exactly?
# inplace=False (default) — creates a NEW sorted table, original unchanged
df_sorted = df.sort_values('Date')

# inplace=True — sorts the ORIGINAL df directly, no new variable needed
df.sort_values('Date', inplace=True)
Both achieve the same result — inplace=True just saves you creating an extra variable.
'''
df.set_index('Date', inplace=True)
'''
`df` -> Your DataFrame (table) 
`.set_index(...)` -> Makes a chosen column the **row label** (index) of the table 
`'Date'` -> The column to use as the index 
`inplace=True` -> Modify the original `df` directly 
'''
df['Daily_Pct_Change'] = df['Close'].pct_change() * 100
'''
df['Daily_Pct_Change']` -> Creates a **new column** in the table called `Daily_Pct_Change` 
`df['Close']` -> Grabs the existing `Close` column 
`.pct_change()` -> Calculates **how much each value changed** compared to the previous row as a decimal 
`* 100` -> Converts the decimal into a **percentage** 

**How `pct_change()` works row by row:**
```
Date        Close    pct_change()    * 100
2024-01-01  153.00   NaN             NaN       ← no previous row
2024-01-02  156.50   0.02288         2.288%    ← (156.50-153.00)/153.00
2024-01-03  154.00  -0.01597        -1.597%    ← (154.00-156.50)/156.50
        
'''
print(df[['Close', 'Daily_Pct_Change']].head(10))
 '''
df[['Close', 'Daily_Pct_Change']] -> Select only these two columns to display (double brackets = multiple columns)
.head(10) -> Show only the first 10 rows
print(...) -> Output the result to the screen

Why double brackets [[ ]]?
df['Close']            # single brackets → returns one column (a Series)
df[['Close', 'Daily_Pct_Change']]  # double brackets → returns multiple columns (a DataFrame)
'''
'''       
Q4) While Loop

Create a loop that repeatedly checks a stock price from a real-time source every 10 seconds until the stock falls below a threshold value. 
In this scenario, print `"Threshold Exceeded"` when the threshold is crossed.
'''
import requests # A library that lets your program talk to the internet — send HTTP requests and receive responses
import time # A library that lets you control timing in your program

def get_stock_price(symbol): # symbol -> A parameter — the stock ticker you pass in (e.g. "AAPL")
    """Fetch real-time stock price using Yahoo Finance API (free, no key needed).""" 
    '''
    """..."""A docstring — a description of what the function does. It is not executed. Python reads it but doesn't run it as code
    It's like a comment but specifically for documenting functions. You can even access it later with:
    print(get_stock_price.__doc__)
# Output: Fetch real-time stock price using Yahoo Finance API (free, no key needed).
    '''
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
    '''
     f"..." -> An f-string — embeds variables inside text
     {symbol}Gets replaced by the actual stock ticker passed in
# If symbol = "AAPL"
url → "https://query1.finance.yahoo.com/v8/finance/chart/AAPL"

# If symbol = "TSLA"
url → "https://query1.finance.yahoo.com/v8/finance/chart/TSLA"         
'''
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
'''
        requests.get(url) -> Visits the URL and fetches the data from Yahoo Finance
        headers={...} -> Extra information sent along with the request
        "User-Agent": "Mozilla/5.0"Tells Yahoo the request is coming from a real browser, not a bot
        response -> Stores the raw reply from Yahoo's server
'''
    data = response.json()
'''
response-> The raw reply from Yahoo's server (looks like plain text)
.json() -> Converts that raw text into a Python dictionary you can navigate
'''
    price = data['chart']['result'][0]['meta']['regularMarketPrice']
'''
 Extract the price from the dictionary:
 Remember data is a nested dictionary (like folders inside folders). You navigate it using ['key'] at each level:
pythondata
 └── ['chart']                    # go into 'chart' folder
      └── ['result']              # go into 'result' folder
           └── [0]                # grab the FIRST item in the list
                └── ['meta']      # go into 'meta' folder
                     └── ['regularMarketPrice']  # grab the price ✓
'''
    return price

def monitor_stock(symbol, threshold):
    """Check stock price every 10 seconds until it falls below threshold."""
    print(f"Monitoring {symbol} | Threshold: ${threshold}")
    print("-" * 40)

    while True:
        price = get_stock_price(symbol)
        print(f"Current price: ${price:.2f}")

        if price < threshold:
            print("Threshold Exceeded")  # price dropped below threshold
            break                        # stop the loop

        time.sleep(10)   # wait 10 seconds before checking again

# --- Run it ---
monitor_stock("AAPL", threshold=180.00)
```
'''
**Example Output:**
```
Monitoring AAPL | Threshold: $180.00
----------------------------------------
Current price: $184.50
Current price: $182.10
Current price: $179.80
Threshold Exceeded
'''
'''
Q5)For Loop
You have data on the opening and closing prices of multiple stocks in a portfolio.
Using a for loop, calculate and print the total daily gain or loss for each stock in the portfolio.
'''
# Portfolio data — list of dictionaries, one per stock
portfolio = [
    {"symbol": "AAPL", "open": 150.00, "close": 155.00},
    {"symbol": "TSLA", "open": 200.00, "close": 192.00},
    {"symbol": "GOOG", "open": 130.00, "close": 133.50},
    {"symbol": "AMZN", "open": 175.00, "close": 170.00},
    {"symbol": "MSFT", "open": 310.00, "close": 318.00},
]

# Loop through each stock and calculate gain/loss
for stock in portfolio:
    symbol = stock["symbol"]
    open_price  = stock["open"]
    close_price = stock["close"]

    daily_change = close_price - open_price   # gain if positive, loss if negative

    if daily_change > 0:
        result = "Gain"
    elif daily_change < 0:
        result = "Loss"
    else:
        result = "No Change"

    print(f"{symbol}: {result} of ${abs(daily_change):.2f}")
```
'''
**Output:**
```
AAPL: Gain of $5.00
TSLA: Loss of $8.00
GOOG: Gain of $3.50
AMZN: Loss of $5.00
MSFT: Gain of $8.00
'''
'''
Q6) Nested Loops

Create a nested loop that simulates a simple market-making strategy by placing buy and sell orders over a range of prices and volumes. 
Assume bid prices range from 90 to 100 and ask prices range from 101 to 110.
'''
# Define price and volume ranges
bid_prices = range(90, 101)    # 90, 91, 92, ... 100
ask_prices = range(101, 111)   # 101, 102, 103, ... 110
volumes    = [10, 20, 30]      # order sizes in units

# Nested loop — simulate placing orders
for bid in bid_prices:
    for ask in ask_prices:
        for volume in volumes:
            spread = ask - bid
            profit = spread * volume

            print(f"BUY  @ ${bid} | SELL @ ${ask} | "
                  f"Volume: {volume} | Spread: ${spread} | Profit: ${profit}")
```
'''
The goal of market making is to find all possible order combinations. 
You don't just want one bid with one ask — you want to simulate every bid paired with every ask at every volume.

Think of it like a multiplication table:
          ask=101  ask=102  ask=103 ... ask=110
bid=90  |   ✓        ✓        ✓           ✓
bid=91  |   ✓        ✓        ✓           ✓
bid=92  |   ✓        ✓        ✓           ✓
  ...
bid=100 |   ✓        ✓        ✓           ✓
Every ✓ is a possible order. A single loop could only go across one row or one column — not fill the whole table. 
Nested loops fill every cell.

Why 3 loops specifically?
Because we have 3 variables that each need to cycle through all their values.
'''
'''
**Output (sample):**
```
BUY  @ $90 | SELL @ $101 | Volume: 10 | Spread: $11 | Profit: $110
BUY  @ $90 | SELL @ $101 | Volume: 20 | Spread: $11 | Profit: $220
BUY  @ $90 | SELL @ $101 | Volume: 30 | Spread: $11 | Profit: $330
BUY  @ $90 | SELL @ $102 | Volume: 10 | Spread: $12 | Profit: $120
...
'''
'''
7. Complex If-Else Logic

You have a complex trading rule where a `"Strong Buy"` signal is given if the stock price is above both the 30-day and 50-day moving averages, 
a `"Buy"` signal is given if only above the 30-day, a `"Hold"` signal if above the 50-day, and a `"Sell"` signal otherwise. 
Calculate the signals assuming you have daily prices for at least 50 days.
'''
# Sample daily prices (50+ days)
daily_prices = [
    120, 122, 119, 125, 128, 130, 127, 123, 121, 118,
    115, 117, 120, 124, 126, 129, 131, 135, 132, 128,
    125, 122, 120, 118, 121, 124, 127, 130, 133, 136,
    138, 135, 132, 129, 126, 124, 127, 130, 134, 137,
    140, 138, 135, 132, 130, 128, 131, 134, 137, 140,
    143   # ← current price (day 51)
]
avg_30days = sum(daily_prices[-30:])/30 # Average of last 30 days
avg_50days = sum(daily_prices[-50:]/50 # Average of last 50 days
current_price = daily_prices[-1]

if current_price > avg_30days and current_price > avg_50days:
            signal =  "Strong Buy"
elif current_price > avg_30days:
            signal = "Buy"
elif current_price > avg_50days:
            signal = "Hold"
else:
            signal = "Sell"
print(f"Current Price: ${current_price}")
print(f"30 Days Moving Averages: ${avg_30days}")
print(f"50 Days Moving Averages: ${avg_50days}")
print(f"Signal: ${signal}")

'''
Q8. Modules (numpy)

Use the `numpy` module to calculate the rolling average for a window of 5 days over a numpy array containing 20 stock prices.
'''
import numpy as np
prices = np.array([
    120, 122, 119, 125, 128,
    130, 127, 123, 121, 118,
    115, 117, 120, 124, 126,
    129, 131, 135, 132, 128
])
'''
Converts a Python list into a numpy array
Why numpy? Numpy arrays are faster and support mathematical operations directly
'''
window = 5 # Calculate 5-day rolling average
rolling_avg = np.convolve(prices, np.ones(window) / window, mode = "valid")
'''
np.ones(window) — creates an array of ones:
np.ones(5)  →  [1, 1, 1, 1, 1]
np.ones(window)/window — divides each one by 5:
np.ones(5)/5  →  [0.2, 0.2, 0.2, 0.2, 0.2]   # each weight = 1/5
This creates equal weights — each of the 5 days contributes equally to the average.
np.convolve() — slides the weights across the prices:
# For the first window (days 1-5):
[120, 122, 119, 125, 128] × [0.2, 0.2, 0.2, 0.2, 0.2]
= (120×0.2) + (122×0.2) + (119×0.2) + (125×0.2) + (128×0.2)
= 24 + 24.4 + 23.8 + 25 + 25.6
= 122.80 ✓
mode='valid' — only returns results where the full window fits:
'''
# Print results
print("Day  Price   5-Day Rolling Avg")
print("-" * 32)

for i, avg in enumerate(rolling_avg):
    day = i + window          # first valid average starts at day 5
    price = prices[day - 1]   # corresponding price
    print(f"{day:>3}  ${price:>5}   ${avg:.2f}")
'''
enumerate() -> Returns both the index and value of each item together
i->The position (0, 1, 2, 3...)
{day:>3}Print day number, right-aligned in 3 characters wide
{price:>5}Print price, right-aligned in 5 characters wide
{avg:.2f}Print average rounded to 2 decimal places
'''
'''
Q9. Optimization with Loops**

Calculate the best day to buy and the best day to sell to maximize profit within a list of daily prices using a single pass of nested loops.
'''
'''
Q10. Scenario Analysis

Given that a certain algorithm follows a strategy where every time a stock gains 5% in value from the last recorded price, 
the program places a sell order. Track the hypothetical prices over 15 days and identify when sell orders should be triggered.
'''
