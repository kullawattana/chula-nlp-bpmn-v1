import spacy
from extract.get_verb import GetVerb
from extract.get_mark import GetMark

class GetPatternCuttingSentence():
    def __init__(self, sentence):
        self.nlp = spacy.load('en_core_web_sm')
        self.sentence = str(sentence)
        self.doc = self.nlp(self.sentence)

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

    def filter_pattern_cutting_sentence(self):
        """
        Find V, V, V, ...
        Find mark, advmod
        """
        doc = self.merge_phrases()
        doc = self.merge_punct()
        v = GetVerb()
        m = GetMark()

        for sent in doc.sents:
            words = []
            jsons_word = []
            verbs = v.main_find_verbs(sent)          #[reject, accept]
            for v in verbs:
                words += m.is_mark(v)
            words += ["."]
            jsons_word = {"patterns": words}
            ls = self.filter_words(jsons_word)
            order_list_sentence = self.get_sentence_result(ls)      
        return order_list_sentence  

    def get_sentence_result(self, ls):
        order_list_sentence = []
        list_flow_id = self.filter_pattern(ls)
        for _, value in list_flow_id.items():
            start, end = self.cutting_sentence_start_end(value[0], value[1]) 
            text = self.sentence
            sentence = text[start:end]
            order_list_sentence.append(str(sentence))  
        return order_list_sentence   

    def filter_words(self, jsons_word):
        ls = []
        for _, value in jsons_word.items():
            for word in value:
                if str(word) in ["If","otherwise","else",",",";","."]:
                    w = str(word)+"|"
                    ls.append(w)
                elif str(word) in ["afterwards","later","next","and","or",",",";","."]:
                    w = str(word)+"|"
                    ls.append(w)
                elif str(word) in ["After","Upon","Once","When","when",",",";","."]:
                    w = str(word)+"|"
                    ls.append(w)
                elif str(word) in ["If","Whether","Unless","In case","In case of","In the former case","In the case of","Whereas","Optionally","for the case",",",";","."]:
                    w = str(word)+"|"
                    ls.append(w)
                elif str(word) in ["Whenever",",",";","."]:
                    w = str(word)+"|"
                    ls.append(w)
        return ls    

    def filter_pattern(self, data):
        json_dict = JsonDictionary()
        result = ([x + y for x, y in zip(data, data[1:] + data[:0])])

        re = []
        for ls in result:
            re.append(ls[:-1])

        #composed data
        x = []
        for (i, item) in enumerate(re):
            a = (i, str(item).split('|'))
            x.append(a)

        #generate flow id
        i = 0
        for _, value in x:
            i += 1
            json_dict.add("Flow_"+str(i), value)
        return json_dict    

    def cutting_sentence_start_end(self, value_start, value_end):
        start = self.sentence.index(value_start)
        text = self.sentence
        end = text.index(value_end,start+1)
        return start, end

class JsonDictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value        