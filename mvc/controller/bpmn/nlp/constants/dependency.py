SUBJECTS = ["nsubj","nsubjpass","csubj","csubjpass","agent", "expl"]
SUBJECTS_ACTIVE = ["nsubj", "csubj", "agent", "expl"]
SUBJECTS_PASSIVE = ["nsubjpass", "csubjpass"]
AUX_VERB = ["aux", "auxpass"]
VERB = ["ROOT"]
OBJECTS = ["dobj", "dative", "attr", "oprd", "pobj"]
PASSIVE_SENTENCE = ['nsubjpass', 'ROOT', 'aux', 'auxpass', 'prep', 'pobj']
ACTIVE_SENTENCE = ['nsubj', 'ROOT', 'aux', 'dobj', 'ccomp', 'xcomp']
ADJECTIVES = ["acomp", "advcl", "advmod", "amod", "appos", "nn", "nmod", "ccomp", "complm", "hmod", "infmod", "xcomp", "rcmod", "poss", " possessive"]
COMPOUNDS = ["compound"]
PREPOSITIONS = ["prep"]
ADP = ["ADP"]
INDEPENDENTS = ["conj"]
ADVERB = ["advcl"]
BREAKER_POS = {"CCONJ", "VERB"}  
PUNCT = {"punct"}