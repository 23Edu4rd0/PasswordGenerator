import random

# List of letters, numbers, and symbols to be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")





while True :
    # Initialize the password list
    password_list = []

    choice = int(input("What type o password do you want? 1 - Simple | 2 - Hard : \n"))

    if choice == 1 :
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))
        for _ in range(nr_letters):
            password_list.append(random.choice(letters))

        for _ in range(nr_numbers):
            password_list.append(random.choice(numbers))

        random.shuffle(password_list)

        password = ""

        for char in password_list:
            password += char

        print(f"Your password is: {password}")
        exit()


    elif choice == 2 :
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))

        # Add the specified number of letters to the password list
        for _ in range(nr_letters):
            password_list.append(random.choice(letters))

        # Add the specified number of numbers to the password list
        for _ in range(nr_numbers):
            password_list.append(random.choice(numbers))

        # Add the specified number of symbols to the password list
        for _ in range(nr_symbols):
            password_list.append(random.choice(symbols))

        # Shuffle the password list to ensure randomness
        random.shuffle(password_list)

        password = ""

        # Convert the password list to a string
        for char in password_list:
            password += char

        print(f"Your password is: {password}")
        exit()

    else:
        print("Type a valid option. 1 or 2")

