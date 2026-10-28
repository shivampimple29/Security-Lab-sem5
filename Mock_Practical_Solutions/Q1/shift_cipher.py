def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    # Decrypt by shifting in the opposite direction
    return encrypt(text, -shift)


while True:
    print("\n===== SHIFT CIPHER MENU =====\n"
          "1. Encrypt Message\n"
          "2. Decrypt Message\n"
          "3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        message = input("Enter the message to encrypt: ")
        key = int(input("Enter shift key (number): "))
        print("Encrypted Result:", encrypt(message, key))

    elif choice == "2":
        message = input("Enter the secret message to decrypt: ")
        key = int(input("Enter the shift key (number): "))
        print("Decrypted Result:", decrypt(message, key))

    elif choice == "3":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")