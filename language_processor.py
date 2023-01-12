

class LemmaConverter:
    def __init__(self, lemma_file_path):
        self.lemma_dict = {}
        
        data = open(lemma_file_path, "r")
        while True:
            line = data.readline()
            if not line:
                break
            line = line.strip()
            lemma_pair = line.split()
            self.lemma_dict[lemma_pair[1]] = lemma_pair[0]
    
    def convert_to_lemma(self, token):
        return self.lemma_dict[token]

if __name__ == '__main__':
    print("lol")