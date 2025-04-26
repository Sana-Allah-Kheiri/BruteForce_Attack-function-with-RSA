def left_shift_word(word, n):
    if len(word) <= 1 or not word.isalpha():
        return word
    n = n % len(word)  # Ensure n is within word length
    return word[n:] + word[:n]

def encrypt_word(word):
    alpha_only = ''.join(filter(str.isalpha, word))
    length = len(alpha_only)

    if length == 1:
        shift = 0
    elif length == 2:
        shift = 1
    elif length == 3:
        shift = 2
    elif length == 4:
        shift = 1
    else:
        shift = 3

    return left_shift_word(word, shift)

def encrypt_text(text):
    words = text.split()
    encrypted_words = [encrypt_word(word) for word in words]
    return ' '.join(encrypted_words)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def brute_force_rsa(n, e):
    print("\n--- Simulating RSA Brute-Force Attack ---")
    for i in range(2, n):
        if n % i == 0:
            p = i
            q = n // i
            if p * q == n:
                print(f"Found factors: p = {p}, q = {q}")
                phi = (p - 1) * (q - 1)
                d = modinv(e, phi)
                if d:
                    print(f"Recovered private key d = {d}")
                    return d
    print("Failed to factor modulus. Attack unsuccessful.")
    return None

def main():
    print("--- Custom Encryption Program ---")
    text = input("Enter the plain text: ")
    encrypted = encrypt_text(text)
    print("Encrypted text:", encrypted)

    # Example RSA values for testing
    n = 55  # Public modulus (product of two primes)
    e = 3   # Public exponent
    brute_force_rsa(n, e)

if __name__ == "__main__":
    main()