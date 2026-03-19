'''
Python Mini Project 1 :
Scenario: Stock Data Entry and Analysis Tool

Objective: Create a Python script that will involve taking manual input for stock prices over a week and will calculate the average price.
It should also demonstrate variable declaration, user input, and basic arithmetic using Python types.

'''
weekly_prices = []
for i in range(7):
    price_asking = float(input("What is the today's stock price?"))
    weekly_prices.append(price_asking)

total = sum(weekly_prices)
average = total/ len(weekly_prices)

print(total)
print(average)