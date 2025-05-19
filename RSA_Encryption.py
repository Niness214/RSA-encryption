import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclidean_algorithm(a,b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def mod_inverse(e, phi_n):
    gcd_val, x, y = extended_euclidean_algorithm(e, phi_n)
    if gcd_val != 1:
        raise ValueError("Modular inverse does not exist!")
    return x % phi_n if x > 0 else (x + phi_n) % phi_n

def is_prime(num):
    if num < 2:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

def generate_prime():
    while True:
        num = random.randint(10, 50)
        if is_prime(num):
            return num

def find_coprime(phi_n):
    e = 3
    while e < phi_n:
        if gcd(e, phi_n) == 1:
            return e
        e += 2
    raise ValueError("No valid e found")

def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, d, n):
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

def authenticate():
    password = "securepass123"
    for _ in range(3):
        user_input = input("Enter password to access RSA tool: ")
        if user_input == password:
            print("Authentication successful!")
            return True
        else:
            print("Incorrect password. Try again.")
    print("Access denied.")
    return False

def main():
    if not authenticate():
        return  # Stop if failed

    # RSA key generation and operations start here
    p = generate_prime()
    while True:
        q = generate_prime()
        if q != p:
            break

    N = p * q
    phi_n = (p - 1) * (q - 1)
    e = find_coprime(phi_n)
    d = mod_inverse(e, phi_n)

    message = input("Enter a message to encrypt: ")
    ciphertext = encrypt(message, e, N)
    print("Encrypted message:", ciphertext)

    decrypted_message = decrypt(ciphertext, d, N)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
