from mock_phrases import MockPhrases
from neural_coref import NeuralCoref

#Scenario 1 =========================================================
#sentence = "A small company manufactures customized bicycles."   
# nsubj A small company
# ROOT manufactures
# dobj customized bicycles
# punct .
#[(1, 'A small company', 'manufactures', customized bicycles, 'VO_', 'isActive', '')]    

#sentence = "Whenever the sales department receives an order, a new process instance is created."
# advmod Whenever
# nsubj the sales department
# advcl receives
# dobj an order
# punct ,
# nsubjpass a new process instance
# auxpass is
#[(1, 'the sales department', 'receives', an order, 'VO_', 'isActive', 'Whenever'), (2, '-', 'created', a new process instance, 'VO_', '')]
#[(1, 'the sales department', 'receives', an order, 'ExclusiveGateway_', 'isActive', 'Whenever'), (2, '-', 'created', a new process instance, 'ExclusiveGateway_', '')]

#sentence = "In the former case, the process instance is finished."
# prep In
# pobj the former case
# punct ,
# nsubjpass the process instance
# auxpass is
#[(1, '-', 'finished', the process instance, 'VO_', '')]

#sentence = "In the latter case, the storehouse and the engineering department are informed."
# prep In
# pobj the latter case
# punct ,
# nsubjpass the storehouse
# cc and
# conj the engineering department
# auxpass are
#[(1, '-', 'informed', the storehouse, 'VO_', ''), (1, '-', 'informed', the engineering department, 'VO_', '')]

#sentence = "The storehouse immediately processes the part list of the order and checks the required quantity of each part."
#[(1, 'The storehouse', processes, [], 'VO_', 'isActive', ''), 
# (1, 'The storehouse', 'checks', the required quantity of each part, 'VO_', 'isActive', ''), 
# (2, '-', checks, the required quantity, 'VO_', 'isActive', '')]
# nsubj The storehouse
# advmod immediately
# ROOT processes
# dobj the part list
# prep of
# pobj the order
# cc and
# conj checks
# dobj the required quantity
# prep of
# pobj each part
# punct .

#sentence = "If the part is available in-house, it is reserved."
#[(1, 'the part', 'is', house, 'VO_', 'isPassive', ''), (2, '-', 'reserved', it, 'VO_', '')]

#sentence = "If it is not available, it is back-ordered."
# mark If
# nsubj it
# advcl is
# neg not
# acomp available
# punct ,
# nsubj it
# ROOT is
# advmod back
# punct -
# acomp ordered
# punct .
#[(1, '-', '!is', it, 'VO_', '')]

#sentence = "This procedure is repeated for each item on the part list."
#[(1, 'This procedure', 'repeated', each item, 'VO_', 'isPassive', ''), (1, 'This procedure', 'repeated', the part list, 'VO_', 'isPassive', '')]
# nsubjpass This procedure
# auxpass is

#sentence = "In the meantime, the engineering department prepares everything for the assembling of the ordered bicycle."
#[(1, 'the engineering department', prepares, everything for the assembling, 'VO_', 'isActive', of the ordered bicycle)]

#sentence = "If the storehouse has successfully reserved or back-ordered every item of the part list and the preparation activity has finished, the engineering department assembles the bicycle."
#เก่า
#[(3, '-', 'finished', the preparation activity, 'ExclusiveGateway_', ''), 
# (4, 'the engineering department', 'assembles', the bicycle, 'ExclusiveGateway_', 'isActive', '')]

#ใหม่
# [(1, 'the storehouse', reserved, [], 'ExclusiveGateway_', 'isActive', ''), 
# (1, 'the storehouse', 'ordered', every item of the part list, 'ExclusiveGateway_', 'isActive', ''), 
# (3, '-', 'finished', the preparation activity, 'ExclusiveGateway_', 'isPassive', ''), 
# (4, 'the engineering department', assembles, every item of the part list, 'ExclusiveGateway_', 'isActive', '')]

# mark If
# nsubj the storehouse
# aux has
# advmod successfully
# advcl reserved
# cc or
# advmod back
# punct -
# conj ordered
# dobj every item
# prep of
# pobj the part list
# cc and
# nsubj the preparation activity
# aux has
# ccomp finished
# punct ,
# nsubj the engineering department
# ROOT assembles
# dobj the bicycle
# punct .

#sentence = "Afterwards, the sales department ships the bicycle to the customer and finishes the process instance."
# ROOT Afterwards, the sales department ships
# appos the bicycle
# prep to
# pobj the customer
# cc and
# conj finishes
# dobj the process instance
# punct .
# [(1, 'Afterwards, the sales department ships', 'finishes', the process instance, 'VO_', 'isActive', '')]

#Scenario 3 =========================================================
#sentence = "Each morning, the files which have yet to be processed need to be checked, to make sure they are in order for the court hearing that day."
#[(1, '-', 'have', the files, 'VO_', 'isActive', ''), 
# (2, '-', 'processed', the files, 'VO_', 'isPassive', ''), 
# (3, '-', 'checked', need, 'VO_', 'isPassive', ''),            X
# (4, '-', 'make', need, 'VO_', 'isActive', '')]

#sentence = "If some files are missing, a search is initiated, otherwise the files can be physically tracked to the intended location."
#[(1, '-', 'missing', some files, 'VO_', 'isPassive', ''), 
# (2, '-', 'initiated', a search, 'VO_', 'isPassive', ''),      X
# (3, 'the files', 'tracked', the intended location, 'VO_', 'isPassive', '')]       X

#sentence = "Once all the files are ready, these are handed to the Associate, and meantime the Judges Lawlist is distributed to the relevant people."
# advmod Once
# nsubj all the files
# advcl are
# acomp ready
# punct ,
# nsubjpass these
# auxpass are
# VERB : are
# VERB : handed
# VERB : distributed
#[(1, '-', 'are', all the files, 'ExclusiveGateway_', 'isPassive', 'Once'), 
# (3, 'the Judges Lawlist', 'distributed', the relevant people, 'ExclusiveGateway_', 'isPassive', 'meantime')] X

#sentence = "Afterwards, the directions hearings are conducted."
#[(1, '-', 'conducted', the directions hearings, 'VO_', 'isPassive', '')]

#Scenario 4 =========================================================
##sentence = "After a claim is registered, it is examined by a claims officer. The claims officer then writes a “settlement recommendation”. This recommendation is then checked by a senior claims officer who may mark the claim as “OK” or “Not OK”. If the claim is marked as “Not OK”, it is sent back to the claims officer and the recommendation is repeated. If the claim is OK, the claim handling process proceeds."
#[(1, '-', 'registered', a claim, 'VO_', 'isPassive', ''), 
# (2, 'it', 'examined', a claims officer, 'VO_', 'isPassive', ''), 
# (3, 'The claims officer', 'writes', a “settlement recommendation, 'VO_', 'isActive', ''), 
# (4, 'This recommendation', 'checked', a senior claims officer, 'VO_', 'isPassive', ''), 
# (5, '-', 'mark', the claim, 'VO_', 'isActive', ''), 
# (6, '-', 'marked', the claim, 'VO_', 'isPassive', ''), 
# (7, 'it', sent, '', 'VO_', 'isActive', ''), 
# (7, 'it', 'repeated', '', 'VO_', 'isActive', ''), 
# (7, '-', 'sent', it, 'VO_', 'isPassive', ''), 
# (8, '-', 'repeated', the recommendation, 'VO_', 'isPassive', ''), 
# (9, '-', 'is', the claim, 'VO_', 'isPassive', ''), 
# (10, 'claim', 'handling', process proceeds, 'VO_', 'isPassive', '')]

#sentence = "After a claim is registered, it is examined by a claims officer."
#[(1, '-', 'registered', a claim, 'VO_', 'isPassive', ''), 
# (2, 'it', 'examined', a claims officer, 'VO_', 'isPassive', '')]

#sentence = "The claims officer then writes a “settlement recommendation”."
#[(1, 'The claims officer', 'writes', a “settlement recommendation, 'VO_', 'isActive', '')]

#sentence = "This recommendation is then checked by a senior claims officer who may mark the claim as “OK” or “Not OK”."
#[(1, 'This recommendation', 'checked', a senior claims officer, 'VO_', 'isPassive', ''), 
# (2, '-', 'mark', the claim, 'VO_', 'isActive', '')]

#sentence = "If the claim is marked as “Not OK”, it is sent back to the claims officer and the recommendation is repeated."
#[(1, '-', 'marked', the claim, 'VO_', 'isPassive', ''), 
# (2, 'it', sent, '', 'VO_', 'isActive', ''), 
# (2, 'it', 'repeated', '', 'VO_', 'isActive', ''), 
# (2, '-', 'sent', it, 'VO_', 'isPassive', ''), 
# (3, '-', 'repeated', the recommendation, 'VO_', 'isPassive', '')]

#sentence = "If the claim is OK, the claim handling process proceeds."
#[(1, '-', 'is', the claim, 'VO_', 'isPassive', ''), 
# (2, 'claim', 'handling', process proceeds, 'VO_', 'isPassive', '')]

#Scenario 5 =========================================================
## sentence = "When a claim is received, it is first checked whether the claimant is insured by the organization. If not, the claimant is informed that the claim must be rejected. Otherwise, the severity of the claim is evaluated. Based on the outcome (simple or complex claims), relevant forms are sent to the claimant. Once the forms are returned, they are checked for completeness. If the forms provide all relevant details, the claim is registered in the Claims Management system, which ends the Claims Notification process. Otherwise, the claimant is informed to update the forms. Upon reception of the updated forms, they are checked again."
#[(1, '-', 'received', a claim, 'ExclusiveGateway_', 'isPassive', 'When'), 
# (2, '-', 'checked', it, 'ExclusiveGateway_', 'isPassive', ''), 
# (3, 'the claimant', 'insured', the organization, 'ExclusiveGateway_', 'isPassive', ''), 
# (4, '-', '!informed', the claimant, 'ExclusiveGateway_', 'isPassive', ''), 
# (5, '-', 'rejected', the claim, 'ExclusiveGateway_', 'isPassive', ''), 
# (6, '-', 'evaluated', the severity, 'ExclusiveGateway_', 'isPassive', ''), 
# (8, 'relevant forms', 'sent', the claimant, 'ExclusiveGateway_', 'isPassive', ''), 
# (9, '-', 'returned', the forms, 'ExclusiveGateway_', 'isPassive', 'Once'), 
# (10, 'they', 'checked', completeness, 'ExclusiveGateway_', 'isPassive', ''), 
# (11, 'the forms', 'provide', all relevant details, 'ExclusiveGateway_', 'isActive', ''), 
# (12, 'the claim', 'registered', the Claims Management system, 'ExclusiveGateway_', 'isPassive', ''), 
# (13, 'the Claims Management system', 'ends', the Claims Notification process, 'ExclusiveGateway_', 'isActive', ''), 
# (14, 'the claimant', 'update', the forms, 'ExclusiveGateway_', 'isActive', ''), 
# (16, '-', 'checked', they, 'ExclusiveGateway_', 'isPassive', 'Upon')]

#sentence = "When a claim is received, it is first checked whether the claimant is insured by the organization."
#[(1, '-', 'received', a claim, 'ExclusiveGateway_', 'isPassive', 'When'), 
# (2, '-', 'checked', it, 'ExclusiveGateway_', 'isPassive', ''), 
# (3, 'the claimant', 'insured', the organization, 'ExclusiveGateway_', 'isPassive', '')]

#sentence = "If not, the claimant is informed that the claim must be rejected."
#[(1, '-', '!informed', the claimant, 'VO_', 'isPassive', ''), 
# (2, '-', 'rejected', the claim, 'VO_', 'isPassive', '')]

#sentence = "Otherwise, the severity of the claim is evaluated."
#[(1, '-', 'evaluated', the severity, 'VO_', 'isPassive', '')]

#sentence = "Based on the outcome (simple or complex claims), relevant forms are sent to the claimant."
#[(2, 'relevant forms', 'sent', the claimant, 'VO_', 'isPassive', '')]

#sentence = "Once the forms are returned, they are checked for completeness."
#[(1, '-', 'returned', the forms, 'ExclusiveGateway_', 'isPassive', 'Once'), 
# (2, 'they', 'checked', completeness, 'ExclusiveGateway_', 'isPassive', '')]

#sentence = "If the forms provide all relevant details, the claim is registered in the Claims Management system, which ends the Claims Notification process."
#[(1, 'the forms', 'provide', all relevant details, 'VO_', 'isActive', ''), 
# (2, 'the claim', 'registered', the Claims Management system, 'VO_', 'isPassive', ''), 
# (3, 'the Claims Management system', 'ends', the Claims Notification process, 'VO_', 'isActive', '')]

#sentence = "Otherwise, the claimant is informed to update the forms."
#[(1, 'the claimant', 'update', the forms, 'VO_', 'isActive', '')]

#sentence = "Upon reception of the updated forms, they are checked again."
#[(1, '-', 'checked', they, 'ExclusiveGateway_', 'isPassive', 'Upon')]

#Scenario 6 =========================================================
##sentence = "The Police Report related to the car accident is searched within the Police Report database and put in a file together with the Claim Documentation. This file serves as input to a claims handler who calculates an initial claim estimate. Then, the claims handler creates an Action Plan based on an Action Plan Checklist available in the Document Management system. Based on the Action Plan, a claims manager tries to negotiate a settlement on the claim estimate. The claimant is informed of the outcome, which ends the process."
#[(1, 'The Police Report', related, a settlement on the claim estimate, 'VO_', 'isActive', ''), 
# (2, 'The Police Report', searched, a settlement on the claim estimate, 'VO_', 'isActive', ''), 
# (2, 'The Police Report', 'put', a settlement on the claim estimate, 'VO_', 'isActive', ''), 
# (4, 'This file', serves, a settlement on the claim estimate, 'VO_', 'isActive', ''), 
# (5, 'who', calculates, a settlement on the claim estimate, 'VO_', 'isActive', ''), 
# (6, 'the claims handler', creates, a settlement on the claim estimate, 'VO_', 'isActive', ''), 
# (9, 'a claims manager', tries, a settlement on the claim estimate, 'VO_', 'isActive', ''), 
# (11, 'The claimant', informed, a settlement on the claim estimate, 'VO_', 'isActive', ''), 
# (12, 'the outcome', ends, a settlement on the claim estimate, 'VO_', 'isActive', '')]

#sentence = "The Police Report related to the car accident is searched within the Police Report database and put in a file together with the Claim Documentation."
#[(1, 'The Police Report', 'related', the car accident, 'VO_', 'isPassive', ''), 
# (2, 'The Police Report', searched, '', 'VO_', 'isActive', ''), 
# (2, 'The Police Report', 'put', '', 'VO_', 'isActive', ''), 
# (2, 'The Police Report', 'searched', the Police Report database, 'VO_', 'isPassive', '')]

#sentence = "This file serves as input to a claims handler who calculates an initial claim estimate."
#[(1, 'This file', 'serves', input, 'VO_', 'isActive', ''), 
# (2, '-', 'calculates', an initial claim estimate, 'VO_', 'isActive', '')]

#ต้องแก้
#sentence = "Then, the claims handler creates an Action Plan based on an Action Plan Checklist available in the Document Management system."
# advmod Then
# punct ,
# nsubj the claims handler
# ROOT creates
# dobj an Action Plan
# acl based
# prep on
# pobj an Action Plan Checklist
# amod available
# prep in
# pobj the Document Management system
# punct .
# VERB : creates
# SEQUENCE : 1
# 5xxxxxxxx
# VERB : based
# SEQUENCE : 2
# [(1, 'the claims handler', 'creates', an Action Plan, 'VO_', 'isActive', '')]

#ต้องแก้
#sentence = "Based on the Action Plan, a claims manager tries to negotiate a settlement on the claim estimate."
# prep Based
# prep on
# pobj the Action Plan
# punct ,
# nsubj a claims manager
# ROOT tries
# aux to
# xcomp negotiate
# dobj a settlement
# prep on
# pobj the claim estimate
# punct .
# VERB : Based
# SEQUENCE : 1
# VERB : tries
# SEQUENCE : 2
# 4xxxxxxxx
# VERB : negotiate
# SEQUENCE : 3
# [(2, 'a claims manager', tries, a settlement on the claim estimate, 'VO_', 'isActive', '')]

#sentence = "The claimant is informed of the outcome, which ends the process."
# nsubjpass The claimant
# auxpass is
# VERB : informed
# SEQUENCE : 1
# 6xxxxxxxx
# VERB : ends
# SEQUENCE : 2
# 5xxxxxxxx
# [(1, 'The claimant', 'informed', the outcome, 'VO_', 'isPassive', ''), 
# (2, 'the outcome', 'ends', the process, 'VO_', 'isActive', '')]

#Scenario7 =========================================================
#sentence = "The process starts when a customer submits a claim by sending in relevant documentation. The Notification department at the car insurer checks the documents upon completeness and registers the claim. Then, the Handling department picks up the claim and checks the insurance. Then, an assessment is performed. If the assessment is positive, a garage is phoned to authorize the repairs and the payment is scheduled (in this order). Otherwise, the claim is rejected. In any case (whether the outcome is positive or negative), a letter is sent to the customer and the process is considered to be complete."
#[(1, '-', 'starts', The process, 'VO_', 'isActive', ''), 
# (2, 'a customer', submits, the documents upon completeness, 'VO_', 'isActive', ''), 
# (3, '-', sending, relevant documentation, 'VO_', 'isPassive', ''), 
# (4, 'The Notification department', checks, the documents upon completeness, 'VO_', 'isActive', ''), 
# (5, '-', registers, the claim, 'VO_', 'isActive', ''), 
# (6, 'the Handling department', picks, the documents upon completeness, 'VO_', 'isActive', ''), 
# (7, '-', checks, the insurance, 'VO_', 'isActive', ''), 
# (8, '-', 'performed', an assessment, 'VO_', 'isPassive', ''), 
# (9, '-', 'is', the assessment, 'VO_', 'isPassive', ''), 
# (10, '-', 'phoned', a garage, 'VO_', 'isPassive', ''), 
# (11, '-', authorize, the repairs, 'VO_', 'isActive', ''), 
# (12, 'the payment', scheduled, the documents upon completeness, 'VO_', 'isActive', ''), 
# (13, '-', 'rejected', the claim, 'VO_', 'isPassive', ''), 
# (14, '-', 'is', the outcome, 'VO_', 'isPassive', ''), 
# (15, 'a letter', sent, the documents upon completeness, 'VO_', 'isActive', to the customer), 
# (16, '-', 'considered', the process, 'VO_', 'isPassive', '')]

#Scenario8 =========================================================
#sentence = "Every time we get a new order from the sales department, first, one of my masters determines the necessary parts and quantities as well as the delivery date. Once that information is present, it has to be entered into our production planning system (PPS). It optimizes our production processes and creates possibly uniform work packages so that the setup times are minimized. Besides, it creates a list of parts to be procured. Unfortunately it is not coupled correctly to our Enterprise Resource Planning system (ERP), so the data must be transferred manually. By the way, that is the second step. Once all the data is present, we need to decide whether any parts are missing and must be procured or if this is not necessary. Once production is scheduled to start, we receive a notice from the system and an employee takes care of the implementation. Finally, the order will be checked again for its quality."
# SEQUENCE : 1
# VERB : determines
# SEQUENCE : 2
# VERB : is
# SEQUENCE : 3
# VERB : has
# SEQUENCE : 4
# VERB : entered
# SEQUENCE : 5
# VERB : optimizes
# SEQUENCE : 6
# VERB : creates
# SEQUENCE : 7
# VERB : minimized
# SEQUENCE : 8
# VERB : creates
# SEQUENCE : 9
# VERB : procured
# SEQUENCE : 10
# VERB : coupled
# SEQUENCE : 11
# VERB : transferred
# SEQUENCE : 12
# VERB : is
# SEQUENCE : 13
# VERB : need
# SEQUENCE : 14
# VERB : decide
# SEQUENCE : 15
# VERB : missing
# SEQUENCE : 16
# VERB : procured
# SEQUENCE : 17
# VERB : is
# SEQUENCE : 18
# VERB : scheduled
# SEQUENCE : 19
# VERB : start
# SEQUENCE : 20
# VERB : receive
# SEQUENCE : 21
# VERB : takes
# SEQUENCE : 22
# VERB : checked
# SEQUENCE : 23
#[(1, 'we', get, care of the implementation, 'VO_', 'isActive', ''), 
# (2, 'one', determines, care of the implementation, 'VO_', 'isActive', ''), 
# (3, '-', 'is', that information, 'VO_', 'isPassive', 'Once'), 
# (4, 'it', has, care of the implementation, 'VO_', 'isActive', ''), 
# (5, '-', entered, our production planning system, 'VO_', 'isPassive', ''), 
# (6, 'It', optimizes, care of the implementation, 'VO_', 'isActive', ''), 
# (7, '-', creates, uniform, 'VO_', 'isActive', ''), 
# (8, '-', 'minimized', the setup times, 'VO_', 'isPassive', ''), 
# (9, 'it', creates, care of the implementation, 'VO_', 'isActive', ''), 
# (11, 'it', coupled, care of the implementation, 'VO_', 'isActive', ''), 
# (12, '-', 'transferred', the data, 'VO_', 'isPassive', ''), 
# (13, '-', 'is', all the data, 'VO_', 'isPassive', 'Once'), 
# (14, '-', 'need', we, 'VO_', 'isActive', ''), 
# (16, 'any parts', missing, care of the implementation, 'VO_', 'isActive', ''), 
# (19, '-', 'scheduled', production, 'ExclusiveGateway_', 'isPassive', 'Once'), 
# (21, 'we', receive, care of the implementation, 'ExclusiveGateway_', 'isActive', ''), 
# (22, 'employee', takes, care of the implementation, 'ExclusiveGateway_', 'isActive', ''), 
# (23, 'the order', checked, care of the implementation, 'ExclusiveGateway_', 'isActive', '')]

#Scenario 9 =========================================================
#sentence = "First, the Manager checks the open leads. Afterwards, he selects the top five ones. He then tells his Sales Assistant to call the contact person of the leads. The Sales Assistant calls each customer. If someone is interested, he sends a note to the Manager. The Manager then processes the lead. Otherwise, he calls the next customer."
#[(1, '-', 'checks', the Manager, 'VO_', 'isActive', ''), 
# (2, '-', 'leads', open, 'VO_', 'isActive', ''), 
# (3, 'he', selects, a note to the Manager, 'VO_', 'isActive', ''), 
# (4, 'He', tells, a note to the Manager, 'VO_', 'isActive', ''), 
# (5, '-', call, the contact person, 'VO_', 'isActive', ''), 
# (6, 'The Sales Assistant', calls, a note to the Manager, 'VO_', 'isActive', ''), 
# (7, '-', 'is', someone, 'VO_', 'isPassive', ''), 
# (8, 'he', sends, a note to the Manager, 'VO_', 'isActive', ''), 
# (9, 'The Manager', processes, a note to the Manager, 'VO_', 'isActive', ''), 
# (10, 'he', calls, a note to the Manager, 'VO_', 'isActive', '')]

#From Neural Coref
#sentence = " First, the Manager checks the open leads. Afterwards, the Manager selects the top five ones. the Manager then tells the Manager Sales Assistant to call the contact person of the leads. his Sales Assistant calls each customer. If someone is interested, someone sends a note to the Manager. the Manager then processes the lead. Otherwise, the Manager calls the next customer."
#[(1, 'the Manager', checks, the contact person of the leads, 'VO_', 'isActive', ''), 
# (2, 'the Manager', selects, the contact person of the leads, 'VO_', 'isActive', ''), 
# (3, 'the Manager', tells, the contact person of the leads, 'VO_', 'isActive', ''), 
# (4, '-', call, the contact person, 'VO_', 'isActive', ''), 
# (5, 'his Sales Assistant', calls, the contact person of the leads, 'VO_', 'isActive', ''), 
# (6, 'someone', sends, the contact person of the leads, 'VO_', 'isActive', ''), 
# (7, 'the Manager', processes, the contact person of the leads, 'VO_', 'isActive', ''), 
# (8, 'the Manager', calls, the contact person of the leads, 'VO_', 'isActive', '')]

#Scenario 11 =========================================================
#sentence = "This process starts whenever a purchase order has been received from a customer. The first activity that is carried out is confirming the order. Next, the shipment address is received so that the product can be shipped to the customer. Afterwards, the invoice is emitted and once the payment is received the order is archived, thus completing the process."
#[(1, '-', 'starts', This process, 'VO_', 'isActive', ''), 
# (2, 'a purchase order', 'received', a customer, 'VO_', 'isPassive', ''), 
# (3, '-', 'carried', The first activity, 'VO_', 'isPassive', ''), 
# (4, 'The first activity', 'confirming', the order, 'VO_', 'isPassive', ''), 
# (5, '-', 'received', the shipment address, 'VO_', 'isPassive', ''), 
# (6, 'the product', 'shipped', the customer, 'VO_', 'isPassive', ''), 
# (7, 'the invoice', emitted, '', 'VO_', 'isActive', ''), 
# (8, '-', 'received', the payment, 'VO_', 'isPassive', ''), 
# (9, '-', 'archived', the order, 'VO_', 'isPassive', ''), 
# (10, '-', completing, the process, 'VO_', 'isPassive', '')]

#Scenario 12 =========================================================
#sentence = "Once the boarding pass has been received, passengers proceed to the security check. Here they need to pass the personal security screening and the luggage screening. Afterwards, they can proceed to the departure level."
#[(1, '-', 'received', the boarding pass, 'ExclusiveGateway_', 'isPassive', 'Once'), 
# (2, 'passengers', 'proceed', the security check, 'ExclusiveGateway_', 'isActive', ''), 
# (3, 'they', 'pass', the personal security screening, 'ExclusiveGateway_', 'isActive', ''), 
# (3, 'they', 'pass', the luggage screening, 'ExclusiveGateway_', 'isActive', ''), 
# (4, '-', pass, the personal security screening, 'ExclusiveGateway_', 'isActive', ''), 
# (4, '-', pass, the luggage screening, 'ExclusiveGateway_', 'isActive', ''), 
# (5, 'they', 'proceed', the departure level, 'ExclusiveGateway_', 'isActive', '')]
#Neural Coref
#sentence = "Once the boarding pass has been received, passengers proceed to the security check. Here passengers need to pass the personal security screening and the luggage screening. Afterwards, passengers can proceed to the departure level."
#[(1, '-', 'received', the boarding pass, 'ExclusiveGateway_', 'isPassive', 'Once'), 
# (2, 'passengers', 'proceed', the security check, 'ExclusiveGateway_', 'isActive', ''), 
# (3, 'passengers', 'pass', the personal security screening, 'ExclusiveGateway_', 'isActive', ''), 
# (3, 'passengers', 'pass', the luggage screening, 'ExclusiveGateway_', 'isActive', ''), 
# (4, '-', pass, the personal security screening, 'ExclusiveGateway_', 'isActive', ''), 
# (4, '-', pass, the luggage screening, 'ExclusiveGateway_', 'isActive', ''), 
# (5, 'passengers', 'proceed', the departure level, 'ExclusiveGateway_', 'isActive', '')]

#Scenario 13 =========================================================
#sentence = "As soon as an invoice is received from a customer, it needs to be checked for mismatches. The check may result in either of these three options: i) there are no mismatches, in which case the invoice is posted; ii) there are mismatches but these can be corrected, in which case the invoice is re-sent to the customer; and iii) there are mismatches but these cannot be corrected, in which case the invoice is blocked. Once one of these three activities is performed the invoice is parked and the process completes."
# VERB : received
# SEQUENCE : 1
# VERB : needs
# SEQUENCE : 2
# VERB : checked
# SEQUENCE : 3
# VERB : result
# SEQUENCE : 4
# VERB : posted
# SEQUENCE : 5
# VERB : corrected
# SEQUENCE : 6
# VERB : re
# SEQUENCE : 7
# VERB : -
# SEQUENCE : 8
# VERB : sent
# SEQUENCE : 9
# VERB : are
# SEQUENCE : 10
# VERB : corrected
# SEQUENCE : 11
# VERB : blocked
# SEQUENCE : 12
# VERB : performed
# SEQUENCE : 13
# VERB : parked
# SEQUENCE : 14
# VERB : completes
# SEQUENCE : 15
#[(1, 'invoice', 'received', a customer, 'VO_', 'isPassive', ''), 
# (2, 'it', 'checked', mismatches, 'VO_', 'isPassive', ''), 
# (3, '-', checked, mismatches, 'VO_', 'isPassive', ''), 
# (4, 'The check', 'result', either, 'VO_', 'isActive', ''), 
# (5, '-', 'posted', the invoice, 'VO_', 'isPassive', ''), 
# (7, '-', 're', the invoice, 'VO_', 'isActive', ''), 
# (9, '-', sent, the customer, 'VO_', 'isPassive', ''), 
# (10, 'there', 'are', mismatches, 'VO_', 'isPassive', ''), 
# (12, '-', 'blocked', the invoice, 'VO_', 'isPassive', ''), 
# (13, '-', 'performed', one, 'VO_', 'isPassive', 'Once'), 
# (14, 'the invoice', parked, '', 'VO_', 'isActive', ''), 
# (15, '-', 'completes', the process, 'VO_', 'isActive', '')]

#Scenario 18 =========================================================
#sentence = "In the treasury minister’s office, once a ministerial inquiry has been received, it is first registered into the system. Then the inquiry is investigated so that a ministerial response can be prepared. The finalization of a response includes the preparation of the response itself by the cabinet officer and the review of the response by the principal registrar. If the registrar does not approve the response, the latter needs to be prepared again by the cabinet officer for review. The process finishes only once the response has been approved."
#[(1, '-', 'received', a ministerial inquiry, 'VO_', 'isPassive', ''), 
# (2, 'it', registered, the preparation of the response, 'VO_', 'isActive', for review), 
# (3, '-', 'investigated', the inquiry, 'VO_', 'isPassive', ''), 
# (4, '-', 'prepared', a ministerial response, 'VO_', 'isPassive', ''), 
# (5, 'The finalization', includes, the preparation of the response, 'VO_', 'isActive', ''), 
# (6, 'the registrar', approve, the preparation of the response, 'VO_', 'isActive', ''), 
# (7, 'latter', needs, the preparation of the response, 'VO_', 'isActive', ''), 
# (8, '-', prepared, the cabinet officer, 'VO_', 'isPassive', ''), 
# (9, '-', 'finishes', The process, 'VO_', 'isActive', ''), 
# (10, '-', 'approved', the response, 'VO_', 'isPassive', '')]
#From Neural Coref
#sentence = " In the treasury minister’s office, once a ministerial inquiry has been received, a ministerial inquiry is first registered into the system. Then a ministerial inquiry is investigated so that a ministerial response can be prepared. The finalization of a response includes the preparation of the response itself by the cabinet officer and the review of the response by the principal registrar. If the principal registrar does not approve the response, the latter needs to be prepared again by the cabinet officer for review. The process finishes only once the response has been approved."
#[(1, '-', 'received', a ministerial inquiry, 'VO_', 'isPassive', ''), 
# (2, 'a ministerial inquiry', registered, the preparation of the response, 'VO_', 'isActive', for review), 
# (3, '-', 'investigated', a ministerial inquiry, 'VO_', 'isPassive', ''), 
# (4, '-', 'prepared', a ministerial response, 'VO_', 'isPassive', ''), 
# (5, 'The finalization', includes, the preparation of the response, 'VO_', 'isActive', ''), 
# (6, 'the principal registrar', approve, the preparation of the response, 'VO_', 'isActive', ''), 
# (7, 'latter', needs, the preparation of the response, 'VO_', 'isActive', ''), 
# (8, '-', prepared, the cabinet officer, 'VO_', 'isPassive', ''), 
# (8, '-', prepared, review, 'VO_', 'isPassive', ''), 
# (9, '-', 'finishes', The process, 'VO_', 'isActive', ''), 
# (10, '-', 'approved', the response, 'VO_', 'isPassive', '')]

sentence = "The Vacation Request Process starts when an employee of the organization submits a vacation request. Once the requirement is registered, the request is received by the immediate supervisor; the supervisor must approve or reject the request. If the request is rejected the application is returned to the applicant/employee who can review the rejection reasons. If the request is approved a notification is generated to the Human Resources representative, who must complete the respective administrative procedures."
neuralCoref = NeuralCoref(sentence)
text = neuralCoref.get_sentence()
phrases = MockPhrases(text)
phrases.get_svo(text)

#"The Vacation Request Process starts when an employee of the organization submits a vacation request. 
# Once the requirement is registered, the request is received by the immediate supervisor; 
# the supervisor must approve or reject the request. 
# If the request is rejected the application is returned to the applicant/employee who can review the rejection reasons. 
# If the request is approved a notification is generated to the Human Resources representative, 
# who must complete the respective administrative procedures."

#Start [(1, '-', 'starts',  The Vacation Request Process, 'VO_', 'isActive', ''), 
#X (2, 'employee', 'submits', a vacation request, 'VO_', 'isActive', ''),    
# (3, '-', 'registered', the requirement, 'VO_', 'isPassive', 'Once'), 
# (4, 'a vacation request', 'received', the immediate supervisor, 'VO_', 'isPassive', ''), 
# (5, 'the immediate supervisor', approve, '', 'ExclusiveGateway_', 'isActive', ''), 
# (6, '-', reject, a vacation request, 'ExclusiveGateway_', 'isActive', ''), 
# (7, '-', 'rejected', a vacation request, 'ExclusiveGateway_', 'isPassive', ''), 
# (8, 'the application', 'returned', the applicant/employee, 'ExclusiveGateway_', 'isPassive', ''), 
# (9, '-', 'review', the rejection reasons, 'ExclusiveGateway_', 'isActive', ''), 
# (10, '-', 'approved', a vacation request, 'ExclusiveGateway_', 'isPassive', ''), 
# (11, 'a notification', 'generated', the Human Resources representative, 'ExclusiveGateway_', 'isPassive', ''), 
# (12, '-', 'complete', the respective administrative procedures, 'ExclusiveGateway_', 'isActive', '')]
