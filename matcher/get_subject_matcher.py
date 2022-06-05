import spacy
from spacy.matcher import Matcher
from constants.dependency import PUNCT

class GetSubjectMatcher():
    def __init__(self, sentence):
        self.nlp = spacy.load('en_core_web_sm')
        self.sentence = str(sentence)
        self.doc = self.nlp(self.sentence)

    def get_subject_matcher(self):
        role_rule_3 = [{'DEP':'nsubjpass'},{'DEP':'prep'},{'DEP':'pobj'}]
        role_rule_4 = [{'DEP':'nsubj'},{'DEP':'prep'},{'DEP':'pobj'}] 
        role_rule_5 = [{'DEP':'prep'},{'DEP':'pobj'}]  
        role_rule_6 = [{'DEP':'agent'},{'DEP':'pobj'}]             
        matcher = Matcher(self.nlp.vocab)
        matcher.add('Rule', [role_rule_3, role_rule_4, role_rule_5, role_rule_6])
        matches = matcher(self.doc)
        span = ""
        for _,start,end in matches:
            span = self.doc[start:end]
        return matches, span

    def get_subject_with_prep(self, v):
        #==================================
        #V => right
        #==================================
        for tok in v.rights:
            if tok.dep_ not in PUNCT:
                print("tok.dep_:",tok.dep_, tok.text)  
                if tok.dep_ in {"prep"}:
                    matches_text, span_text = self.get_subject_matcher()
                    print("Found! prep :", matches_text, span_text)        
        return matches_text, span_text             