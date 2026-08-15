# -----------------------------
# Step 1 : Store all alphabets
# -----------------------------
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXY"   # Y is omitted

# -----------------------------
# Step 2 : User Input for Keyword
# -----------------------------
keyword = input("Enter Keyword : ").upper()
keyword = keyword.replace("Z", "Y")

# -----------------------------
# Step 3 : User Input for Plaintext
# -----------------------------
plaintext = input("Enter Plain Text : ").upper()

# Remove spaces
plaintext = plaintext.replace(" ", "")

# Replace J with I
plaintext = plaintext.replace("Z", "Y")

# -----------------------------
# Step 4 : Split Plaintext into Pairs
# -----------------------------
pairs = []

index = 0

while index < len(plaintext):

    first = plaintext[index]

    if index + 1 == len(plaintext):
        second = "X"
        index += 1

    else:
        second = plaintext[index + 1]

        if first == second:
            second = "X"
            index += 1
        else:
            index += 2

    pairs.append(first + second)

print("\nPlaintext Pairs")
print(pairs)

# -----------------------------
# Step 5 : Generate 5x5 Matrix
# -----------------------------
matrix_string = ""

# Add keyword letters
for letter in keyword:
    if letter not in matrix_string and letter in alphabets:
        matrix_string += letter

# Add remaining alphabets
for letter in alphabets:
    if letter not in matrix_string:
        matrix_string += letter

# Create Matrix
matrix = []

position = 0

for row in range(5):

    current_row = []

    for column in range(5):
        current_row.append(matrix_string[position])
        position += 1

    matrix.append(current_row)

print("\nPlayfair Key Matrix\n")

for row in matrix:
    print(" ".join(row))


# -----------------------------
# Function : Find Position
# -----------------------------
def find_position(character):

    for row in range(5):
        for column in range(5):

            if matrix[row][column] == character:
                return row, column


# -----------------------------
# Step 6 : Encryption
# -----------------------------
encrypted_text = ""

for pair in pairs:

    first = pair[0]
    second = pair[1]

    row1, col1 = find_position(first)
    row2, col2 = find_position(second)

    # Same Row
    if row1 == row2:

        encrypted_text += matrix[row1][(col1 + 1) % 5]
        encrypted_text += matrix[row2][(col2 + 1) % 5]

    # Same Column
    elif col1 == col2:

        encrypted_text += matrix[(row1 + 1) % 5][col1]
        encrypted_text += matrix[(row2 + 1) % 5][col2]

    # Rectangle Rule
    else:

        encrypted_text += matrix[row1][col2]
        encrypted_text += matrix[row2][col1]

print("\nEncrypted Text :")
print(encrypted_text)


# -----------------------------
# Prepare Ciphertext Pairs
# -----------------------------
cipher_pairs = []

for i in range(0, len(encrypted_text), 2):
    cipher_pairs.append(encrypted_text[i:i + 2])


# -----------------------------
# Step 7 : Decryption
# -----------------------------
decrypted_text = ""

for pair in cipher_pairs:

    first = pair[0]
    second = pair[1]

    row1, col1 = find_position(first)
    row2, col2 = find_position(second)

    # Same Row
    if row1 == row2:

        decrypted_text += matrix[row1][(col1 - 1) % 5]
        decrypted_text += matrix[row2][(col2 - 1) % 5]

    # Same Column
    elif col1 == col2:

        decrypted_text += matrix[(row1 - 1) % 5][col1]
        decrypted_text += matrix[(row2 - 1) % 5][col2]

    # Rectangle Rule
    else:

        decrypted_text += matrix[row1][col2]
        decrypted_text += matrix[row2][col1]

print("\nDecrypted Text :")
print(decrypted_text)
