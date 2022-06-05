from subject_verb_object_extract import findSVOs, nlp

str = "Once the boarding pass has been received, passengers proceed to the security check. Here they need to pass the personal security screening and the luggage screening. Afterwards, they can proceed to the departure level."

#"Once the boarding pass has been received, passengers proceed to the security check. 
# Here they need to pass the personal security screening and the luggage screening. 
# Afterwards, they can proceed to the departure level."

#Once {the boarding pass has been received}, {passengers proceed to the security check.}
#[('the boarding pass', 'received'), ('the security check', 'proceed', 'passengers'), 
#[Once, (SV), (SVO)]

# Here {they need to pass the personal security screening} and {the luggage screening.} 
# ('the security screening', 'pass', 'they'), ('the luggage screening', 'pass', 'they'),
# [(SVO), (SVO)] 

# Afterwards, {they can proceed to the departure level.}
# ('the departure level', 'proceed', 'they')]
# [Afterwards, (SVO)] 

#====================================================
#[('the boarding pass', 'received'), 
# ('the security check', 'proceed', 'passengers'), 
# ('the security screening', 'pass', 'they'), 
# ('the luggage screening', 'pass', 'they'), 
# ('the departure level', 'proceed', 'they')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)