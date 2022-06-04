from subject_verb_object_extract import findSVOs, nlp

str = "This process starts whenever a purchase order has been received from a customer. The first activity that is carried out is confirming the order. Next, the shipment address is received so that the product can be shipped to the customer. Afterwards, the invoice is emitted and once the payment is received the order is archived, thus completing the process."

#{This process starts} whenever {a purchase order has been received from a customer.} 
#('This process', 'starts'), ('a customer', 'receive', 'a purchase order'), 
#[(SV),(SVO)]

# {The first activity that is carried} out is {confirming the order.}
#('The first activity', 'carried'), ('the order', 'confirm', 'The first activity'), 
#[(SV),(SVO)]

# Next, {the shipment address is received} so that {the product can be shipped to the customer.}
# ('the shipment address', 'received'), ('the customer', 'ship', 'the product'), 
#[Next, (SV),(SVO)]

# Afterwards, the invoice is emitted and once {the payment is received} {the order is archived}, thus completing the process."
# ('the payment', 'received'), ('the order', 'archived')]
#[Afterwards, (SV) and once (SVO) (SVO)]

#=================================================
#[('This process', 'starts'), 
# ('a customer', 'receive', 'a purchase order'), 
# ('The first activity', 'carried'), 
# ('the order', 'confirm', 'The first activity'), 
# ('the shipment address', 'received'), 
# ('the customer', 'ship', 'the product'), 
# ('the payment', 'received'), 
# ('the order', 'archived')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)