def encrypt(text, key):
    cipher = ""
    key = key.upper()
    keyIndex = 0

    for character in text:
        if character == " ":
            cipher += " "
            continue

        plain = ord(character.upper()) - ord("A")
        keyCharacter = ord(key[keyIndex % len(key)]) - ord("A")

        encrypted = (plain + keyCharacter) % 26
        cipher += chr(encrypted + ord("A"))

        keyIndex += 1

    return cipher


def decrypt(cipher, key):
    text = ""
    key = key.upper()
    keyIndex = 0

    for character in cipher:
        if character == " ":
            text += " "
            continue

        c = ord(character.upper()) - ord('A')
        k = ord(key[keyIndex % len(key)]) - ord('A')
        p = (c - k) % 26

        text += chr(p + ord('A'))
        keyIndex += 1

    return text


plain = input("Enter Plain Text: ").replace(" ", "").upper()
key = input("Enter Key: ").upper()

blockSize = len(key)

plainBlocks = []
keyBlocks = []
cipherBlocks = []

for startIndex in range(0, len(plain), blockSize):
    plainBlock = plain[startIndex:startIndex + blockSize]

    # Match the key length to the current block
    keyBlock = key[:len(plainBlock)]

    cipherBlock = encrypt(plainBlock, key)

    plainBlocks.append(plainBlock)
    keyBlocks.append(keyBlock)
    cipherBlocks.append(cipherBlock)

print("\nPlain :", " ".join(plainBlocks))
print("Key   :", " ".join(keyBlocks))
print("Cipher:", " ".join(cipherBlocks))

cipherText = "".join(cipherBlocks)
decryptedText = decrypt(cipherText, key)

print("\nEncrypted Text:", cipherText)
print("Decrypted Text:", decryptedText)