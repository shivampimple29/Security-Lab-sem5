# direction: 1 for encryption, -1 for decryption
def transform(text, key, direction):
    result = ""

    for i, character in enumerate(text):
        letter = ord(character) - ord("A")
        shift = ord(key[i % len(key)]) - ord("A")
        result += chr((letter + direction * shift) % 26 + ord("A"))

    return result


print("1. Encrypt and decrypt")
print("2. Decrypt only")
choice = input("Enter choice (1-2): ")

if choice not in ("1", "2"):
    raise SystemExit("Invalid choice.")

text = input("Enter text: ").replace(" ", "").upper()
key = input("Enter Key: ").upper()

if not key:
    raise SystemExit("Key cannot be empty.")

blockSize = len(key)
direction = 1 if choice == "1" else -1

textBlocks = []
keyBlocks = []
resultBlocks = []

# Split into blocks, match the key, and process each block
for start in range(0, len(text), blockSize):
    block = text[start:start + blockSize]

    textBlocks.append(block)
    keyBlocks.append(key[:len(block)])
    resultBlocks.append(transform(block, key, direction))

result = "".join(resultBlocks)

if choice == "1":
    print("\nPlain :", " ".join(textBlocks))
    print("Key   :", " ".join(keyBlocks))
    print("Cipher:", " ".join(resultBlocks))

    print("\nEncrypted Text:", result)
    print("Decrypted Text:", transform(result, key, -1))

else:
    print("\nCipher :", " ".join(textBlocks))
    print("Key    :", " ".join(keyBlocks))
    print("Plain  :", " ".join(resultBlocks))

    print("\nDecrypted Text:", result)