from subject_verb_object_extract import findSVOs, nlp

str = "A company has two warehouses that store different products: Amsterdam and Hamburg. When an order is received, it is distributed across these warehouses: if some of the relevant products are maintained in Amsterdam, a sub-order is sent there; likewise, if some relevant products are maintained in Hamburg, a sub-order is sent there. Afterwards, the order is registered and the process completes."

#A company has two warehouses that store different products: Amsterdam and Hamburg. 
# When an order is received, it is distributed across these warehouses: if some of the relevant products are maintained in Amsterdam, a sub-order is sent there; likewise, if some relevant products are maintained in Hamburg, a sub-order is sent there. 
# Afterwards, the order is registered and the process completes.

#A company has two warehouses that store different products: Amsterdam and Hamburg.
#[('two warehouses', 'have', 'A company'), ('different products', 'store', 'two warehouses')

#ยังตัดไม่ถูก
# When an order is received, it is distributed across these warehouses: 
# if some of the relevant products are maintained in Amsterdam, a sub-order is sent there; likewise, 
# if some relevant products are maintained in Hamburg, a sub-order is sent there. 
# ('an order', 'received'), ('these warehouses', 'distribute', 'it'), 
# ('-', 'sent'), ('order', 'sent'), ('Hamburg ,', 'maintain', 'some relevant products'), 
# ('-', 'sent'), ('-', 'sent'), ('order', 'sent'), 

# Afterwards, the order is registered and the process completes.
#('the process', 'completes')

#============================================================
#[('two warehouses', 'have', 'A company'), 
# ('different products', 'store', 'two warehouses'), 
# ('an order', 'received'), 
# ('these warehouses', 'distribute', 'it'), 
# ('-', 'sent'), 
# ('order', 'sent'), 
# ('Hamburg ,', 'maintain', 'some relevant products'), 
# ('a sub', 'sent'), 
# ('-', 'sent'), 
# ('order', 'sent'), 
# ('the process', 'completes')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)