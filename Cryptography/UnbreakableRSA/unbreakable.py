from Crypto.Util.number import getPrime, bytes_to_long

def encrypt_message(message, N, e):
    """Encrypt a message using RSA public key."""
    # Convert the message to a number
    m = bytes_to_long(message.encode('utf-8'))
    
    # Encrypt the number using RSA: c = m^e mod N
    c = pow(m, e, N)
    
    return c

# Generate two large 2048-bit prime numbers for p and q
p = getPrime(2048)
q = getPrime(2048)
#print(p)
#print(q)
# Compute N (the modulus)
N = p * q

# RSA public exponent (common value)
e = 65537

# Message to encrypt
message = "flag{f4k3_fl4g}"

# Encrypt the message
ciphertext = encrypt_message(message, N, e)

# Print the encrypted message (ciphertext)
print(f"Encrypted Ciphertext: {ciphertext}")
print(f"Public Key (N, e): ({N}, {e})")
print(f"sum of prime : {p+q}")
