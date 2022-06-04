from subject_verb_object_extract import findSVOs, nlp

str = "The process starts when a customer submits a claim by sending in relevant documentation. The Notification department at the car insurer checks the documents upon completeness and registers the claim. Then, the Handling department picks up the claim and checks the insurance. Then, an assessment is performed. If the assessment is positive, a garage is phoned to authorize the repairs and the payment is scheduled (in this order). Otherwise, the claim is rejected. In any case (whether the outcome is positive or negative), a letter is sent to the customer and the process is considered to be complete."

#"{The process starts} when {a customer submits a claim} by sending in relevant documentation. 
#[('The process', 'starts'), ('a claim', 'submit', 'a customer'), 
#[(SV) when (SVO)]

# {The Notification department at the car insurer checks the documents} upon completeness and registers the claim.
# ('the documents', 'check', 'The Notification department at the car insurer'), 
#[(SVO)]

# Then, {the Handling department picks up the claim} and checks the insurance. 
# ('the claim', 'pick', 'the Handling department'), 
#[Then (SVO) and (SVO)]

# Then, an assessment is performed. 
# ('an assessment', 'performed'), 
#[Then (SVO)]

# If {the assessment is} positive, {a garage is phoned} to authorize the repairs and {the payment is scheduled (in this order)}. 
# ('the assessment', 'is'), ('a garage', 'phoned'), ('this order', 'schedule', 'the payment'), 
#[If (SVO), (SVO) and (SVO)]

# Otherwise, the claim is rejected. 
# ('the claim', 'rejected'), 
#[Otherwise (SVO), (SVO) and (SVO)]

# In any case (whether {the outcome is} positive or negative), {a letter is sent to the customer} and {the process is considered} to be complete."
# ('the outcome', 'is'), ('the customer', 'send', 'a letter'), ('the process', 'considered')]
#[In any case (SVO), (SVO), (SVO)]

#=============================================================================
#[('The process', 'starts'), 
# ('a claim', 'submit', 'a customer'), 
# ('the documents', 'check', 'The Notification department at the car insurer'), 
# ('the claim', 'pick', 'the Handling department'), 
# ('an assessment', 'performed'), 
# ('the assessment', 'is'), 
# ('a garage', 'phoned'), 
# ('this order', 'schedule', 'the payment'), 
# ('the claim', 'rejected'), 
# ('the outcome', 'is'), 
# ('the customer', 'send', 'a letter'), 
# ('the process', 'considered')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)