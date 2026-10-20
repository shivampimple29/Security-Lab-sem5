# Function to encrypt text using a shift key
def encrypt(text, shift):
    result = ""

    # Loop through each letter in the text
    for char in text:
        # Check if the letter is uppercase
        if char.isupper():
            # Shift the uppercase letter and wrap around A-Z
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        # Check if the letter is lowercase
        elif char.islower():
            # Shift the lowercase letter and wrap around a-z
            result += chr((ord(char) - 97 + shift) % 26 + 97)

        # If it is a space, number, or punctuation, keep it as it is
        else:
            result += char

    return result


# Function to decrypt text using a shift key
def decrypt(text, shift):
    result = ""

    # Loop through each letter in the secret text
    for char in text:
        # Check if the letter is uppercase
        if char.isupper():
            # Shift backward and wrap around A-Z
            result += chr((ord(char) - 65 - shift) % 26 + 65)

        # Check if the letter is lowercase
        elif char.islower():
            # Shift backward and wrap around a-z
            result += chr((ord(char) - 97 - shift) % 26 + 97)

        # If it is a space, number, or punctuation, keep it as it is
        else:
            result += char

    return result


# Display the menu repeatedly until the user chooses to exit
while True:

    # Display the available options
    print("\n===== SHIFT CIPHER MENU =====")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    # Ask the user to choose an option
    choice = input("Enter your choice (1-3): ")

    # Perform encryption
    if choice == "1":

        # Ask the user for the text and the shift key
        user_message = input("Enter the message to encrypt: ")
        user_key = int(input("Enter shift key (number): "))

        # Run the encryption function and print the secret message
        cipher_text = encrypt(user_message, user_key)
        print("Encrypted Result:", cipher_text)

    # Perform decryption
    elif choice == "2":

        # Ask the user for the secret text and the original shift key
        secret_message = input("Enter the secret message to decrypt: ")
        user_key = int(input("Enter the shift key (number): "))

        # Run the decryption function and print the original message
        plain_text = decrypt(secret_message, user_key)
        print("Decrypted Result:", plain_text)

    # Exit the program
    elif choice == "3":
        print("Exiting the program...")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
