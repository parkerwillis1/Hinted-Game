# game/utils/glove_loader.py

class GloVeLoader:
    def __init__(self, file_path):
        self.glove_model = self.load_glove_model(file_path)

    def load_glove_model(self, file_path):
        print("Loading GloVe Model")
        glove_model = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                split_line = line.split()
                word = split_line[0]
                embedding = [float(val) for val in split_line[1:]]
                glove_model[word] = embedding
        print(f"Done. {len(glove_model)} words loaded!")
        return glove_model

    def get_word_vector(self, word):
        return self.glove_model.get(word)
