import random
import string

def generate_password(length):
    # Define the character set: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters from the character set
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt the user to input the desired password length
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 for security.")
            return
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
