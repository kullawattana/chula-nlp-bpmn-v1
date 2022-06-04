from subject_verb_object_extract import findSVOs, nlp

str = "First, the Manager checks the open leads. Afterwards, he selects the top five ones. He then tells his Sales Assistant to call the contact person of the leads. The Sales Assistant calls each customer. If someone is interested, he sends a note to the Manager. The Manager then processes the lead. Otherwise, he calls the next customer."

#First, the Manager checks the open leads. 
# Afterwards, he selects the top five ones. 
# He then tells his Sales Assistant to call the contact person of the leads. 
# The Sales Assistant calls each customer. 
# If someone is interested, he sends a note to the Manager. 
# The Manager then processes the lead. Otherwise, he calls the next customer."

#First, {the Manager checks} {the open leads.} 
#[('the Manager', 'checks'), ('the open', 'leads'), 
#[First (SVO), (SVO)]

# Afterwards, {he selects the top five ones.} 
# ('he', 'selects', 'the top five ones'), 
#[Afterwards (SVO)]

# {He then tells his Sales Assistant} to {call the contact person of the leads.}
# ('He', 'call', 'his Sales Assistant'), ('He', 'call', 'the contact person of the leads'),
#[(SVO),(SVO)] 

# The Sales Assistant calls each customer. 
#('The Sales Assistant', 'calls', 'each customer'), 
#[(SVO)] 

# If someone is interested, he sends a note to the Manager. 
# ('someone', 'is'), ('he', 'sends', 'a note'), 
#[If (SVO), (SVO)]

# The Manager then processes the lead. 
# ('The Manager', 'processes', 'the lead'), 
#[(SVO)]

# Otherwise, he calls the next customer."
# ('he', 'calls', 'the next customer')]
#[Otherwise, (SVO)]

#=================================================
#[('the Manager', 'checks'), 
# ('the open', 'leads'), 
# ('he', 'selects', 'the top five ones'), 
# ('He', 'call', 'his Sales Assistant'), 
# ('He', 'call', 'the contact person of the leads'),
# ('The Sales Assistant', 'calls', 'each customer'), 
# ('someone', 'is'), ('he', 'sends', 'a note'), 
# ('The Manager', 'processes', 'the lead'), 
# ('he', 'calls', 'the next customer')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)