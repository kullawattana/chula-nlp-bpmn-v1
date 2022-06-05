from subject_verb_object_extract import findSVOs, nlp

str1 = "The party sends a warrant possession request asking a warrant to be released."  
#[('a warrant possession request', 'send', 'The party'), ('a warrant', 'ask', 'a warrant possession request'), ('a warrant', 'released')]
#[(SVO),(SVO),(SV)]

str2 = "The Client Service Back Office as part of the Small Claims Registry Operations receives the request and retrieves the SCT file."
#[('The Service Back Office as part of', 'receives', 'the request')]
#[(S as part of V O)]
 
str3 = "Then, the SCT Warrant Possession is forwarded to Queensland Police."  
#[('Queensland Police', 'forward', 'the SCT Warrant Possession')]
#[Then (SVO)]

str4 = "The SCT physical file is stored by the Back Office awaiting a report to be sent by the Police."
#[('the Back Office', 'await', 'The SCT physical file'), ('a report', 'await', 'The SCT physical file'), ('the Police', 'send', 'a report')]
#[(SVO),(SVO),(SVO)]

str5 = "When the report is received, the respective SCT file is retrieved."
#[('the report', 'received'), ('the respective SCT file', 'retrieved')]
#[When (SV),(SV)]

str6 = "Then, Back Office attaches the new SCT document, and stores the expanded SCT physical file."
#[('Back Office', 'attaches', 'the new SCT document'), ('the file', 'expanded')]
#[Then (SV),(SV)]

str7 = "After that, some other MC internal staff receives the physical SCT file (out of scope)."
#[('some other MC internal staff', 'receives', 'the physical SCT file (')]
#[After that (SV),(SV)]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)