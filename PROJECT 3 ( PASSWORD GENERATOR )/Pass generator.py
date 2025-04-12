# password_generator.py

import random
import string

def generate_password(length, use_uppercase, use_digits, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "⚠️ No character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!\n")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("❌ Length should be a positive number.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_digits, use_symbols)
    print(f"\n🔑 Your generated password: {password}")

if __name__ == "__main__":
    main()
