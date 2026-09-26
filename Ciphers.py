class Cipher:
    def __init__(self, key):
        self.key=key
    def encrypt(self,text):
        pass
    def decrpyt(self, text):
        pass

#ceasar cipher encrypts the data by pushing all the letter the same number of times so like a is c then b is d and so on
class CaesarCipher(Cipher):
    def encrypt(self, text):
        result=""

        for letter in text :
            if letter.isupper():
                position=ord(letter)-ord('A')
                new_position=(position+self.key)%26
                result=result+chr(new_position+ord('A'))
            elif letter.islower():
                position=ord(letter)-ord('a')
                new_position=(position+self.key)%26
                result=result+chr(new_position+ord('a'))
            else:
                result=result+letter
        return result
    def decrypt(self, text):
        result=""

        for letter in text:
            if letter.isupper():
                position=ord(letter)-ord('A')
                new_position=(position- self.key)%26
                result=result+chr(new_position+ord('A'))
            elif letter.islower():
                position=ord(letter)-ord('a')
                new_position=(position-self.key)%26
                result=result+chr(new_position+ord('a'))
            else:
                result=result+letter
        return result

#atbash cipher encrpts the data by mirroring the letters
class AtbashCipher(Cipher):
    def encrypt(self, text):
        result=""

        for letter in text:
            if letter.isupper():
                position=ord(letter)-ord('A')
                mirrored=25-position
                result=result+chr(mirrored+ord('A'))
            elif letter.islower():
                position=ord(letter)-ord('a')
                mirrored=25-position
                result=result+chr(mirrored+ord('a'))
            else:
                result=result+letter
        return result
    def decrypt(self,text):
        return self.encrypt(text)