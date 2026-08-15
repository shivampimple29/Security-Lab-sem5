# RSA Encryption and Decryption
# Security Lab - Experiment 4

# Extended Euclidean Algorithm
def extended_euclidean_algorithm(first_number, second_number):
    if second_number == 0:
        return first_number, 1, 0

    greatest_common_divisor, first_coefficient, second_coefficient = (
        extended_euclidean_algorithm(
            second_number,
            first_number % second_number
        )
    )

    new_first_coefficient = second_coefficient
    new_second_coefficient = (
        first_coefficient
        - (first_number // second_number) * second_coefficient
    )

    return (
        greatest_common_divisor,
        new_first_coefficient,
        new_second_coefficient
    )


# ---------------- KEY GENERATION ----------------

prime_number_p = int(input("Enter prime number p: "))
prime_number_q = int(input("Enter prime number q: "))
public_exponent = int(input("Enter public key e: "))

# Calculate n = p × q
modulus_n = prime_number_p * prime_number_q

# Calculate phi(n) = (p - 1)(q - 1)
phi_n = (prime_number_p - 1) * (prime_number_q - 1)

# Check whether e and phi(n) are coprime
greatest_common_divisor, _, _ = extended_euclidean_algorithm(
    public_exponent,
    phi_n
)

if greatest_common_divisor != 1:
    print("Invalid value of e.")
    print("e and phi(n) must be coprime.")
    exit()

# Calculate d using Extended Euclidean Algorithm
_, private_exponent, _ = extended_euclidean_algorithm(
    public_exponent,
    phi_n
)

# Make d positive
private_exponent = private_exponent % phi_n

# Display keys
print("\n----- KEY GENERATION -----")
print("n =", modulus_n)
print("phi(n) =", phi_n)
print("Public Key  =", (public_exponent, modulus_n))
print("Private Key =", (private_exponent, modulus_n))


# ---------------- ENCRYPTION ----------------

plaintext_message = int(input("\nEnter message P: "))

if plaintext_message >= modulus_n:
    print("Message must be less than n.")
    exit()

# RSA Encryption Formula:
# C = P^e mod n
ciphertext_message = (
    plaintext_message ** public_exponent
) % modulus_n

print("\n----- ENCRYPTION -----")
print("Plaintext =", plaintext_message)
print("Ciphertext =", ciphertext_message)


# ---------------- DECRYPTION ----------------

# RSA Decryption Formula:
# P = C^d mod n
decrypted_message = (
    ciphertext_message ** private_exponent
) % modulus_n

print("\n----- DECRYPTION -----")
print("Ciphertext =", ciphertext_message)
print("Decrypted message =", decrypted_message)
