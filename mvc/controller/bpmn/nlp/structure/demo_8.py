from subject_verb_object_extract import findSVOs, nlp

str = "Every time we get a new order from the sales department, first, one of my masters determines the necessary parts and quantities as well as the delivery date. Once that information is present, it has to be entered into our production planning system (PPS). It optimizes our production processes and creates possibly uniform work packages so that the setup times are minimized. Besides, it creates a list of parts to be procured. Unfortunately it is not coupled correctly to our Enterprise Resource Planning system (ERP), so the data must be transferred manually. By the way, that is the second step. Once all the data is present, we need to decide whether any parts are missing and must be procured or if this is not necessary. Once production is scheduled to start, we receive a notice from the system and an employee takes care of the implementation. Finally, the order will be checked again for its quality."

#Every time {we get a new order from the sales department}, first, {one of my masters determines the necessary parts} and {quantities as well as the delivery date}. 
#[('a new order from the sales department', 'get', 'we'), ('the necessary parts', 'determine', 'one of my masters'), ('quantities as', 'determine', 'one of'), ('the delivery date', 'determine', 'one of'), 
#[Every time (SVO), first, (SVO) and (SVO)]

# Once {that information is} present, {it has to be entered into our production planning system (PPS)}. 
#('that information', 'is'), ('our planning system ( PPS )', 'enter', 'it'), 
#[Once (SVO), (SVO)]

# {It optimizes our production processes} and creates possibly uniform work packages so that {the setup times are minimized.} 
# ('our production processes', 'optimize', 'It'), ('the setup times', 'minimized'), 
#[(SVO) and (SVO) so that (SVO)]

# Besides, {it creates a list of parts to be procured.}
# ('a list of parts', 'create', 'it'), 
#[Besides, (SVO)]

# Unfortunately {it is not coupled correctly to our Enterprise Resource Planning system (ERP)}, so {the data must be transferred} manually. 
# ('our Planning system ( ERP )', '!couple', 'it'), ('the data', 'transferred'),
#[Unfortunately, (SVO) so (SVO)]

# By the way, that is the second step. Once {all the data is} present, {we need} to decide whether any parts are missing and must be procured or if this is not necessary. 
# ('all the data', 'is'), ('we', 'need'),
#[By the way, that (SVO) Once (SVO), (SVO)]

#Once {production is scheduled} to start, {we receive a notice from the system} and {an employee takes care} of the implementation. 
#('production', 'scheduled'), ('a notice from the system', 'receive', 'we'), ('care', 'take', 'an employee'), 
#[Once, (SVO), (SVO) and (SVO)]

# Finally, {the order will be checked again for its quality."}
# ('its quality', 'check', 'the order')]
#[Finally, (SVO)]

#========================================================================
#[('a new order from the sales department', 'get', 'we'), 
# ('the necessary parts', 'determine', 'one of my masters'), 
# ('quantities as', 'determine', 'one of'), 
# ('the delivery date', 'determine', 'one of'), 
# ('that information', 'is'), 
# ('our planning system ( PPS )', 'enter', 'it'), 
# ('our production processes', 'optimize', 'It'), 
# ('the setup times', 'minimized'), 
# ('a list of parts', 'create', 'it'), 
# ('our Planning system ( ERP )', '!couple', 'it'), 
# ('the data', 'transferred'), 
# ('all the data', 'is'), 
# ('we', 'need'), 
# ('production', 'scheduled'), 
# ('a notice from the system', 'receive', 'we'), 
# ('care', 'take', 'an employee'), 
# ('the implementation', 'take', 'an employee'), 
# ('its quality', 'check', 'the order')]

tokens = nlp(str)
svos = findSVOs(tokens)
print("\n1")
print(str)
print(svos)