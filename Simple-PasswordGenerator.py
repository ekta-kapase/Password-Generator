#Code by Ekta Kapase

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
ip_letters= int(input("How many letters would you like in your password?\n")) 
ip_symbols = int(input(f"How many symbols would you like?\n"))
ip_numbers = int(input(f"How many numbers would you like?\n"))


r_letters = random.choices(letters,weights=None, cum_weights=None, k = ip_letters)
r_letters = ''.join(r_letters)

r_symbols = random.choices(symbols,weights=None, cum_weights=None, k = ip_symbols)
r_symbols = ''.join(r_symbols)

r_numbers = random.choices(numbers,weights=None, cum_weights=None, k = ip_numbers)
r_numbers = ''.join(r_numbers)

print(f"{r_letters}{r_symbols}{r_numbers}")
