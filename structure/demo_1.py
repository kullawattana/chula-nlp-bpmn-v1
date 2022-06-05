from subject_verb_object_extract import findSVOs, nlp

str1 = "A small company manufactures customized bicycles."       

# tokens1 = nlp(str1)
# svos1 = findSVOs(tokens1)
# print("\n1")
# print(str1)
# print(svos1)

#================================================================
#Example : 
#Step 1.1 : Find word all
# ["A", "small", "company", "manufactures", "bicycles", "bicycles", "customized"]
#Step 1.2 : Find word V 
#["manufactures"]
#Step 1.3 : Find word relation
#["A", "small", "company"] <- ["manufactures"] -> ["bicycles"] -> ["bicycles", "customized"]
#Step 1.4 (ซ้าย - ขวา) 
#[('A small company', 'manufactures', 'bicycles'), ('bicycles', 'customized')]

#Step 1
#Check SVO
##      ('The Vacation Request Process', 'starts')
##      ('an employee of the organization', 'submits', 'a vacation request')
#Step 2
# Check Wording for Start Activity :: ['starts'] 
##      ('The Vacation Request Process', 'starts')
#Step 3
# Check Verb relation :: V -> advcl -> V :: ['starts','submits']
#Step 4
# Check Verb relation :: "When" <- advmod <- V :: ['When']
##      ('an employee of the organization', 'submits', 'a vacation request')

# str2 = "Whenever the sales department receives an order, a new process instance is created."       
# #[('an order', 'receive', 'the sales department'), ('a process instance', 'created')]
# #[Whenever (SV),(SV)]

# str3 = "A member of the sales department can then reject or accept the order for a customized bike."       
# #[('A member of the sales department', 'reject', 'the order for a customized bike'), ('A member of', 'accept', 'the order for')]
# #[(SVO),(SVO)]

# str4 = "In the former case, the process instance is finished."       
# #[('the process instance', 'finished')]
# #[In the former case, (SV)]

# str5 = "In the latter case, the storehouse and the engineering department are informed." 
# #[('the storehouse', 'informed'), ('the engineering department', 'informed')]      
# #[In the latter case, (SV), (SV)]

# str6 = "The storehouse immediately processes the part list of the order and checks the required quantity of each part."
# #[('The storehouse', 'processes', 'the part list of the order'), ('the quantity of each part', 'required')]
# #[(S V the part list of O), (S of each part V)]

# str7 = "If the part is available in-house, it is reserved."
# #[('house', 'be', 'the part'), ('it', 'reserved')]
# #[If (S V O), (S V)]

# str8 = "If it is not available, it is back-ordered."
# #[('it', '!is')]
# #[If (S V O), (S V O)]

# str9 = "This procedure is repeated for each item on the part list."
# #[('each item', 'repeat', 'This procedure'), ('the part list', 'repeat', 'This procedure')]
# #[(S V O), (S V O)]

# str10 = "In the meantime, the engineering department prepares everything for the assembling of the ordered bicycle."
# #[('the engineering department', 'prepares', 'everything'), ('the bicycle', 'ordered')]
# #[In the meantime, (S V O), (S V O)]

# str11 = "If the storehouse has successfully reserved or back-ordered every item of the part list and the preparation activity has finished, the engineering department assembles the bicycle."
# #[('the preparation activity', 'finished'), ('the engineering department', 'assembles', 'the bicycle')]
# #[If (S V O), (S V O)]

# str12 = "Afterwards, the sales department ships the bicycle to the customer and finishes the process instance."
# #[('Afterwards , the department ships bicycle to the customer', 'finishes', 'the process instance')]
# #[Afterwards, (S V O)]