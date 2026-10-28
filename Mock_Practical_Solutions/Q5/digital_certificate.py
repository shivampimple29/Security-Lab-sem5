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

# Signature generation: S = M^d mod n
message = int(input("\nEnter message M: "))

if message >= n:
    print("Message must be less than n.")
    raise SystemExit

signature = pow(message, d, n)

print("\n----- DIGITAL SIGNATURE -----")
print("Message =", message)
print("Digital Signature =", signature)

# Signature verification: M' = S^e mod n
received_signature = int(input("\nEnter signature S: "))
received_message = int(input("Enter message M: "))

verified_message = pow(received_signature, e, n)

print("\n----- SIGNATURE VERIFICATION -----")
print("Signature =", received_signature)
print("Message =", received_message)
print("Calculated M' =", verified_message)

if verified_message == received_message:
    print("The message is authenticate")
else:
    print("Message is altered, Discard.")