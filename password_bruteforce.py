from primenumber import *
from Ciphers import CaesarCipher
common_passwords = ['123456', 'password', 'qwerty', 'admin', 'abc', 'abc123', 'welcome']

# we can directly check from the above dictionary if it is one of the common passwords
def brute_force_password(target_password):
    attempts = 0
    for guess in common_passwords:
        attempts+=1
        if guess==target_password:
            return True
    return False

#when the diffie hellman parametera are small then it can be easily decrypted by brute force
# public key = b^private key mod p
# here b is base and p is prime modulus
#p is not the limit for dh problems but since this is just a small project we are just basically proving that if b n p are small then it is really easy to break the encryption
def brute_force_dh(b,p,known_public_key):
    attempts = 0
    for guess in range (p):
        attempts+=1
        if mod_exp(b,guess,p)==known_public_key:
            print(f"Private key found: {guess} (in {attempts} attempts)")
            return guess
    return None

def brute_force_caesar(ciphertext):
    for key in range(26):
        cipher = CaesarCipher(key)
        attempt = cipher.decrypt(ciphertext)
        print(f"Key {key}: {attempt}")