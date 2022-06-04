import spacy
from spacy.matcher import Matcher

class GetObjectMatcher():
    def __init__(self, sentence):
        self.nlp = spacy.load('en_core_web_sm')
        self.sentence = str(sentence)
        self.doc = self.nlp(self.sentence)

    def get_object_matcher(self):
        rule_1 = [{'DEP':'dobj'},{'DEP':'prep'},{'DEP':'pobj'}]
        matcher = Matcher(self.nlp.vocab)
        matcher.add('Object', [rule_1])
        matches = matcher(self.doc)

        span = ""
        for _,start,end in matches:
            span = self.doc[start:end]

        return matches, span    