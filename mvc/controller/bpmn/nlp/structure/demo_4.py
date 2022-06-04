from subject_verb_object_extract import findSVOs, nlp

str1 = "After a claim is registered, it is examined by a claims officer."
#[('a claim', 'registered'), ('a claims officer', 'examine', 'it')]
#[After (SVO),(SVO)]

str2 = "The claims officer then writes a “settlement recommendation”."
#[('The claims officer', 'writes', 'a “ settlement recommendation ”')]
#[(SVO)]

str3 = "This recommendation is then checked by a senior claims officer who may mark the claim as “OK” or “Not OK”."
#[('a senior claims officer', 'check', 'This recommendation'), ('the claim as', 'mark', 'who')]
#[(SVO),(SVO)]

str4 = "If the claim is marked as “Not OK”, it is sent back to the claims officer and the recommendation is repeated."
#[('the claim', 'marked'), ('it', 'sent'), ('the recommendation', 'repeated')]
#[If (SVO),(SVO) and (SVO)]

str5 = "If the claim is OK, the claim handling process proceeds."
#[('the claim', 'is'), ('claim', 'handling', 'process proceeds')]
#[If (SVO),(SVO)]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)