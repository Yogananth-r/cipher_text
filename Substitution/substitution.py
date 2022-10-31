from string import digits, ascii_letters
from random import shuffle
import pfc as pfc

class Substitution():
    """contains caesarcipher, monoalphabetic ciopher, playfair cipher"""
    def __init__(self):
        pass


class CaesarCipher(Substitution):
    def __init__(self):
        super().__init__()
    
    def encrypt(self,text,shift):
        self.ciphered_text=""
        for i in range(len(text)):
            self.current_char=text[i]
            if(self.current_char==" "):
                    self.ciphered_text+=" "
            elif (self.current_char.isupper()):
                self.ciphered_text+=chr((ord(self.current_char)+shift-65)%26 + 65)
            else:
                self.ciphered_text+=chr((ord(self.current_char)+shift-97)%26 + 97)
        return self.ciphered_text

    def decrypt(self,ciphered_text,shift):
        self.deciphered_text=""
        for i in range(len(ciphered_text)):
            self.current_char=ciphered_text[i]
            if(self.current_char==" "):
                    self.deciphered_text+=" "
            elif (self.current_char.isupper()):
                self.deciphered_text+=chr((ord(self.current_char)-shift-65)%26 + 65)
            else:
                self.deciphered_text+=chr((ord(self.current_char)-shift-97)%26 + 97)
        return self.deciphered_text




class MonoAlphabeticCipher(Substitution):
    def __init__(self):
         super().__init__()
    
    def shuffle_letters(self,pool=None):
        if pool is None:
            pool=ascii_letters + digits
        self.original_pool=list(pool)
        self.shuffled_pool=list(pool)
        shuffle(self.shuffled_pool)
        return dict(zip(self.original_pool,self.shuffled_pool))

    def inverse_monoalpha_cipher(self,monoalpha_cipher):
        self.inverse_monoalpha={}
        for self.key, self.value in monoalpha_cipher.items():
            self.inverse_monoalpha[self.value]=self.key
        return self.inverse_monoalpha
    
    def encrypt(self,text,monoalpha_cipher):
        self.ciphered_text=[]
        for letter in text:
            self.ciphered_text.append(monoalpha_cipher.get(letter, letter))
        return ''.join(self.ciphered_text)
    
    def decrypt(self,ciphered_text,monoalpha_cipher):
        self.mon=self.inverse_monoalpha_cipher(monoalpha_cipher)
        return self.encrypt(ciphered_text,self.mon)

class PlayfairCipher(Substitution):
    def __init__(self):
        super().__init__()
    
    def encrypt(self,text,key):
        self.cipher=pfc.playfair(key,text)
        return self.cipher
    def decrypt(self,ciph,key):
        self.deciph=pfc.playfair(key,ciph,False)
        return self.deciph
        


    