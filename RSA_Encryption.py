import random

def gcd(a, b):
    while b != 0:
        a, b = b, a%b   # Set a to b and b to the remainder of a divided by b
    return a # when b is 0 a will be the gcd

def extended_euclidean_algorithm(a,b):
    if a == 0:
        return b, 0, 1      # Base case: gcd(b, 0) = b, and x = 0, y = 1 
    gcd, x1, y1 = extended_euclidean_algorithm(b%a, a) #recursive call. keep calling b%a until a becomes 0
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi_n):
    gcd, x, y = extended_euclidean_algorithm(e, phi_n)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist!") # e and phi_n must be coprime
    return x % phi_n if x > 0 else (x + phi_n) % phi_n #Ensure positive result

def is_prime(num):
    if num < 2:
        return False
    for n in range (2, int(num**0.5) + 1):  #Check up to sqrt(num). we only need to check up to sq root of num
        if num % n == 0:
            return False
    return True


#Step 1: Generate 2 Prime Numbers

def generate_prime():
    while True:
        num = random.randint(10, 50)
        if is_prime(num):
            return num

p = generate_prime()      
while True:
    q = generate_prime()
    if q != p:
        break #Ensure p and q are different

#Step 2: Compute n and Euler's totient function φ(n)

N = (p*q)
phi_n = (p-1)*(q-1)

#Step 3: Choose an encryption key such that 1<e<φ(n) and e is coprime with φ(n) and N

def find_coprime(phi_n):
    e = 3 #start with e = 3 and increment it because we skip checking through even numbers which are not prime 
    while e < phi_n:
        if gcd(e, phi_n) == 1:
            return e
        e += 2
    raise ValueError("No valid e found")

e = find_coprime(phi_n)

#Step 4: Compute decryption key

d = mod_inverse(e, phi_n)

#Step 5: Encyption function

def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]  #char^e(mod n) #ord because you cant compute on char so convert to ASCII
    #ciphertext = char^e (mod N)

#Step 6: Decryption function

def decrypt(ciphertext, d, n):
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in ciphertext]) #chr to convert back to char
    return decrypted_message
    #original_char = ciphertext^d (mod N)

#Testing the Encryption implementation
message = input("Enter a message to encrypt: ")
ciphertext = encrypt(message, e, N)
print("Encypted message: ", ciphertext)

decrypted_message = decrypt(ciphertext, d, N)
print("Decrypted message: ", decrypted_message)



