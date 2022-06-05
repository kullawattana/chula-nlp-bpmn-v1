import spacy

class GetMark():
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def is_mark(self, v):
        word = [tok for tok in v.lefts if tok.dep_ in ["mark","advmod","prep"]]
        return word    

    def is_mark_right(self, v):
        word = [tok for tok in v.rights if tok.dep_ in ["prep"]]
        return word 

    def is_mark_continue_right(self, words):
        result_words = []
        for w in words:
            word = [tok for tok in w.rights if tok.dep_ in ["pobj"]]
            if len(word) > 0:
                result_words.append(str(w)+" "+str(word[0]).replace(",",""))
        return result_words       