# CODSOFT TASK 3: PASSWORD GENERATOR
# Developed by: Piyush Patel

import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=== PASSWORD GENERATOR ===")
try:
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid number.")
