# Function to try a specific shift key backward
def decrypt_with_key(text, shift):
    result = ""

    # Loop through each letter in the encrypted text
    for char in text:
        if char.isupper():
            # Shift backward for uppercase
            result += chr((ord(char) - 65 - shift) % 26 + 65)

        elif char.islower():
            # Shift backward for lowercase
            result += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            # Keep spaces and punctuation unchanged
            result += char

    return result


# Get the encrypted message from the user
cipher_text = input("Enter the encrypted message to crack: ")

print("\n--- Trying all 26 possible keys ---")

# Loop through every possible key from 0 to 25
for key in range(26):
    guessed_text = decrypt_with_key(cipher_text, key)

    # Print the decrypted text for the current key
    print(f"Key {key:2d}: {guessed_text}")
