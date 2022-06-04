import spacy
from constants.word import CONJUNCTION_COMPARISON, CONJUNCTION_OF_CHOICE, CONJUNCTION_OF_CONDITION, CONJUNCTION_OF_TIME, PARALLEL_WORDS, NEGATIONS
from constants.dependency import PUNCT
from extract.get_subject import GetSubject
from extract.get_verb import GetVerb
from extract.get_object import GetObject
from extract.get_similarity import GetSimilarity
from matcher.get_prep_pobj_matcher import GetPrepPobjMatcher

class Phrases():
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
        self.span_object = ""
        self.objNegated = ""
        self.subs = ""
        self.sequence = 0

    def merge_phrases(self):
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
        #Subject <- VERB -> dobj
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
    
    def get_verb_suffix_with_s_and_es(self, verb):
        if (str(verb.lemma_).find(str(verb.lower_)) != -1) \
            or (str(verb.lemma_+"s").find(str(verb.lower_)) != -1) \
            or (str(verb.lemma_+"es").find(str(verb.lower_)) != -1):
            return True
        else:
            return False

    def get_signal_word_with_verb(self, v):
        #==================================================================================
        #Check Mark and Label
        #[VERB] -> <advmod> 
        #<advmod> <- [VERB]
        #<mark> <- [VERB]   
        #(mark or advmod) <- Subject <- auxpass <- [VERB] -> dobj
        #==================================================================================
        signal_word_text = ""
        _event_label = ""
        word = [tok for tok in v.lefts]
        if len(word) > 0:
            for tok in v.lefts:
                if tok.dep_ in ["mark","advmod","prep"]:
                    token_text = str(tok.text).lower()
                    if str(token_text) in ["In"]:
                        _, signal_word_text = GetPrepPobjMatcher(tok.text).get_prep_matcher()
                        _event_label = "VO_"
                    elif str(token_text) in CONJUNCTION_OF_CONDITION:
                        signal_word_text = token_text
                        _event_label = "ExclusiveGateway_"
                    elif str(token_text) in CONJUNCTION_COMPARISON:
                        signal_word_text = token_text  
                        _event_label = "ExclusiveGateway_"
                    elif str(token_text) in CONJUNCTION_OF_CHOICE:
                        signal_word_text = token_text 
                        _event_label = "ExclusiveGateway_"
                    elif str(token_text) in CONJUNCTION_OF_TIME:
                        signal_word_text = token_text  
                        _event_label = "VO_"
                    elif str(token_text) in PARALLEL_WORDS:
                        signal_word_text = token_text
                        _event_label = "ParallelGateway_"
        else:
            signal_word_text = "-"
            _event_label = "VO_"

        #===========================================================================================================================
        #Check Mark and Label
        #(mark or advmod) <- Subject <- auxpass <- VERB -> (cc -> conj) -> dobj and VERB -> (cc -> conj) -> dobj
        #===========================================================================================================================
        #Check Ex or VO
        for tok in v.rights:
            if tok.dep_ not in PUNCT:
                if tok.dep_ in {"cc","conj"}: 
                    token_text = str(tok.text).lower()
                    if str(token_text) in {"or"}:
                        signal_word_text = tok.text
                        _event_label = "ExclusiveGateway_"  
                    elif str(token_text) in {"and"}:
                        signal_word_text = tok.text 
                        _event_label = "VO_"
        return signal_word_text, _event_label 

    def get_SVOS_is_active_v(self, i, subjects, v, verbNegated, objNegated, obj, event_label, signal_word_with_verb):  
        #================================================================================
        # V1 : svos.append((subject_uuid, verb_word_1, object_word, event_label, signal_word))
        #================================================================================
        if str(subjects).find("who") != -1: 
            self.svos.append((i, "-", "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isActive", signal_word_with_verb))
        else:
            self.svos.append((i, subjects, "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isActive", signal_word_with_verb))   

    def get_SVOS_is_passive_v(self, i, _subjects, v, verbNegated, objNegated, obj, event_label, signal_word_with_verb):
        #================================================================================
        # V1 : svos.append((subject_uuid, verb_word_1, object_word, event_label, signal_word))
        #================================================================================  
        self.svos.append((i, _subjects, "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isPassive", signal_word_with_verb))

    def get_SVOS_is_active_v2(self, i, subjects, v, v2, verbNegated, objNegated, obj, event_label, signal_word_with_verb): 
        #================================================================================
        # V1,V2 : svos.append((subject_uuid, verb_word_1, object_word, event_label, signal_word))
        #================================================================================
        if str(subjects).find("who") != -1:  
            self.svos.append((i, "-", "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isActive", signal_word_with_verb))
            self.svos.append((i, "-", "!" + v2.lower_ if verbNegated or objNegated else v2.lower_, obj, event_label, "isActive", signal_word_with_verb))
        else:
            self.svos.append((i, subjects, "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isActive", signal_word_with_verb))
            self.svos.append((i, subjects, "!" + v2.lower_ if verbNegated or objNegated else v2.lower_, obj, event_label, "isActive", signal_word_with_verb)) 

    def get_SVOS_is_passive_v2(self, i, _subjects, v, v2, verbNegated, objNegated, obj, event_label, signal_word_with_verb):  
        #================================================================================
        # V1,V2 : svos.append((subject_uuid, verb_word_1, object_word, event_label, signal_word))
        #================================================================================ 
        self.svos.append((i, _subjects, "!" + v.lower_ if verbNegated or objNegated else v.lower_, obj, event_label, "isPassive", signal_word_with_verb))
        self.svos.append((i, _subjects, "!" + v2.lower_ if verbNegated or objNegated else v2.lower_, obj, event_label, "isPassive", signal_word_with_verb))                       
        
    def get_svo(self, sentence, is_show_gateway):
        doc = self.nlp(sentence)
        doc = self.merge_phrases()
        doc = self.merge_phrases()
        
        s = GetSubject()
        v = GetVerb() 
        o = GetObject()
        #===========================================
        #1 Start
        #2 Check passive sentence/ Check active sentence
        #3 Find verb
            #3.1 Check Start verb to start process
        #4 subject <= V    
        #5 Find verb conjunnction between subject
        #6 Prepare subject, verb and object
        #7 get S,V => SVO
        #===========================================
        is_pas = self.is_passive(doc)           #2
        verbs = v.main_find_verbs(doc)          #3
        for verb in verbs:                      #4
            self.sequence += 1
            subs, verbNegated = s.main_get_all_subs(verb)               #5
            isConjVerb, conjV = v.right_of_verb_is_conj_verb(verb)      #6
            if isConjVerb:
                v2, objs = o.main_get_all_objs(conjV, is_pas)           #7 
                
                signal_word = ""
                if is_show_gateway == True:
                    signal_word, _event_label = self.get_signal_word_with_verb(verb)      #8 
                    if len(_event_label) == 0:
                        signal_word = "-"
                        _event_label = "VO_"
                else:
                    _event_label = "VO_"

                for sub in subs:
                    _subjects = str(sub).replace("an ","")
                    for obj in objs:
                        objNegated = self.is_negated(obj) 
                        if self.get_verb_suffix_with_s_and_es(verb) == True: 
                            print("1xxxx", _subjects)
                            self.get_SVOS_is_active_v2(self.sequence, _subjects, verb, v2, verbNegated, objNegated, obj, _event_label, signal_word)        
                        else:
                            print("2xxxx", _subjects)
                            self.get_SVOS_is_passive_v2(self.sequence, _subjects, verb, v2, verbNegated, objNegated, obj, _event_label, signal_word)
            else:    
                verb, objs = o.main_get_all_objs(verb, is_pas)
                
                signal_word = ""
                if is_show_gateway == True:
                    signal_word, _event_label = self.get_signal_word_with_verb(verb)      #8 
                    if len(_event_label) == 0:
                        signal_word = "-"
                        _event_label = "VO_"
                else:
                    _event_label = "VO_"

                for sub in subs:
                    _subjects = str(sub).replace("an ","")
                    if len(objs) > 0:
                        for obj in objs:
                            objNegated = self.is_negated(obj) 
                            if self.get_verb_suffix_with_s_and_es(verb) == True: 
                                print("3xxxx", _subjects)
                                self.get_SVOS_is_active_v(self.sequence, _subjects, verb, verbNegated, objNegated, obj, _event_label, signal_word)
                            else:
                                print("4xxxx", _subjects)
                                self.get_SVOS_is_passive_v(self.sequence, _subjects, verb, verbNegated, objNegated, obj, _event_label, signal_word)
                    else:
                        if self.get_verb_suffix_with_s_and_es(verb) == True:
                            print("5xxxx")    
                            self.svos.append((self.sequence, "-", "!" + verb.lower_ if verbNegated else verb.lower_, sub, _event_label, "isActive", signal_word))
                        else:
                            print("6xxxx")    
                            self.svos.append((self.sequence, "-", "!" + verb.lower_ if verbNegated else verb.lower_, sub, _event_label, "isPassive", signal_word))         
        return self.svos

    #=====================================================================================
    # get_new_svos()
    #=====================================================================================
    def get_subject_collection(self):
        #=====================================================================================
        #change loop by sentence and check "subject" with the collection of subject (new_list)
        #=====================================================================================
        sentence_list = []
        sentence_list.append(self.svos)
        subjects = []
        for sv in sentence_list:
            for svo in sv:
                if str(svo[1]) != "-": 
                    subjects.append((str(svo[1])).replace("a ","")) 
        return sentence_list, subjects
    
    def get_duplicates_subject(self, subjects):
        sort_list = sorted(subjects)
        duplicates_subject = []
        for i in sort_list:
            if sort_list.count(i) > 1:
                if i not in duplicates_subject:
                    duplicates_subject.append(i)

        #อาจจะไม่มี duplicate
        new_subject_list = list(dict.fromkeys(subjects))
        if len(duplicates_subject) == 0:
            duplicates_subject = new_subject_list

        return new_subject_list, duplicates_subject
    
    def renew_svos_with_sentence(self, similar_list, sentence_list):
        #=================================================================================================================
        #       svo[0], _subs,        svo[2],               svo[3],          svo[4],           svo[5],         svo[6]
        #SVOS = ( seq,    S,    (V, V2, verbNegated), (objNegated, obj),   "event_tag",  isPassive/isActive, signal_word )
        #=================================================================================================================
        renew_list = list(dict.fromkeys(similar_list))
        new_svos = []
        _subs = ""
        _role_subjects = []
        for sv in sentence_list:
            for svo in sv:
                for main_subject in renew_list:
                    if str(svo[1]) == main_subject:
                        _subs = svo[1]
                        _role_subjects.append(_subs)
                new_svos.append((svo[0], _subs, svo[2], svo[3], svo[4], svo[5], svo[6])) 
        return renew_list, new_svos
    
    def get_bpmn_direction_from_svos(self, new_svos, renew_list):
        #=================================================================================================================
        #       svo[0], _subs,        svo[2],               svo[3],          svo[4],           svo[5],         svo[6]
        #SVOS = ( seq,    S,    (V, V2, verbNegated), (objNegated, obj),   "event_tag",  isPassive/isActive, signal_word , BPMN-MOVE-NEXT)
        
        #Note Seq = 1 ไม่ต้องปรับ เป็นตัวเริ่มต้น Flow
        #SVOS = (  1 ,    S,    (V, V2, verbNegated), (objNegated, obj),   "event_tag",  isPassive/isActive, signal_word , BPMN-MOVE-NEXT/BPMN-MOVE-UP/BPMN-MOVE-DOWN)
        #Note Seq = 2,...N ปรับ format ตาม isActive/isPassive
        #SVOS = (  2 ,    S,    (V, V2, verbNegated), (objNegated, obj),   "event_tag",  isPassive/isActive, signal_word , BPMN-MOVE-NEXT/BPMN-MOVE-UP/BPMN-MOVE-DOWN)
        #SVOS = (  N ,    S,    (V, V2, verbNegated), (objNegated, obj),   "event_tag",  isPassive/isActive, signal_word , BPMN-MOVE-NEXT/BPMN-MOVE-UP/BPMN-MOVE-DOWN)
        #=================================================================================================================
        init_move_direction = 0
        direction = ["BPMN-MOVE-UP","BPMN-MOVE-DOWN","BPMN-MOVE-NEXT"]
        get_direction = ""
        renew_svos = []
        for svo in new_svos:
            if len(str(svo[1])) > 0:
                number_of_subject = renew_list.index(str(svo[1]))
                if number_of_subject > init_move_direction:         #1 > 0 DOWN
                    init_move_direction = number_of_subject           
                    get_direction = direction[1]                    
                elif number_of_subject < init_move_direction:       #0 < 1 UP
                    init_move_direction = number_of_subject 
                    get_direction = direction[0]                          
                else:
                    init_move_direction = number_of_subject         #0 == 0 NEXT 
                    get_direction = direction[2]
                renew_svos.append((svo[0], svo[1], svo[2], svo[3], svo[4], svo[5], svo[6], get_direction)) 
            else:
                get_direction = direction[2]
                if svo[0] == 1:     #first sentence hasn't no subject, add subject first
                    renew_svos.append((svo[0], renew_list[0], svo[2], svo[3], svo[4], svo[5], svo[6], get_direction)) 
                else:
                    renew_svos.append((svo[0], svo[1], svo[2], svo[3], svo[4], svo[5], svo[6], get_direction))
        return renew_svos

    def get_new_svos(self):
        _sentence_list, _subjects = self.get_subject_collection()
        _new_subject_list, _duplicates_subject = self.get_duplicates_subject(_subjects)
        _similar_list = GetSimilarity().get_similarity(_duplicates_subject, _new_subject_list)
        _renew_list, _new_svos = self.renew_svos_with_sentence(_similar_list, _sentence_list)
        _renew_svos = self.get_bpmn_direction_from_svos(_new_svos, _renew_list)
        return _renew_svos      