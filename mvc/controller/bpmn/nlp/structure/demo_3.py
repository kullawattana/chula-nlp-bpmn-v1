from subject_verb_object_extract import findSVOs, nlp

str1 = "Each morning, the files which have yet to be processed need to be checked, to make sure they are in order for the court hearing that day." 
#[('the files', 'have'), ('the files', 'processed'), ('morning , files need', 'checked'), ('morning , files need', 'make')]
#[(SV),(SV),(SV),(SV)]

str2 = "If some files are missing, a search is initiated, otherwise the files can be physically tracked to the intended location."
#[('some files', 'missing'), ('a search', 'initiated'), ('the location', 'track', 'the files'), ('the location', 'intended')]
#[If (SV),(SV),(SVO),(SV)]

str3 = "Once all the files are ready, these are handed to the Associate, and meantime the Judges Lawlist is distributed to the relevant people."
#[('all the files', 'are'), ('the relevant people', 'distribute', 'the Judges Lawlist')]
#[Once (SV),(SVO)]

str = "Afterwards, the directions hearings are conducted."
#[('the directions hearings', 'conducted')]
#[Afterwards, (SVO)]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)