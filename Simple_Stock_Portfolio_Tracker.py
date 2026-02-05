stocks = {"AAPL": 180, "TSLA": 250}
total = 0

while True:
    name = input("Enter stock name (or DONE): ").upper()

    if name == "DONE":
        break

    if name in stocks:
        qty = int(input("Enter quantity: "))
        total = total + (stocks[name] * qty)
    else:
        print("Stock not found")

print("\nTotal Investment =", total)