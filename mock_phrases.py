import spacy
from constants.word import NEGATIONS
from constants.dependency import PUNCT
from extract.get_subject import GetSubject
from extract.get_verb import GetVerb
from extract.get_object import GetObject
from spacy.matcher import Matcher

class MockPhrases():
    #===================================Grammar=======================================
    #Subject <- VERB -> dobj
    #(Subject -> Subject) <- VERB -> dobj
    #(DET <- Subject -> Subject) <- VERB -> dobj
    #(DET <- Subject -> Subject) <- VERB -> dobj, VERB -> Verb
    #(DET <- Subject -> Subject) <- VERB -> dobj, VERB -> Verb -> dobj
    #(advmod <- VERB, DET <- Subject -> Subject) <- VERB -> dobj, VERB -> Verb -> dobj 
    #==================================================================================
    def __init__(self, sentence):
        self.nlp = spacy.load('en_core_web_sm')
        self.sentence = str(sentence)
        self.doc = self.nlp(self.sentence)
        self.svos = []
        self.signal_word_with_verb = []
        self.span_object = ""
        self.objNegated = ""
        self.subs = ""
        self.sequence = 0

    def merge_phrases(self):
        #=========================================
        #Subject <- VERB -> dobj
        #=========================================
        with self.doc.retokenize() as retokenizer:
            for np in list(self.doc.noun_chunks):
                attrs = {
                    "tag": np.root.tag_,
                    "lemma": np.root.lemma_,
                    "ent_type": np.root.ent_type_,
                }
                retokenizer.merge(np, attrs=attrs)
        return self.doc
    
    def merge_punct(self):
        #=========================================
        #Subject <- VERB -> dobj.
        #=========================================
        spans = []
        for word in self.doc[:-1]:
            if word.is_punct or not word.nbor(1).is_punct:
                continue
            start = word.i
            end = word.i + 1
            while end < len(self.doc) and self.doc[end].is_punct:
                end += 1
            span = self.doc[start:end]
            spans.append((span, word.tag_, word.lemma_, word.ent_type_))
        with self.doc.retokenize() as retokenizer:
            for span, tag, lemma, ent_type in spans:
                attrs = {"tag": tag, "lemma": lemma, "ent_type": ent_type}
                retokenizer.merge(span, attrs=attrs)
        return self.doc   
           
    def is_passive(self, tokens):
        #=========================================
        #Subject <- auxpass <- VERB -> dobj
        #=========================================
        for tok in tokens:
            print(tok.dep_, tok.text)
            if tok.dep_ == "auxpass":
                return True
        return False

    def is_negated(self, tok):
        #==================================================================================
        #Subject <- auxpass <- VERB -> ("no", "not", "n't", "never", "none") -> dobj
        #==================================================================================
        parts = list(tok.lefts) + list(tok.rights)
        for dep in parts:
            if dep.lower_ in NEGATIONS:
                return True
        return False  

    def get_signal_word_with_verb(self, v):
        #==================================================================================
        #Check Mark and Label
        #[VERB] -> <advmod> 
        #<advmod> <- [VERB]
        #<mark> <- [VERB]   
        #(mark or advmod) <- Subject <- auxpass <- [VERB] -> dobj
        #==================================================================================
        text = ""
        word = [tok for tok in v.lefts]
        if len(word) > 0:
            for tok in v.lefts:
                if tok.dep_ in ["mark","advmod","prep"]:
                    if str(tok.text) in ["In"]:
                        _, text = self.get_prep_matcher()
                        self.signal_word_with_verb.append("VO_")
                    elif str(tok.text) in ["Upon","Once","When","Whenever"]:
                        text = tok.text  
                        self.signal_word_with_verb.append("ExclusiveGateway_")
                    elif str(tok.text) in ["meantime"]:
                        text = tok.text 
                        self.signal_word_with_verb.append("ParallelGateway_")
                else:
                    self.signal_word_with_verb.append("VO_")  
        else:
            self.signal_word_with_verb.append("VO_")                         

        #===========================================================================================================================
        #Check Mark and Label
        #(mark or advmod) <- Subject <- auxpass <- VERB -> (cc -> conj) -> dobj and VERB -> (cc -> conj) -> dobj
        #===========================================================================================================================
        #Check Ex or VO
        for tok in v.rights:
            if tok.dep_ not in PUNCT:
                if tok.dep_ in {"cc","conj"}: 
                    if str(tok.text) in {"or"}:
                        self.signal_word_with_verb.clear() 
                        self.signal_word_with_verb.append("ExclusiveGateway_")    
                    elif str(tok.text) in {"and"}:
                        self.signal_word_with_verb.append("VO_") 
        return text                              

    def get_SVOS_is_active_v(self, i, sub, _subjects, v, verbNegated, objNegated, obj, event_label, signal_word_with_verb):  
        #================================================================================
        # V1 : svos.append((subject_uuid, verb_word_1, object_word, event_label, signal_word))
        #================================================================================
        if str(sub).find("who") != -1: 
            self.svos.append((i, "-", "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isActive", signal_word_with_verb))
        else:
            self.svos.append((i, _subjects, "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isActive", signal_word_with_verb))   

    def get_SVOS_is_passive_v(self, i, _subjects, v, verbNegated, objNegated, obj, event_label, signal_word_with_verb):
        #================================================================================
        # V1 : svos.append((subject_uuid, verb_word_1, object_word, event_label, signal_word))
        #================================================================================  
        self.svos.append((i, _subjects, "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isPassive", signal_word_with_verb))

    def get_SVOS_is_active_v2(self, i, sub, _subjects, v, v2, verbNegated, objNegated, obj, event_label, signal_word_with_verb): 
        #================================================================================
        # V1,V2 : svos.append((subject_uuid, verb_word_1, object_word, event_label, signal_word))
        #================================================================================
        if str(sub).find("who") != -1:  
            self.svos.append((i, "-", "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isActive", signal_word_with_verb))
            self.svos.append((i, "-", "!" + v2.lower_ if verbNegated or objNegated else v2.lower_, obj, event_label, "isActive", signal_word_with_verb))
        else:
            self.svos.append((i, _subjects, "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isActive", signal_word_with_verb))
            self.svos.append((i, _subjects, "!" + v2.lower_ if verbNegated or objNegated else v2.lower_, obj, event_label, "isActive", signal_word_with_verb)) 

    def get_SVOS_is_passive_v2(self, i, _subjects, v, v2, verbNegated, objNegated, obj, event_label, signal_word_with_verb):  
        #================================================================================
        # V1,V2 : svos.append((subject_uuid, verb_word_1, object_word, event_label, signal_word))
        #================================================================================ 
        self.svos.append((i, _subjects, "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isPassive", signal_word_with_verb))
        self.svos.append((i, _subjects, "!" + v2.lower_ if verbNegated or objNegated else v2.lower_, obj, event_label, "isPassive", signal_word_with_verb))                       
    
    #================================================================================
    # Get SVO Matcher
    #================================================================================
    def get_svo_matcher(self, subs, verb):
        objs = []
        isConj = False
        verb_rights = [tok for tok in verb.rights]
        if len(verb_rights) > 0:
            for tok in verb_rights:
                if tok.dep_ not in PUNCT:
                    if tok.dep_ in {"cc","conj"}: 
                        #Get Signal Word
                        signal_word = self.get_signal_word_with_verb(verb)
                        for sub in subs:
                            _subjects = str(sub).replace("an ","")
                            if tok.dep_ in {"conj"}:
                                verb = tok.text     #get verb from conj dep_
                                objs = self.get_object_matcher()
                                self.svos.append((self.sequence, _subjects, verb, objs, self.signal_word_with_verb[0], "isActive", signal_word))
                            else:
                                objs = self.get_object_matcher()
                                if len(objs) > 0:
                                    self.svos.append((self.sequence, _subjects, verb, objs, self.signal_word_with_verb[0], "isActive", signal_word))
                                else:
                                    self.svos.append((self.sequence, _subjects, verb, objs, self.signal_word_with_verb[0], "isActive", signal_word))    
                        isConj = True
                    else:
                        isConj = False
                return isConj, objs
        else:
            return isConj, objs
    
    def get_svo_object_matcher(self, subject, verb, signal_word):
        obj = self.get_object_matcher()
        if len(obj) > 0:
            self.svos.append((self.sequence, subject, verb, obj, self.signal_word_with_verb[0], "isActive", signal_word))
            return True
        else:
            return False  

    #================================================================================
    # Get SVO with V2, V1, Active/Passive, No Subject
    #================================================================================
    def get_svo_active_passive_v1(self, subject, subjects, verb, verbNegated, objNegated, obj, signal_word):
        if (str(verb.lemma_).find(str(verb.lower_)) != -1) \
            or (str(verb.lemma_+"s").find(str(verb.lower_)) != -1) \
            or (str(verb.lemma_+"es").find(str(verb.lower_)) != -1): 
            self.get_SVOS_is_active_v(self.sequence, subject, subjects, verb, verbNegated, objNegated, obj, self.signal_word_with_verb[0], signal_word)
        else:
            self.get_SVOS_is_passive_v(self.sequence, subjects, verb, verbNegated, objNegated, obj, self.signal_word_with_verb[0], signal_word)         
    
    def get_svo_active_passive_v2(self, subject, subjects, verb, verbs, verbNegated, objNegated, obj, signal_word):
        if (str(verb.lemma_).find(str(verb.lower_)) != -1) \
            or (str(verb.lemma_+"s").find(str(verb.lower_)) != -1) \
            or (str(verb.lemma_+"es").find(str(verb.lower_)) != -1):  
            self.get_SVOS_is_active_v2(self.sequence, subject, subjects, verb, verbs, verbNegated, objNegated, obj, self.signal_word_with_verb[0], signal_word)        
        else:
            self.get_SVOS_is_passive_v2(self.sequence, subjects, verb, verbs, verbNegated, objNegated, obj, self.signal_word_with_verb[0], signal_word)

    def get_svo_active_passive(self, subject, verb, verbNegated, signal_word):
        # check verb with __s, __es,
        if (str(verb.lemma_).find(str(verb.lower_)) != -1) \
                or (str(verb.lemma_+"s").find(str(verb.lower_)) != -1) \
                or (str(verb.lemma_+"es").find(str(verb.lower_)) != -1): 
            self.svos.append((self.sequence, "-", "!" + verb.lower_ if verbNegated else verb.lower_, subject, self.signal_word_with_verb[0], "isActive", signal_word))
        else:
            self.svos.append((self.sequence, "-", "!" + verb.lower_ if verbNegated else verb.lower_, subject, self.signal_word_with_verb[0], "isPassive", signal_word))

    def get_svo_no_subject(self, verb, objs, signal_word):
        for obj in objs:
            if (str(verb.lemma_).find(str(verb.lower_)) != -1) \
                or (str(verb.lemma_+"s").find(str(verb.lower_)) != -1) \
                or (str(verb.lemma_+"es").find(str(verb.lower_)) != -1): 
                self.svos.append((self.sequence, "-", verb, obj, self.signal_word_with_verb[0], "isActive", signal_word))
            else:
                self.svos.append((self.sequence, "-", verb, obj, self.signal_word_with_verb[0], "isPassive", signal_word))

    #================================================================================
    # Main SVO
    #================================================================================
    def get_svo(self, sentence):
        signal_word_with_verb = []

        doc = self.nlp(sentence)
        doc = self.merge_phrases()
        doc = self.merge_phrases()
        
        s = GetSubject()
        v = GetVerb() 
        o = GetObject()

        is_pas = self.is_passive(doc)           
        verbs = v.main_find_verbs(doc)          

        for verb in verbs:
            print("VERB :", verb)
            self.sequence += 1
            print("SEQUENCE :",self.sequence)

            #Get Subject/Verb      
            subs, verbNegated = s.main_get_all_subs(verb)               
            isConjVerb, conjV = v.right_of_verb_is_conj_verb(verb) 
            objs = "" 

            if isConjVerb:
                objs = self.get_svo_matcher(subs, verb)          
                #SVOS
                if len(objs) == 0:
                    v2, objs = o.main_get_all_objs(conjV, is_pas)  
                    signal_word = self.get_signal_word_with_verb(verb)
                    for sub in subs:
                        _subjects = str(sub).replace("an ","")
                        isMatcher = self.get_svo_object_matcher(_subjects, verb, signal_word)
                        if isMatcher == False:
                            for obj in objs:
                                objNegated = self.is_negated(obj) 
                                self.get_svo_active_passive_v2(sub, _subjects, verb, v2, verbNegated, objNegated, obj, signal_word)
            else:
                isConj, objs = self.get_svo_matcher(subs, verb) 
                #SVOS
                if len(objs) == 0 and isConj == False:       
                    _verb, objs = o.main_get_all_objs(verb, is_pas)
                    signal_word = self.get_signal_word_with_verb(verb) 
                    if len(subs) > 0:
                        for sub in subs:
                            _subject = str(sub).replace("an ","")
                            if len(objs) > 0:
                                isMatcher = self.get_svo_object_matcher(_subject, verb, signal_word)
                                if isMatcher == False:
                                    for obj in objs:
                                        objNegated = self.is_negated(obj) 
                                        self.get_svo_active_passive_v1(sub, _subject, _verb, verbNegated, objNegated, obj, signal_word)
                            else:
                                self.get_svo_active_passive(sub, _verb, verbNegated, signal_word)
                    else:
                        self.get_svo_no_subject(_verb, objs, signal_word)
                    
            #Clear All Signal Word
            signal_word_with_verb.clear() 

        print(self.svos)
        return self.svos 
    
    #================================================================================
    # Matcher
    #================================================================================
    def get_object_matcher(self):
        rule_1 = [{'DEP':'dobj'},{'DEP':'prep'},{'DEP':'pobj'}]
        matcher = Matcher(self.nlp.vocab)
        matcher.add('Object', [rule_1])
        matches = matcher(self.doc)

        span = ""
        for _,start,end in matches:
            span = self.doc[start:end]

        return span 

    def get_prep_matcher(self):
        rule_1 = [{'DEP':'prep'},{'DEP':'pobj'}]
        matcher = Matcher(self.nlp.vocab)
        matcher.add('PREP-POBJ', [rule_1])
        matches = matcher(self.doc)

        span = ""
        for _,start,end in matches:
            span = self.doc[start:end]

        return matches, span     