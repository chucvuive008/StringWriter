from converter import *

class DuplicateRemover(Converter):
    def convert(self, string):
        list_of_word = string.split()
        list_of_non_duplicate_word = []
        for word in list_of_word:
            if word not in list_of_non_duplicate_word:
                list_of_non_duplicate_word.append(word)
        return " ".join(list_of_non_duplicate_word)
