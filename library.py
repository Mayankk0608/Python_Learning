import random

# Create lists for alphabets, numbers, and symbols
alphabets = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!@#$%^&*()-_=+[{]}|;:,.<>?/')

# Get user input for how many of each type is required in the password
num_alphabets = int(input("How many alphabets do you want in your password? "))
num_numbers = int(input("How many numbers do you want in your password? "))
num_symbols = int(input("How many symbols do you want in your password? "))

# Generate random alphabets, numbers, and symbols
password_letters = random.choices(alphabets, k=num_alphabets)
password_numbers = random.choices(numbers, k=num_numbers)
password_symbols = random.choices(symbols, k=num_symbols)

# Combine the characters into one list
password_list = password_letters + password_numbers + password_symbols

# Shuffle the combined list to make the password order random
random.shuffle(password_list)

# Join the list into a single string (password)
password = ''.join(password_list)

# Output the generated password
print(f"Your randomly generated password is: {password}")
