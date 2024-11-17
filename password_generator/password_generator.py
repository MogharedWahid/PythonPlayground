import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

your_password = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for i in range(0, nr_letters):
    random_letter = random.choice(letters)
    your_password.append(random_letter)

for i in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    your_password.append(random_symbol)

for i in range(0, nr_numbers):
    random_number = random.choice(numbers)
    your_password.append(random_number)

# Easy Version (Generate the password in sequence. Letters, then symbols, then numbers.)
output_password = ''.join(your_password)
# print(your_password)
print(f"Your password is: {output_password} (easy version)")

# Hard Version (The final password does not follow a pattern)
random.shuffle(your_password)
output_password = ''.join(your_password)
# print(your_password)
print(f"Your password is: {output_password} (hard version)")
