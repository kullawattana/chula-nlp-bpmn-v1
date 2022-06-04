from subject_verb_object_extract import findSVOs, nlp

str = "The Vacation Request Process starts when an employee of the organization submits a vacation request. Once the requirement is registered, the request is received by the immediate supervisor; the supervisor must approve or reject the request. If the request is rejected the application is returned to the applicant/employee who can review the rejection reasons. If the request is approved a notification is generated to the Human Resources representative, who must complete the respective administrative procedures."
#[('The Vacation Request Process', 'starts'), 
# ('a vacation request', 'submit', 'an employee of the organization'), 
# ('the requirement', 'registered'), 
# ('the immediate supervisor', 'receive', 'the request'), 
# ('the request', 'approve', 'the supervisor'), 
# ('the request', 'reject', 'the supervisor'), 
# ('the request', 'rejected'), 
# ('the applicant / employee', 'return', 'the application'), 
# ('the rejection reasons', 'review', 'who'), 
# ('the request', 'approved'), 
# ('the Resources representative ,', 'generate', 'a notification'), 
# ('the respective administrative procedures', 'complete', 'who')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)