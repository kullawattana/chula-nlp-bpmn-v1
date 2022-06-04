import spacy
from constants.dependency import SUBJECTS, SUBJECTS_PASSIVE, SUBJECTS_ACTIVE
from constants.word import NEGATIONS
from matcher.get_subject_matcher import GetSubjectMatcher

class GetSubject():
    #==================================================
    # N <- [and] -> N
    # Group Actor + Verb Collection : 
    #   <(Subject (PRON) <- [and] -> Subject (PRON) <- nsubjpass> <- [VERB]
    # Verb + Actor Collection : 
    #   [VERB] -> <prep -> pobj>
    #   [VERB] -> <agent -> pobj> 
    #   <prep -> pobj> <- [VERB]
    #==================================================
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def contains_conj(self, depSet):
        return "and" in depSet or "or" in depSet or "nor" in depSet or \
            "but" in depSet or "yet" in depSet or "so" in depSet or "for" in depSet        

    def is_negated(self, tok):
        parts = list(tok.lefts) + list(tok.rights)
        for dep in parts:
            if dep.lower_ in NEGATIONS:
                return True
        return False    

    def get_subject_with_verb(self, v):
        #======================================
        #Get (subject <= V)
        #======================================
        subjects = ""
        dep_subject = ""
        for tok in v.lefts:
            if tok.dep_ in SUBJECTS and tok.pos_ != "DET":
                subjects = tok.text
                dep_subject = tok.dep_  
        return subjects, dep_subject  

    def get_subject_with_agent(self, v):
        #======================================
        #Get (V => agent)
        #======================================
        matcher = GetSubjectMatcher()
        agent = [tok for tok in v.rights if tok.dep_ in {"agent"}]
        if len(agent) > 0:
            print("agent:", agent)
            if len(agent) > 0:
                matches_subject, span_subject = matcher.get_subject_matcher()    
                if str(span_subject).find(str(agent[0])) != -1:
                    print("Found! relation with 'agent' :", matches_subject, span_subject) 
        # #nsubjpass => prep => pobj
        # elif dep_subject == "nsubjpass":
        #     if len(subjects) > 0:
        #         matches_subject, span_subject = matcher.get_subject_matcher() 
        #         # if str(span_subject).find(str(subjects[0])) != -1:
        #         #     print("Found! relation with subject passive :", matches_subject, span_subject)
        # #nsubj => prep => pobj
        # else:
        #     if len(subjects) > 0:
        #         matches_subject, span_subject = matcher.get_subject_matcher() 
        #         # if str(span_subject).find(str(subjects[0])) != -1:
        #         #     print("Found! relation with subject active :", matches_subject, span_subject)               
        return matches_subject, span_subject                 

    def main_get_all_subs(self, v):
        #======================================
        #Find conjunnction between subject with verb
        #======================================
        verb_negated = self.is_negated(v)
        subs = [tok for tok in v.lefts if tok.dep_ in SUBJECTS and tok.pos_ != "DET"]
        if len(subs) > 0:
            subs.extend(self._get_subs_from_conjunctions(subs))
        else:
            foundSubs, verb_negated = self._find_subs(v)
            subs.extend(foundSubs)
        return subs, verb_negated  

    def _get_all_subs_passive(self, v):
        #======================================
        #Find conjunnction between subject with verb (Passive)
        #======================================
        verb_negated = self.is_negated(v)        
        subs_passive = [tok for tok in v.lefts if tok.dep_ in SUBJECTS_PASSIVE and tok.pos_ != "DET"]
        if len(subs_passive) > 0:
            subs_passive.extend(self._get_subs_from_conjunctions(subs_passive))
        else:
            foundSubs, verb_negated = self._find_subs(v)
            subs_passive.extend(foundSubs)
        return subs_passive, verb_negated 

    def _get_all_subs_active(self, v):  
        #======================================
        #Find conjunnction between subject with verb (Active)
        #======================================
        verb_negated = self.is_negated(v)      
        subs_active = [tok for tok in v.lefts if tok.dep_ in SUBJECTS_ACTIVE and tok.pos_ != "DET"]
        if len(subs_active) > 0:
            subs_active.extend(self._get_subs_from_conjunctions(subs_active))
        else:
            foundSubs, verb_negated = self._find_subs(v)
            subs_active.extend(foundSubs)
        return subs_active, verb_negated           

    # get subs joined by conjunctions
    def _get_subs_from_conjunctions(self, subs):
        #======================================
        #Find conjunnction between subject with verb
        #======================================
        more_subs = []
        for sub in subs:
            rights = list(sub.rights)
            rightDeps = {tok.lower_ for tok in rights}
            if self.contains_conj(rightDeps):
                more_subs.extend([tok for tok in rights if tok.dep_ in SUBJECTS or tok.pos_ == "NOUN"])
                if len(more_subs) > 0:
                    more_subs.extend(self._get_subs_from_conjunctions(more_subs))
        return more_subs   

    # find sub dependencies
    def _find_subs(self, tok):
        #======================================
        #nsubj <= V
        #======================================
        head = tok.head
        while head.pos_ != "VERB" and head.pos_ != "NOUN" and head.head != head:
            head = head.head
        if head.pos_ == "VERB":
            subs = [tok for tok in head.lefts if tok.dep_ == "SUB"]
            if len(subs) > 0:
                verb_negated = self.is_negated(head)
                subs.extend(self._get_subs_from_conjunctions(subs))
                return subs, verb_negated
            elif head.head != head:
                return self._find_subs(head)
        elif head.pos_ == "NOUN":
            return [head], self.is_negated(tok)
        return [], False       
