import cryptogram_solution

class cryptogram_problem():
    def set_ciphertext(self,ciphertext):
        self.problem = ciphertext

    def apply_solution(self,solution):
        return solution.decipher(self.problem)

    def score_solution(self,cleartext,wordlist):
        score = 0
        clear_list = cleartext.split()
        for word in clear_list:
            if word in wordlist:
                score += len(word)
        return score
