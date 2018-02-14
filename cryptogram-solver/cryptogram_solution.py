import string
import random
import copy

class cryptogram_solution():
    def __init__(self):
        self.char_list = list(string.ascii_uppercase)
        self.solution = self.gen_initial_solution()

    def gen_initial_solution(self):
        solution = {c:c for c in self.char_list}
        val_list = [solution[k] for k in solution.keys()]
        random.shuffle(val_list)
        for k in solution.keys():
            solution[k] = val_list.pop()
        return solution

    def get_deciphered_value(self,cipher_char):
        if cipher_char not in self.solution:
            return cipher_char
        else:
            return self.solution[cipher_char]

    def set_deciphered_value(self,cipher_char,decipher_char):
        self.solution[cipher_char] = decipher_char

    def swap_values(self,cipher1,cipher2):
        val = self.get_deciphered_value(cipher1)
        self.set_deciphered_value(cipher1,self.get_deciphered_value(cipher2))
        self.set_deciphered_value(cipher2,val)

    def get_random_swap_chars(self):
        a = random.choice(self.char_list)
        b = a
        while a == b:
            b = random.choice(self.char_list)
        return a,b

    def mutate(self):
        a,b = self.get_random_swap_chars()
        self.swap_values(a,b)

    def decipher(self,ciphertext):
        cleartext = ''
        ciphertext = ciphertext.upper()
        for i in range(len(ciphertext)):
            cleartext += self.get_deciphered_value(ciphertext[i])
        return cleartext

    def copy(self):
        c = cryptogram_solution()
        c.solution = copy.deepcopy(self.solution)
        return c
