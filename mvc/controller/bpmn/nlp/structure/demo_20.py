from subject_verb_object_extract import findSVOs, nlp

str = "An employee purchases a product or service he requires. For instance, a sales person on a trip rents a car. The employee submits an expense report with a list of items, along with the receipts for each item. A supervisor reviews the expense report and approves or rejects the report. Since the company has expense rules, there are circumstances where the supervisor can accept or reject the report upon first inspection. These rules could be automated, to reduce the workload on the supervisor. If the supervisor rejects the report, the employee, who submitted it, is given a chance to edit it, for example to correct errors or better describe an expense. If the supervisor approves the report, it goes to the treasurer. The treasurer checks that all the receipts have been submitted and match the items on the list. If all is in order, the treasurer accepts the expenses for processing (including, e.g. , payment or refund, and accounting). If receipts are missing or do not match the report, he sends it back to the employee. If a report returns to the employee for corrections, it must again go to a supervisor, even if the supervisor previously approved the report. If the treasurer accepts the expenses for processing, the report moves to an automatic activity that links to a payment system. The process waits for the payment confirmation. After the payment is confirmed, the process ends."

#{An employee purchases a product} or {service he requires}. 
#[('a product', 'purchase', 'An employee'), ('service', 'purchase', 'An employee'), ('he', 'requires'), 
# [(SVO) or (SVO)]

# For instance, {a sales person on a trip rents a car.}
# ('a car', 'rent', 'a sales person on a trip'), 
# [For instance (SVO)]

# {The employee submits an expense report with a list of items}, along with the receipts for each item. 
# ('an expense report with a list of items', 'submit', 'The employee'), 
# [(SVO)]

# {A supervisor reviews the expense report} and approves or rejects the report. 
# ('the expense report', 'review', 'A supervisor'), ('expense rules', 'have', 'the company'),  
# [(SVO),(SVO)]

# Since the company has expense rules, there are circumstances where the supervisor can accept or reject the report upon first inspection. 
# ('the report', 'accept', 'the supervisor'), ('the report', 'reject', 'the supervisor'), ('the report', 'reject', 'circumstances'), 
# [(SVO),(SVO) or (SVO)]

# {These rules could be automated}, to reduce the workload on the supervisor. 
# ('These rules', 'automated'),
# [(SVO),(SVO)]

# If {the supervisor rejects the report}, the employee, {who submitted it}, is given {a chance to edit it}, for example to correct errors or better describe an expense.
#('the report , employee', 'reject', 'the supervisor'), ('it', 'submit', 'who'), ('it', 'edit', 'a chance'), 
# [(SVO),(SVO),(SVO)]

# If {the supervisor approves the report}, it goes to the treasurer. 
#('the report', 'approve', 'the supervisor'), ('the treasurer', 'go', 'it'), 
# [If (SVO),(SVO)]

# {The treasurer checks} that all {the receipts have been submitted and match the items on the list}. 
# ('The treasurer', 'checks'), ('the items on the list', 'submit', 'all the receipts'), ('the items on', 'match', 'all the receipts'), 
# [(SVO),(SVO), (SVO)]

# If all is in order, {the treasurer accepts the expenses for processing (including, e.g. , payment or refund, and accounting).} 
# ('the expenses for processing (', 'accept', 'the treasurer'), ('payment', 'include', 'processing ('), ('refund', 'include', 'processing ('), # ('payment', 'accounting'), 
# [If (SVO),(SVO),(SVO)] 

# If receipts are missing or do not match the report, he sends it back to the employee. 
# ('the report', 'miss', 'receipts'), ('the report', 'match', 'receipts'), ('it', 'send', 'he'), 
# [If (SVO),(SVO)] 

# If a report returns to the employee for corrections, it must again go to a supervisor, even if the supervisor previously approved the report. 
# ('the employee for corrections', 'return', 'a report'), ('a supervisor', 'go', 'it'), ('the report', 'approve', 'the supervisor'), 
# [If (SVO),(SVO),(SVO)] 

# If the treasurer accepts the expenses for processing, the report moves to an automatic activity that links to a payment system.
# ('the expenses for processing', 'accept', 'the treasurer'), ('an automatic activity', 'move', 'the report'), ('a payment system', 'link', 'an automatic activity'), 
# [If (SVO),(SVO),(SVO)] 

# The process waits for the payment confirmation. 
# ('the payment confirmation', 'wait', 'The process')

# After the payment is confirmed, the process ends."
# ('the payment', 'confirmed'), ('the process', 'ends')]
# [(SVO),(SVO)] 

#================================================
#[('a product', 'purchase', 'An employee'), 
# ('service', 'purchase', 'An employee'), 
# ('he', 'requires'), 
# ('a car', 'rent', 'a sales person on a trip'), 
# ('an expense report with a list of items', 'submit', 'The employee'), 
# ('the expense report', 'review', 'A supervisor'), 
# ('expense rules', 'have', 'the company'), 
# ('the report', 'accept', 'the supervisor'), 
# ('the report', 'reject', 'the supervisor'), 
# ('the report', 'reject', 'circumstances'), 
# ('These rules', 'automated'), 
# ('the report , employee', 'reject', 'the supervisor'), 
# ('it', 'submit', 'who'), 
# ('it', 'edit', 'a chance'), 
# ('the report', 'approve', 'the supervisor'), 
# ('the treasurer', 'go', 'it'), 
# ('The treasurer', 'checks'), 
# ('the items on the list', 'submit', 'all the receipts'), 
# ('the items on', 'match', 'all the receipts'), 
# ('the expenses for processing (', 'accept', 'the treasurer'), 
# ('payment', 'include', 'processing ('), 
# ('refund', 'include', 'processing ('), 
# ('payment', 'accounting'), 
# ('the report', 'miss', 'receipts'), 
# ('the report', 'match', 'receipts'),
# ('it', 'send', 'he'), 
# ('the employee for corrections', 'return', 'a report'), 
# ('a supervisor', 'go', 'it'), 
# ('the report', 'approve', 'the supervisor'), 
# ('the expenses for processing', 'accept', 'the treasurer'), 
# ('an automatic activity', 'move', 'the report'), 
# ('a payment system', 'link', 'an automatic activity'), 
# ('the payment confirmation', 'wait', 'The process'), 
# ('the payment', 'confirmed'), 
# ('the process', 'ends')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)