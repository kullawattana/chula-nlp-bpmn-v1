1. Rs([START EVENT(Es)])
# TODO Return 
## uuid = fa4c5c7
## flow_id : StartEvent_{uuid}
## list_svo_to_generate_bpmn_in_out_diagram : [StartEvent_{uuid}_Start|]
## result_vo_subject : ["Start_{Start}|StartEvent_{uuid}_Start", "Subject_{subject}"]

2. Rs([START EVENT(Es) + ACTIVITY EVENT(VP)])
# TODO Return 
## uuid = fa4c5c7 
## event_id : Activity_uuid
## list_svo_to_generate_bpmn_in_out_diagram : [Activity_{uuid}_{VO}|]
## result_vo_subject : ["VO_{VO}|Activity_{uuid}", "Subject_{subject}"]

3. ACTIVITY-EVENT
# TODO Return 
## uuid = fa4c5c7
## event_id : Activity_{uuid}
## list_svo_to_generate_bpmn_in_out_diagram : [Activity_{uuid}_{VO}|]
## result_vo_subject : ("ExclusiveGateway_{VO}|Activity_{uuid}", "Subject_{subject}")

4. GATEWAY START JOIN EVENT Rx, R+, Gxs G+s Gos
# TODO Return 
## uuid = fa4c5c7
## event_id : Activity_{uuid}
## list_svo_to_generate_bpmn_in_out_diagram : [Activity_{uuid}_{VO}|]
## result_vo_subject : ("ExclusiveGateway_{VO}|Activity_{uuid}", "Subject_{subject}")
## gateway_svo_list_split : ["Activity_{uuid}_{VO}|"]