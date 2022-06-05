import spacy

class GetVerb():
    #==================================================
    # [VERB] -> <dobj> 
    # [VERB] -> <dobj> -> [NOUN] {Subject} 
    # [VERB] -> <dobj -> prep -> pobj {Subject}>  
    # [VERB] -> <dobj -> prep -> pobj -> prep -> pobj {Subject}> 
    #==================================================
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def main_find_verbs(self, tokens):
        #====================================================
        # aux <= V
        #====================================================
        verbs = [tok for tok in tokens if self._is_non_aux_verb(tok)]
        if len(verbs) == 0:
            verbs = [tok for tok in tokens if self._is_verb(tok)]
        return verbs      

    def right_of_verb_is_conj_verb(self, v):
        #====================================================
        # VERB CCONJ VERB (e.g. he beat and hurt me)
        #====================================================
        rights = list(v.rights)
        if len(rights) > 1 and rights[0].pos_ == 'CCONJ':
            for tok in rights[1:]:
                if self._is_non_aux_verb(tok):
                    return True, tok
        return False, v      

    def _is_non_aux_verb(self, tok):
        #====================================================
        # is the token a verb?  (excluding auxiliary verbs)
        #====================================================
        return tok.pos_ == "VERB" and (tok.dep_ != "aux" and tok.dep_ != "auxpass")

    def _is_verb(self, tok):
        #====================================================
        # is the token a verb?  (including auxiliary verbs)
        #====================================================
        return tok.pos_ == "VERB" or tok.pos_ == "AUX"

    def get_advcl_right(self, v):
        #====================================================
        #V => advcl => V
        #====================================================
        advcl = [tok for tok in v.rights if tok.dep_ in {"advcl"}]
        if len(advcl) > 0:
            print("relation of verb on right:",advcl)
            return advcl

    def get_advcl_left(self, v):
        #====================================================
        #V <= advcl <= V
        #====================================================
        advcl = [tok for tok in v.lefts if tok.dep_ in {"advcl"}]
        if len(advcl) > 0:
            print("relation of verb on left:",advcl)  
            return advcl       
