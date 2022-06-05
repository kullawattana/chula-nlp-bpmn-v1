from subject_verb_object_extract import findSVOs, nlp

str = "By assuming that a purchase order is only confirmed if the product is in stock, otherwise the process completes by rejecting the order. Further, if the order is confirmed, the shipment address is received and the requested product is shipped while the invoice is emitted and the payment is received. Afterwards, the order is archived and the process completes."

#By assuming that a purchase order is only confirmed if the product is in stock, otherwise the process completes by rejecting the order. Further, if the order is confirmed, the shipment address is received and the requested product is shipped while the invoice is emitted and the payment is received. Afterwards, the order is archived and the process completes.

#By assuming that {a purchase order is only confirmed} if {the product is in stock} otherwise {the process completes} by rejecting the order.
#[('a purchase order', 'confirmed'), ('stock', 'be', 'the product'), ('the process', 'completes'),
# [By assuming that (SVO) if (SVO) otherwise (SVO)] 

#Further, if {the order is confirmed}, the shipment address is received and {the requested product is shipped} while the invoice is emitted and {the payment is received}.
# ('the order', 'confirmed'), ('the product', 'requested'), ('the payment', 'received'),
# [Further, if (SVO), (SVO) and (SVO) while the invoice is emitted and (SVO)] 

#Afterwards, the order is archived and {the process completes.}
#('the process', 'completes')]
# [Afterwards (SVO) and (SVO)] 

#===========================================
#[('a purchase order', 'confirmed'), 
# ('stock', 'be', 'the product'), 
# ('the process', 'completes'), 
# ('the order', 'confirmed'), 
# ('the product', 'requested'), 
# ('the product', 'shipped'), 
# ('the payment', 'received'), 
# ('the process', 'completes')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)