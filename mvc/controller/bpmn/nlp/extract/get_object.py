import spacy
from constants.dependency import OBJECTS

class GetObject():
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def contains_conj(self, depSet):
        return "and" in depSet or "or" in depSet or "nor" in depSet or \
            "but" in depSet or "yet" in depSet or "so" in depSet or "for" in depSet    

    def main_get_all_objs(self, v, is_pas):
        #====================================================
        # get all objects for an active/passive sentence
        #====================================================
        rights = list(v.rights)

        objs = [tok for tok in rights if tok.dep_ in OBJECTS or (is_pas and tok.dep_ == 'pobj')]
        objs.extend(self._get_objs_from_prepositions(rights, is_pas))

        potential_new_verb, potential_new_objs = self._get_obj_from_xcomp(rights, is_pas)
        if potential_new_verb is not None and potential_new_objs is not None and len(potential_new_objs) > 0:
            objs.extend(potential_new_objs)
            v = potential_new_verb
        if len(objs) > 0:
            objs.extend(self._get_objs_from_conjunctions(objs))
        return v, objs   

    def _get_objs_from_prepositions(self, deps, is_pas):
        #====================================================
        # prep => pobj, agent => prep => pobj
        #====================================================
        objs = []
        for dep in deps:
            if dep.pos_ == "ADP" and (dep.dep_ == "prep" or (is_pas and dep.dep_ == "agent")):
                objs.extend([tok for tok in dep.rights if tok.dep_  in OBJECTS or
                            (tok.pos_ == "PRON" and tok.lower_ == "me") or
                            (is_pas and tok.dep_ == 'pobj')])
        return objs   

    def _get_obj_from_xcomp(self, deps, is_pas):
        #====================================================
        # VERB, xcomp => dobj
        #====================================================
        for dep in deps:
            if dep.pos_ == "VERB" and dep.dep_ == "xcomp":
                v = dep
                rights = list(v.rights)
                objs = [tok for tok in rights if tok.dep_ in OBJECTS]
                objs.extend(self._get_objs_from_prepositions(rights, is_pas))
                if len(objs) > 0:
                    return v, objs
        return None, None  

    def _get_objs_from_conjunctions(self, objs):
        #====================================================
        # VERB => dobj
        #====================================================
        more_objs = []
        for obj in objs:
            rights = list(obj.rights)
            rightDeps = {tok.lower_ for tok in rights}
            if self.contains_conj(rightDeps):
                more_objs.extend([tok for tok in rights if tok.dep_ in OBJECTS or tok.pos_ == "NOUN"])
                if len(more_objs) > 0:
                    more_objs.extend(self._get_objs_from_conjunctions(more_objs))
        return more_objs           