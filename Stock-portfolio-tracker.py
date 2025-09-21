# Stock Portfolio Tracker

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("📊 Welcome to Stock Portfolio Tracker 📊")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Enter 'done' when you are finished adding stocks.\n")

# Step 2: Get user input for stocks
while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("⚠ Stock not found! Please enter a valid stock name.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
    except ValueError:
        print("⚠ Please enter a valid number.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Step 3: Calculate total investment
print("\n📌 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock}: {qty} × ${price} = ${value}")

print(f"\n💰 Total Investment: ${total_investment}")

# Step 4: Optional - Save to file
save = input("\nDo you want to save this portfolio? (y/n): ").lower()
if save == "y":
    file_name = "portfolio.csv"
    with open(file_name, "w") as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock},{qty},{stock_prices[stock]},{qty * stock_prices[stock]}\n")
        f.write(f"Total Investment,,,{total_investment}\n")
    print(f"✅ Portfolio saved to {file_name}")