from subject_verb_object_extract import findSVOs, nlp

str = "A loan application is approved if it passes two checks: (i) the applicant’s loan risk assessment, done automatically by a system, and (ii) the appraisal of the property for which the loan has been asked, carried out by a property appraiser. The risk assessment requires a credit history check on the applicant, which is performed by a financial officer. Once both the loan risk assessment and the property appraisal have been performed, a loan officer can assess the applicant’s eligibility. If the applicant is not eligible, the application is rejected, otherwise the acceptance pack is prepared and sent to the applicant."

#มั่วๆ
#{A loan application is approved} if {it passes two checks:} (i) the applicant’s loan risk assessment, {done automatically by a system,} and (ii) the appraisal of the property for which the {loan has been asked}, {carried out by a property appraiser}.
#('A loan application i', 'approved'), ('two checks :', 'pass', 'it'), ('a system', 'do', '( i ) assessment ,'), ('the loan', 'asked'), ('a property appraiser', 'carry', 'the appraisal of the property'), 
# [(SVO), (SVO), (SVO), (SVO), (SVO)] 

# {The risk assessment requires a credit history check on the applicant}, which is {performed by a financial officer}.
# ('a history check on the applicant ,', 'require', 'The risk assessment'), ('a financial officer', 'perform', 'the applicant ,'), 
# [(SVO), which is (SVO)] 

# Once both the loan risk {assessment} and {the property appraisal have been performed}, a loan officer can assess the applicant’s eligibility. 
#('assessment', 'performed'), ('the property appraisal', 'performed'), ('the applicant eligibility', 'assess', 'a loan officer'),
# [Once both (SVO) and (SVO), (SVO)] 

# If {the applicant is not eligible}, the application is rejected, otherwise the acceptance pack is prepared and sent to the applicant.
#('the applicant', '!is'),  ('the application', 'rejected'), ('the applicant', 'prepare', 'the acceptance pack'), ('the applicant', 'send', 'the acceptance pack')]
# [If (SVO) and (SVO), (SVO)] 

#===============================================================================
#[('A loan application i', 'approved'), 
# ('two checks :', 'pass', 'it'), 
# ('a system', 'do', '( i ) assessment ,'), 
# ('the loan', 'asked'), 
# ('a property appraiser', 'carry', 'the appraisal of the property'), 
# ('a history check on the applicant ,', 'require', 'The risk assessment'), 
# ('a financial officer', 'perform', 'the applicant ,'), 
# ('assessment', 'performed'), 
# ('the property appraisal', 'performed'), 
# ('the applicant eligibility', 'assess', 'a loan officer'), 
# ('the applicant', '!is'), 
# ('the application', 'rejected'), 
# ('the applicant', 'prepare', 'the acceptance pack'), 
# ('the applicant', 'send', 'the acceptance pack')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)