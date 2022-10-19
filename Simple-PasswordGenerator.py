#Code by Ekta Kapase

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
ip_letters = int(input("How many letters would you like in your password?\n")) 
ip_symbols = int(input("How many symbols would you like?\n"))
ip_numbers = int(input("How many numbers would you like?\n"))

r_letters = random.sample(letters, ip_letters)

r_symbols = random.sample(symbols, ip_symbols)

r_numbers = random.sample(numbers, ip_numbers)

r_pass = r_letters + r_symbols + r_numbers
r_pass = ''.join(r_pass)

print(f"Your password is {r_pass}")
