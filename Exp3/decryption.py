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


cipher = input("Enter Cipher Text: ").replace(" ", "").upper()
key = input("Enter Key: ").upper()

blockSize = len(key)

cipherBlocks = []
keyBlocks = []
plainBlocks = []

for startIndex in range(0, len(cipher), blockSize):
    cipherBlock = cipher[startIndex:startIndex + blockSize]

    keyBlock = key[:len(cipherBlock)]
    plainBlock = decrypt(cipherBlock, key)

    cipherBlocks.append(cipherBlock)
    keyBlocks.append(keyBlock)
    plainBlocks.append(plainBlock)

print("\nCipher :", " ".join(cipherBlocks))
print("Key    :", " ".join(keyBlocks))
print("Plain  :", " ".join(plainBlocks))

plainText = "".join(plainBlocks)
print("\nDecrypted Text:", plainText)