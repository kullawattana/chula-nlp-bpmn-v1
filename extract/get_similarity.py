import spacy

class GetSimilarity():
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.similar_list = []

    def get_similarity(self, duplicates_subject, new_subject_list):
        #==================================================================================================================
        #If have similarity more than 0.60 then add subject into new_svos.append((_subs, svo[2], svo[3])) for create
        #If have similarity less than 0.60 then ignore
        #==================================================================================================================
        for _dup in duplicates_subject:
            for _new in new_subject_list:
                doc1 = self.nlp(_dup)
                doc2 = self.nlp(_new)
                similar = doc1.similarity(doc2)
                print(similar, "|", _dup, "|", _new)
                if similar > 0.60:
                    self.similar_list.append(_dup)
                else:    
                    self.similar_list.append(_new)       
        return self.similar_list