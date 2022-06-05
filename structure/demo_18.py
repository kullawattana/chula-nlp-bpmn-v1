from subject_verb_object_extract import findSVOs, nlp

str = "In the treasury minister’s office, once a ministerial inquiry has been received, it is first registered into the system. Then the inquiry is investigated so that a ministerial response can be prepared. The finalization of a response includes the preparation of the response itself by the cabinet officer and the review of the response by the principal registrar. If the registrar does not approve the response, the latter needs to be prepared again by the cabinet officer for review. The process finishes only once the response has been approved."

#========================================
#ไม่มี Verb ทำให้ไม่สามารถตัดคำได้
#In the treasury minister’s office, [once {a ministerial inquiry} has been {received}, {it} is first {registered} into the system}].
#[('a ministerial inquiry', 'received'), ('the system', 'register', 'it'), 
# [once (SVO), (SVO)]

#Then [{the inquiry is investigated} so that {a ministerial response can be prepared}]
# ('the inquiry', 'investigated'), ('a ministerial response', 'prepared'), 
# [Then (SVO) so that (SVO)]

# {The finalization of a response includes the preparation of the response itself by the cabinet officer} and the review of the response by the principal registrar. 
# ('the preparation of the response itself by the cabinet officer', 'include', 'The finalization of a response'), 
# [(SVO) and (SVO)]

# If {the registrar does not approve the response}, {the latter needs to be prepared again by the cabinet officer for review.} 
# ('the response', '!approve', 'the registrar'), ('the cabinet officer for review', 'prepare', 'the latter'),
# [If (SVO), (SVO)]

# {The process finishes} only once {the response has been approved}.
# ('The process', 'finishes'), ('the response', 'approved')]
# [(SVO) only once (SVO)]

#========================================
#[('a ministerial inquiry', 'received'), 
# ('the system', 'register', 'it'), 
# ('the inquiry', 'investigated'), 
# ('a ministerial response', 'prepared'), 
# ('the preparation of the response itself by the cabinet officer', 'include', 'The finalization of a response'), 
# ('the response', '!approve', 'the registrar'), 
# ('the cabinet officer for review', 'prepare', 'the latter'), 
# ('The process', 'finishes'), 
# ('the response', 'approved')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)