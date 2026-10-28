def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


print("----- Diffie-Hellman Key Exchange -----")

# Public parameters
q = int(input("Enter prime number q: "))
alpha = int(input("Enter primitive root alpha: "))

if not is_prime(q):
    print("Error: q must be a prime number.")
    raise SystemExit

if not 1 < alpha < q:
    print("Error: alpha must satisfy 1 < alpha < q.")
    raise SystemExit

# Private keys
xa = int(input("Enter Alice's private key XA: "))
xb = int(input("Enter Bob's private key XB: "))

if not 1 <= xa < q:
    print("Error: Alice's private key XA must be smaller than q.")
    raise SystemExit

if not 1 <= xb < q:
    print("Error: Bob's private key XB must be smaller than q.")
    raise SystemExit

# Public keys: Y = alpha^X mod q
ya = pow(alpha, xa, q)
yb = pow(alpha, xb, q)

# Shared keys: K = other person's public key ^ own private key mod q
ka = pow(yb, xa, q)
kb = pow(ya, xb, q)

print("\n----- Alice -----")
print("Private Key (XA):", xa)
print("Public Key (YA):", ya)

print("\n----- Bob -----")
print("Private Key (XB):", xb)
print("Public Key (YB):", yb)

print("\n----- Shared Secret -----")
print("Alice's Shared Key:", ka)
print("Bob's Shared Key  :", kb)

if ka == kb:
    print("\nShared key successfully established.")
else:
    print("\nError: Shared keys do not match.")