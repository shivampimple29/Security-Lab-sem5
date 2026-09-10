def is_prime(number):
    """Return True if the given number is prime."""
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True

def calculate_public_key(generator, private_key, prime_number):
    """Calculate public key: Y = alpha^X mod q."""
    return pow(generator, private_key, prime_number)


def calculate_shared_key(public_key, private_key, prime_number):
    """Calculate shared secret: K = Y_other^X mod q."""
    return pow(public_key, private_key, prime_number)


print("----- Diffie-Hellman Key Exchange -----")

# Input global public parameters
prime_number = int(input("Enter prime number q: "))
generator = int(input("Enter primitive root alpha: "))

# Validate q
if not is_prime(prime_number):
    print("Error: q must be a prime number.")
    exit()

# Validate alpha
if generator <= 1 or generator >= prime_number:
    print("Error: alpha must satisfy 1 < alpha < q.")
    exit()

# Input private keys
alice_private_key = int(input("Enter Alice's private key XA: "))
bob_private_key = int(input("Enter Bob's private key XB: "))

# Validate private keys
if not (1 <= alice_private_key < prime_number):
    print("Error: Alice's private key XA must be smaller than q.")
    exit()

if not (1 <= bob_private_key < prime_number):
    print("Error: Bob's private key XB must be smaller than q.")
    exit()

# Calculate public keys
alice_public_key = calculate_public_key(
    generator,
    alice_private_key,
    prime_number
)

bob_public_key = calculate_public_key(
    generator,
    bob_private_key,
    prime_number
)

# Calculate shared secret keys
alice_shared_key = calculate_shared_key(
    bob_public_key,
    alice_private_key,
    prime_number
)

bob_shared_key = calculate_shared_key(
    alice_public_key,
    bob_private_key,
    prime_number
)

# Display results
print("\n----- Alice -----")
print("Private Key (XA):", alice_private_key)
print("Public Key (YA):", alice_public_key)

print("\n----- Bob -----")
print("Private Key (XB):", bob_private_key)
print("Public Key (YB):", bob_public_key)

print("\n----- Shared Secret -----")
print("Alice's Shared Key:", alice_shared_key)
print("Bob's Shared Key  :", bob_shared_key)

# Verify shared key
if alice_shared_key == bob_shared_key:
    print("\nShared key successfully established.")
else:
    print("\nError: Shared keys do not match.")
