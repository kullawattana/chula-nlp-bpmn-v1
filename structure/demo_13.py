from subject_verb_object_extract import findSVOs, nlp

str = "As soon as an invoice is received from a customer, it needs to be checked for mismatches. The check may result in either of these three options: i) there are no mismatches, in which case the invoice is posted; ii) there are mismatches but these can be corrected, in which case the invoice is re-sent to the customer; and iii) there are mismatches but these cannot be corrected, in which case the invoice is blocked. Once one of these three activities is performed the invoice is parked and the process completes."

#As soon as {an invoice is received from a customer}, {it needs to be checked for mismatches.} 
#[('a customer', 'receive', 'an invoice'), 
# ('mismatches', 'check', 'it'), 
# [As soon as, (SVO), (SVO)] 

#The check may result in either of these three options: 
# ('either of these three options', 'result', 'The check'), 
# [(SVO)] 

# i) there are no mismatches, in which case {the invoice is posted}; 
# ('the invoice', 'posted'), 
# [in which case (SVO)] 

# ii) there are mismatches but these can be corrected, in which case {the invoice is re-sent} to the customer;
# ('the invoice', 're'), 
# [in which case (SVO)] 

# iii) {there are mismatches} but these cannot be corrected, in which case {the invoice is blocked.} 
# ('mismatches', 'be', 'there'), ('the invoice', 'blocked'), 
# [in which case (SVO)] 

# {Once one of these three activities is performed} the invoice is parked and {the process completes.}"
# ('one of these three activities', 'performed'), ('the process', 'completes')]
# [(SVO),(SVO)] 

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)