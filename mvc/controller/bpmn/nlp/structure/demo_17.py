from subject_verb_object_extract import findSVOs, nlp

str = "If the product requested is not in stock, it needs to be manufactured before the order handling can continue. To manufacture a product, the required raw materials have to be ordered. Two preferred suppliers provide different types of raw material. Depending on the product to be manufactured, raw materials may be ordered from either Supplier 1 or Supplier 2, or from both. Once the raw materials are available, the product can be manufactured and the order can be confirmed. On the other hand, if the product is in stock, it is retrieved from the warehouse before confirming the order. Then the process continues normally."
#========================================
#If {the product requested is not in stock}, {it} needs to be {manufactured} before {the order} handling can continue.
#[('the product', 'requested'), ('stock', '!be', 'the product'), ('the order', 'manufacture', 'it'), ('handling', 'continue'), 

#สกัดได้ไม่ครบ
# To manufacture a product, {the required raw materials have} to be ordered. 
#('the materials', 'required'), ('the materials', 'have'), 
#[(SVO)]

# Two preferred suppliers provide different types of raw material. 
# ('different types of raw material', 'provide', 'Two preferred suppliers'), 
#[(SVO)]

#สกัดได้ไม่ครบ
# Depending on the product to be manufactured, raw materials may be ordered from either Supplier 1 or Supplier 2, or from both. 
#('Supplier 1', 'order', 'raw materials'), 

# Once the raw materials are available, the product can be manufactured and the order can be confirmed. 
# ('the raw materials', 'are'), ('the order', 'confirmed'), 
#[Once (SV),(SV)]

# On the other hand, {if the product is in stock}, {it is retrieved from the warehouse before confirming the order}. 
# # ('stock', 'be', 'the product'), ('the warehouse', 'retrieve', 'it')
#[On the other hand, if (SVO),(SVO)]

# Then the process continues normally.
# ('the process', 'continues')]
#[(SVO)]

#========================================
#[('the product', 'requested'), 
# ('stock', '!be', 'the product'), 
# ('the order', 'manufacture', 'it'), 
# ('handling', 'continue'), 
# ('the materials', 'required'), 
# ('the materials', 'have'), 
# ('different types of raw material', 'provide', 'Two preferred suppliers'), 
# ('Supplier 1', 'order', 'raw materials'), 
# ('the raw materials', 'are'), 
# ('the order', 'confirmed'), 
# ('stock', 'be', 'the product'), 
# ('the warehouse', 'retrieve', 'it'), 
# ('the process', 'continues')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)