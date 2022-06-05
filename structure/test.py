# l = ['A small company', 'some files', 'A small company']
# #_duplicates_subject : ['some files']

# #l=["A","A","B",4,5,2,3,4,7,9,5]
# l1=[]
# l2=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:
#         print(l1)

import spacy
nlp = spacy.load('en')    
sent = "Modi is a great leader.He has made India proud. Rahul Gandhi is naive . He is not fit to be prime minister."
doc=nlp(sent)

sub_toks = [tok for tok in doc if ((tok.dep_ == "nsubj") )]
print(sub_toks)

nc= [x for x in doc.noun_chunks]
print(nc)


l=[]
for i,token in enumerate(doc):
    if token.pos_ in ('PROPN','PRON'):
        l.append([token.text,i,token.pos_])        