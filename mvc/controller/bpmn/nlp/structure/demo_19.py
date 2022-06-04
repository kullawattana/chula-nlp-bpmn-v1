from subject_verb_object_extract import findSVOs, nlp

str = "The Evanstonian is an upscale independent hotel. When a guest calls room service at The Evanstonian, the room-service manager takes down the order. She then submits an order ticket to the kitchen to begin preparing the food. She also gives an order to the sommelier (i.e., the wine waiter) to fetch wine from the cellar and to prepare any other alcoholic beverages. Eighty percent of room-service orders include wine or some other alcoholic beverage. Finally, she assigns the order to the waiter. While the kitchen and the sommelier are doing their tasks, the waiter readies a cart (i.e., puts a tablecloth on the cart and gathers silverware). The waiter is also responsible for nonalcoholic drinks. Once the food, wine, and cart are ready, the waiter delivers it to the guests room. After returning to the room-service station, the waiter debits the guests account. The waiter may wait to do the billing if he has another order to prepare or deliver."

#ไม่มี
#The Evanstonian is an upscale independent hotel. 

#When {a guest calls room service} at The Evanstonian, {the room-service manager takes down the order}. 
#[('a guest', 'calls', 'room service'),  ('the service manager', 'takes', 'the order'),
# [When (SVO), (SVO)]
 
# {She then submits an order ticket to the kitchen} to begin preparing the food.   
# ('She', 'submits', 'an order ticket to the kitchen'), 
# [(SVO)]

# {She also gives an order} {to the sommelier (i.e., the wine waiter)} to fetch wine from the cellar and to prepare any other alcoholic beverages. 
# ('She', 'gives', 'an order'), ('She', 'gives', 'to sommelier ( i.e. , the wine waiter'), 
# [(SVO), (SVO) and (SVO)]

# {Eighty percent of room-service orders include wine} or {some other alcoholic beverage.} 
# ('Eighty percent of service orders', 'include', 'wine'), ('Eighty percent of', 'include', 'some other alcoholic beverage'),  
# [(SVO) or (SVO)]

# Finally, {she assigns the order to the waiter.}
# ('she', 'assigns', 'the order to the waiter'),
# [Finally, (SVO)]

# While {the kitchen and the sommelier are doing their tasks}, the waiter readies a cart (i.e., puts a tablecloth on the cart and {gathers silverware}).
# ('the kitchen', 'doing', 'their tasks'), ('the sommelier', 'doing', 'their tasks'), ('gathers', 'silverware'), 
# [While, (SVO), (SVO) and (SVO)]

# The waiter is also responsible for nonalcoholic drinks. 

# Once {the food, wine}, and cart are ready, {the waiter delivers it} to the guests room. 
# ('the food , wine', 'are'), ('the waiter', 'delivers', 'it'), 
# [Once (SVO), (SVO)]

# After returning to the room-service station, {the waiter debits} {the guests account.} 
# ('the waiter', 'debits'), ('the guests', 'account'), 
# [After (SVO), (SVO)]

# {The waiter may wait to do the billing} if {he has another order to prepare or deliver.}
# ('The waiter', 'do', 'the billing'), ('he', 'has', 'another order'), ('another order', 'deliver')]
# [(SVO) if (SVO)]

#===================================================================
#[('a guest', 'calls', 'room service'), 
# ('the service manager', 'takes', 'the order'), 
# ('She', 'submits', 'an order ticket to the kitchen'), 
# ('She', 'gives', 'an order'), 
# ('She', 'gives', 'to sommelier ( i.e. , the wine waiter'), 
# ('Eighty percent of service orders', 'include', 'wine'), 
# ('Eighty percent of', 'include', 'some other alcoholic beverage'), 
# ('she', 'assigns', 'the order to the waiter'), 
# ('the kitchen', 'doing', 'their tasks'), 
# ('the sommelier', 'doing', 'their tasks'), 
# ('gathers', 'silverware'), 
# ('the food , wine', 'are'), 
# ('the waiter', 'delivers', 'it'), 
# ('the waiter', 'debits'), 
# ('the guests', 'account'), 
# ('The waiter', 'do', 'the billing'), 
# ('he', 'has', 'another order'), 
# ('another order', 'deliver')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)