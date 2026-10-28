alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is omitted

keyword = input("Enter Keyword : ").upper().replace("J", "I")
plaintext = input("Enter Plain Text : ").upper().replace(" ", "").replace("J", "I")

# Split plaintext into pairs
pairs = []
index = 0

while index < len(plaintext):
    first = plaintext[index]

    if index + 1 == len(plaintext) or first == plaintext[index + 1]:
        second = "X"
        index += 1
    else:
        second = plaintext[index + 1]
        index += 2

    pairs.append(first + second)

print("\nPlaintext Pairs")
print(pairs)

# Build the key matrix using unique letters
matrix_string = ""

for letter in keyword + alphabets:
    if letter in alphabets and letter not in matrix_string:
        matrix_string += letter

matrix = [list(matrix_string[i:i + 5]) for i in range(0, 25, 5)]

print("\nPlayfair Key Matrix\n")
for row in matrix:
    print(" ".join(row))


def find_position(character):
    for row in range(5):
        for column in range(5):
            if matrix[row][column] == character:
                return row, column


# Use shift 1 for encryption and -1 for decryption
def transform(pairs, shift):
    result = ""

    for first, second in pairs:
        row1, col1 = find_position(first)
        row2, col2 = find_position(second)

        if row1 == row2:  # Same row
            result += matrix[row1][(col1 + shift) % 5]
            result += matrix[row2][(col2 + shift) % 5]

        elif col1 == col2:  # Same column
            result += matrix[(row1 + shift) % 5][col1]
            result += matrix[(row2 + shift) % 5][col2]

        else:  # Rectangle rule
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result


encrypted_text = transform(pairs, 1)
print("\nEncrypted Text :")
print(encrypted_text)

cipher_pairs = [
    encrypted_text[i:i + 2]
    for i in range(0, len(encrypted_text), 2)
]

decrypted_text = transform(cipher_pairs, -1)
print("\nDecrypted Text :")
print(decrypted_text)