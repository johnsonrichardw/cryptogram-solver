class cryptogram_wordlist():
    def __init__(self):
        self.words = {}

    def load_list(self,filename):
        #f = open(filename, encoding='utf-8')
        f = open(filename)
        for line in f:
            split_list = line.split()
            for word in split_list:
                self.words[word.upper()] = 1
        f.close()

    def is_word(self,word):
        return word in self.words
