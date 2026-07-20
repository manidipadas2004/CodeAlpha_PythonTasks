stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 135,
    "MSFT": 330
}

portfolio = {}
total_investment = 0

print("Welcome to Stock Portfolio Tracker")
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock symbol. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

print("\nYour Portfolio Summary:")
print("-" * 30)

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"{stock} - Quantity: {quantity}, Price: ${stock_prices[stock]}, Total: ${investment}")

print("-" * 30)
print(f"Total Investment Value: ${total_investment}")

save_choice = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if save_choice == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-" * 30 + "\n")
        for stock, quantity in portfolio.items():
            investment = stock_prices[stock] * quantity
            file.write(f"{stock} - Quantity: {quantity}, Price: ${stock_prices[stock]}, Total: ${investment}\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total Investment Value: ${total_investment}\n")

    print("Portfolio summary saved successfully as portfolio_summary.txt")
else:
    print("Summary not saved.")