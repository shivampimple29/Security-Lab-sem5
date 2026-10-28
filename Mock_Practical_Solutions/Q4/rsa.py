# Extended Euclidean Algorithm
def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x, y = extended_euclidean_algorithm(b, a % b)
    return gcd, y, x - (a // b) * y


# Key generation
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
e = int(input("Enter public key e: "))

n = p * q
phi = (p - 1) * (q - 1)

# One call gives both the GCD and the coefficient needed for d
gcd, d, _ = extended_euclidean_algorithm(e, phi)

if gcd != 1:
    print("Invalid value of e.")
    print("e and phi(n) must be coprime.")
    raise SystemExit

d %= phi

print("\n----- KEY GENERATION -----")
print("n =", n)
print("phi(n) =", phi)
print("Public Key  =", (e, n))
print("Private Key =", (d, n))

# Encryption: C = P^e mod n
message = int(input("\nEnter message P: "))

if message >= n:
    print("Message must be less than n.")
    raise SystemExit

cipher = pow(message, e, n)

print("\n----- ENCRYPTION -----")
print("Plaintext =", message)
print("Ciphertext =", cipher)

# Decryption: P = C^d mod n
decrypted = pow(cipher, d, n)

print("\n----- DECRYPTION -----")
print("Ciphertext =", cipher)
print("Decrypted message =", decrypted)