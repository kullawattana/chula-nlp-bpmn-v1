from subject_verb_object_extract import findSVOs, nlp

str1 = "When a claim is received, it is first checked whether the claimant is insured by the organization."
#[('a claim', 'received'), ('it', 'checked'), ('the organization', 'insure', 'the claimant')]
#[When (SVO),(SVO) whether (SVO)]

str2 = "If not, the claimant is informed that the claim must be rejected."
#[('the claimant', '!informed'), ('the claim', 'rejected')]
#[If (SVO),(SVO)]

str3 = "Otherwise, the severity of the claim is evaluated."
#[('the severity of the claim', 'evaluated')]
#[Otherwise (SVO)]

str4 = "Based on the outcome (simple or complex claims), relevant forms are sent to the claimant."
#[('the claimant', 'send', 'relevant forms')]
#[Based on (SVO)]

str5 = "Once the forms are returned, they are checked for completeness."
#[('the forms', 'returned'), ('completeness', 'check', 'they')]
#[Once (SVO), (SVO)]

str6 = "If the forms provide all relevant details, the claim is registered in the Claims Management system, which ends the Claims Notification process."
#[('all relevant details', 'provide', 'the forms'), ('the Management system ,', 'register', 'the claim'), ('the Notification process', 'end', 'the Management system ,')]
#[If (SVO), (SVO), (SVO)]

str7 = "Otherwise, the claimant is informed to update the forms."
#[('the forms', 'update', 'the claimant')]
#[Otherwise (SVO)]

str8 = "Upon reception of the updated forms, they are checked again."
#[('the forms', 'updated'), ('they', 'checked')]
#[Upon (SV), (SV)]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)