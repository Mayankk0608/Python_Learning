size_prices = {'R': 100, 'M': 120, 'L': 140}
base_prices = {'T': 60, 'A': 70, 'D': 90}
cheese_prices = {'C': 50, 'E': 80}

print("Choose the size for your pizza:\nEnter 'R' for regular, 'M' for medium, 'L' for large")
s = input("Enter the size for pizza: ").upper()
print("\n")

print("Choose the base for your pizza:\nEnter 'T' for thin, 'A' for medium, 'D' for thick")
b = input("Enter the base for pizza: ").upper()
print("\n")

print("Choose cheese for your pizza:\nEnter 'E' for extra cheese, 'C' for regular cheese")
ch = input("Enter the cheese for pizza: ").upper()
print("\n")

if s in size_prices and b in base_prices and ch in cheese_prices:
    print(f"You chose a {s} size pizza which costs {size_prices[s]}")
    print(f"With a {b} base which costs {base_prices[b]}")
    print(f"With {ch} cheese which costs {cheese_prices[ch]}")
    
    total_bill = size_prices[s] + base_prices[b] + cheese_prices[ch]
    print(f"Your total bill is: {total_bill}")
else:
    print("Invalid choice. Please enter valid options.")