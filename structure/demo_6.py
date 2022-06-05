from subject_verb_object_extract import findSVOs, nlp

str = "The Police Report related to the car accident is searched within the Police Report database and put in a file together with the Claim Documentation. This file serves as input to a claims handler who calculates an initial claim estimate. Then, the claims handler creates an Action Plan based on an Action Plan Checklist available in the Document Management system. Based on the Action Plan, a claims manager tries to negotiate a settlement on the claim estimate. The claimant is informed of the outcome, which ends the process."

#"{The Police Report related to the car accident} is {searched within the Police Report database} and put in a file together with the Claim Documentation. 
#[('the car accident', 'relate', 'The Police Report'), ('the Report database', 'search', 'The Police Report'), 
#[(SVO), (SVO)]

# {This file serves as input to a claims handler} {who calculates an initial claim estimate.}  
# ('input to a claims handler', 'serve', 'This file'), ('an initial claim estimate', 'calculate', 'who'),
#[(SVO), (SVO)]
 
# Then, {the claims handler creates an Action Plan} based on an Action Plan Checklist available in the Document Management system.   
# ('an Action Plan', 'create', 'the claims handler'),
#[Then (SVO)]

# Based on the Action Plan, {a claims manager tries to negotiate a settlement on the claim estimate.} 
# ('a settlement on the claim estimate', 'negotiate', 'a claims manager'), 
#[Based on (SVO)]

# The claimant is informed of {the outcome, which ends the process.}"
# ('the process', 'end', 'the outcome ,')]
#[(SVO)]

#=======================================================================
#[('the car accident', 'relate', 'The Police Report'), 
# ('the Report database', 'search', 'The Police Report'), 
# ('input to a claims handler', 'serve', 'This file'), 
# ('an initial claim estimate', 'calculate', 'who'), 
# ('an Action Plan', 'create', 'the claims handler'), 
# ('a settlement on the claim estimate', 'negotiate', 'a claims manager'), 
# ('the outcome ,', 'inform', 'The claimant'), 
# ('the process', 'end', 'the outcome ,')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)