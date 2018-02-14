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
            if wordlist.is_word(word):
                score += len(word)
        return score

    def max_score(self):
        score = 0
        split_prob = self.problem.split()
        for word in split_prob:
            score += len(word)
        return score
