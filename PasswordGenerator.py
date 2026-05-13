import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("My name is Anton and I am here to help you create a strong and random password")
print("I am going to ask you to give me some parameters to help me create your password")
nr_letters = int(input("\033[91m"+"How many letters would you like in your password?"+"\033[0m"))
nr_symbols = int(input("\033[91m"+"How many symbols would you like?"+"\033[0m"))
nr_numbers = int(input("\033[91m"+"How many numbers would you like?"+"\033[0m"))
password =[]
if nr_letters<=0 or nr_symbols<=0 or nr_numbers<=0:
    print("Invalid input, please try again")
    exit()
for i in range(nr_letters):
    random_letter = random.choice(letters)
    password.append(random_letter)
for x in range(nr_symbols):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)
for y in range(nr_numbers):
    random_number = random.choice(numbers)
    password.append(random_number)

random.shuffle(password)
your_password = "".join(password)
print("\033[92m"+f"Your password is: {your_password}"+"\033[0m")



