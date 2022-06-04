# install : python -m spacy download en
# Load your usual SpaCy model (one of SpaCy English models)

import spacy
import neuralcoref

class NeuralCoref():
    def __init__(self, sentence):
        self.sentence = sentence
    
    def get_sentence(self):
        nlp = spacy.load('en')
        coref = neuralcoref.NeuralCoref(nlp.vocab)
        nlp.add_pipe(coref, name='neuralcoref')
        doc = nlp(self.sentence)
        resolved_text = doc._.coref_resolved
        sentences = [sent.string.strip() for sent in nlp(resolved_text).sents]
        append_sentence = ""
        for sentence in sentences: 
            append_sentence += " "+sentence
        return append_sentence