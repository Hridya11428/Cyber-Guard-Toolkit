from primenumber import *
from Ciphers import CaesarCipher
class Client:
    def __init__(self ,name ,private_key):
        self.name = name # stores the client's name inside the object
        self.private_key= private_key # similarly with their private key
        self.public_key=None

    def compute_public_key(self, b, p):
        self.public_key = mod_exp(b, self.private_key, p)
        return self.public_key 

    def compute_shared_secret(self, others_public_key, p):
        shared_secret = mod_exp(others_public_key, self.private_key, p)
        return shared_secret
