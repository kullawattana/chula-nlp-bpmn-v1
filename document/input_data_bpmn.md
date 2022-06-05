## Pattern
role = { 
        "{number_of_role}|{subject}|Lane_{id}":[
            "{event}_{id}",
            "{event}_{id}",
            "{event}_{id}"
        ],
        "{number_of_role}|{subject}|Lane_{id}":[
            "{event}_{id}",
            "{event}_{id}",
            "{event}_{id}"
        ]
        .
        .
        .
    }

lane = {
        "Lane_{id}":[
            "{event}_{id}",
            "{event}_{id}",
            "{event}_{id}"
        ],
        "Lane_{id}":[
            "{event}_{id}",
            "{event}_{id}",
            "{event}_{id}"
        ]
        .
        .
        .
    }

list_svo_to_generate_bpmn_in_out_diagram = [
        "{event}_{id}_{label}_{direction}|",
        "{event}_{id}_{label}_{direction}|",

        "{event}_{id}_{label}_{direction}|",
        "{event}_{id}_{label}_{direction}|",

        .
        .
        .
    ]

=============================================
## Case 1

- Sequence
Start 
START-ACT1, ACT1-ACT2,  
                 ACT2-ACT3, ACT3-END

```json
    a1 = { 
        "1| A small company|Lane_bd0972e":[
            "StartEvent_a0aecaf",
            "Activity_8caf90c",
            "ExclusiveGateway_fca89aa"
        ],
        "2|some files|Lane_da2bbfe":[
            "Activity_6b2f6f5",
            "EndEvent_056a7dc"
        ]
    }
    a11 = json.dumps(a1)
    list_flow = json.loads(a11)
    
    b2 = {
        "Lane_bd0972e":[
            "StartEvent_a0aecaf",
            "Activity_8caf90c",
            "ExclusiveGateway_fca89aa"
        ],
        "Lane_da2bbfe":[
            "Activity_6b2f6f5",
            "EndEvent_056a7dc"
        ]
    }

    list_svo_to_generate_bpmn_in_out_diagram = [
        "StartEvent_a0aecaf_Start_BPMN-MOVE-NEXT|",
        "Activity_8caf90c_manufactures customized bicycles_BPMN-MOVE-NEXT|",

        "Activity_8caf90c_manufactures customized bicycles_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_549cb36_initiated a search_BPMN-MOVE-NEXT|",
        
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_6b2f6f5_tracked the intended location_BPMN-MOVE-DOWN|",
        
        "Activity_549cb36_initiated a search_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_1c58bf5_Gxj_BPMN-MOVE-DOWN|",
        
        "Activity_6b2f6f5_tracked the intended location_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_1c58bf5_Gxj_BPMN-MOVE-DOWN|",
        
        "EndEvent_056a7dc_End_BPMN-MOVE-DOWN|"
    ]

    b12 = json.dumps(b2)
    json_list_lane = json.loads(b12)

    list_lane = [
        "Lane_bd0972e_di",
        "Lane_da2bbfe_di"
    ]
```

## Case 2

- Sequence
#START-ACT1, ACT1-GATEWAY, S_GATEWAY-ACT2, ACT2-J_GATEWAY, J_GATEWAY-END
                           S_GATEWAY-ACT3, ACT3-J_GATEWAY,

- Sequence
#START-ACT1, ACT1-ACT2, ACT2-GATEWAY, S_GATEWAY-ACT3, ACT3-J_GATEWAY, J_GATEWAY-END
                                      S_GATEWAY-ACT4, ACT4-J_GATEWAY

```json
    a1 = { 
        "1| A small company|Lane_bd0972e":[
            "StartEvent_a0aecaf",       
            "Activity_8caf901",         
            "Activity_8caf902",         
            "ExclusiveGateway_fca89aa",  
            "Activity_8caf903",         
            "Activity_8caf904",        
            "ExclusiveGateway_1c58bf5",  
            "EndEvent_056a7dc"
        ],
    }
    a11 = json.dumps(a1)
    list_flow = json.loads(a11)

    b2 = {
        "Lane_bd0972e":[
            "StartEvent_a0aecaf",       
            "Activity_8caf901",         
            "Activity_8caf902",         
            "ExclusiveGateway_fca89aa",  
            "Activity_8caf903",         
            "Activity_8caf904",        
            "ExclusiveGateway_1c58bf5",  
            "EndEvent_056a7dc"
        ],
    }

    list_svo_to_generate_bpmn_in_out_diagram = [
        "StartEvent_a0aecaf_Start_BPMN-MOVE-NEXT|",
        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",

        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",
        "Activity_8caf902_bbb_BPMN-MOVE-NEXT|",
        
        "Activity_8caf902_bbb_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",
        
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",
        
        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_1c58bf5_Gxj_BPMN-MOVE-DOWN|",

        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_1c58bf5_Gxj_BPMN-MOVE-DOWN|",
        
        "EndEvent_056a7dc_End_BPMN-MOVE-NEXT|"
    ]

    b12 = json.dumps(b2)
    json_list_lane = json.loads(b12)

    list_lane = [
        "Lane_bd0972e_di",
    ]
```

## Case 3

- Sequence
START-ACT1, ACT1-ACT2, ACT2-GATEWAY, S_GATEWAY-ACT3, ACT3-J_GATEWAY, J_GATEWAY-ACT5 , ACT5-End
                                     S_GATEWAY-ACT4, ACT4-J_GATEWAY,

```json        
    a1 = { 
        "1| A small company|Lane_bd0972e":[
            "StartEvent_a0aecaf",
            "Activity_8caf901",
            "Activity_8caf902",
            "ExclusiveGateway_fca89aa",
            "Activity_8caf903",         
            "Activity_8caf904",        
            "ExclusiveGateway_1c58bf5",  
            "Activity_8caf905",
            "EndEvent_056a7dc"
        ],
    }
    a11 = json.dumps(a1)
    list_flow = json.loads(a11)

    b2 = {
        "Lane_bd0972e":[
            "StartEvent_a0aecaf",       
            "Activity_8caf901",         
            "Activity_8caf902",         
            "ExclusiveGateway_fca89aa",  
            "Activity_8caf903",         
            "Activity_8caf904",        
            "ExclusiveGateway_1c58bf5",  
            "Activity_8caf905",
            "EndEvent_056a7dc"
        ],
    }

    list_svo_to_generate_bpmn_in_out_diagram = [
        "StartEvent_a0aecaf_Start_BPMN-MOVE-NEXT|",
        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",

        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",
        "Activity_8caf902_bbb_BPMN-MOVE-NEXT|",
        
        "Activity_8caf902_bbb_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",
        
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",
        
        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_1c58bf5_Gxj_BPMN-MOVE-DOWN|",

        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_1c58bf5_Gxj_BPMN-MOVE-DOWN|",
        
        "ExclusiveGateway_1c58bf5_Gxj_BPMN-MOVE-DOWN|",
        "Activity_8caf905_ddd_BPMN-MOVE-NEXT|",

        "EndEvent_056a7dc_End_BPMN-MOVE-NEXT|"
    ]

    b12 = json.dumps(b2)
    json_list_lane = json.loads(b12)

    list_lane = [
        "Lane_bd0972e_di"
    ]
```        

## Case 4

- Sequence
START-ACT1, ACT1-ACT2, ACT2-GATEWAY, S_GATEWAY-ACT3, ACT3-J_GATEWAY, J_GATEWAY-ACT5, ACT5-GATEWAY, S_GATEWAY-ACT6,ACT6-J_GATEWAY, J_GATEWAY-ACT7, ACT7-END
                                     S_GATEWAY-ACT4, ACT4-J_GATEWAY                                 S_GATEWAY-ACT7, ACT7-J_GATEWAY

```json 
    a1 = { 
        "1| A small company|Lane_bd0972e":[
            "StartEvent_a0aecaf",
            "Activity_8caf901",
            "Activity_8caf902",
            "ExclusiveGateway_fca89aa",
            "Activity_8caf903",         
            "Activity_8caf904",        
            "ExclusiveGateway_fca89bb",  
            "Activity_8caf905",
            "Activity_8caf906",
            "ExclusiveGateway_fca89cc",  
            "Activity_8caf907",
            "Activity_8caf908",
            "ExclusiveGateway_fca89dd",  
            "EndEvent_8caf000"  
        ],
    }
    a11 = json.dumps(a1)
    list_flow = json.loads(a11)

    b2 = {
        "Lane_bd0972e":[
            "StartEvent_a0aecaf",       
            "Activity_8caf901",         
            "Activity_8caf902",         
            "ExclusiveGateway_fca89aa",
            "Activity_8caf903",         
            "Activity_8caf904",        
            "ExclusiveGateway_fca89bb",  
            "Activity_8caf905",
            "Activity_8caf906",
            "ExclusiveGateway_fca89cc",  
            "Activity_8caf907",
            "Activity_8caf908",
            "ExclusiveGateway_fca89dd",  
            "EndEvent_8caf000"  
        ],
    }

    list_svo_to_generate_bpmn_in_out_diagram = [
        "StartEvent_a0aecaf_Start_BPMN-MOVE-NEXT|",
        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",

        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        
        #gateway loop 1
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf902_bbb_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf903_ccc_BPMN-MOVE-DOWN|",
        
        "Activity_8caf902_bbb_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        "Activity_8caf902_ccc_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",
        #End loop

        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",
        "Activity_8caf904_ddd_BPMN-MOVE-NEXT|",

        "Activity_8caf904_ddd_BPMN-MOVE-NEXT|",
        "Activity_8caf905_fff_BPMN-MOVE-NEXT|",

        "Activity_8caf905_fff_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89cc_Gxs?_BPMN-MOVE-NEXT|",

        #gateway loop 2
        "ExclusiveGateway_fca89cc_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf906_ggg_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89cc_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf907_hhh_BPMN-MOVE-DOWN|",

        "Activity_8caf906_ggg_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89dd_Gxj?_BPMN-MOVE-NEXT|",

        "Activity_8caf907_hhh_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89dd_Gxj?_BPMN-MOVE-NEXT|",
        #End loop

        "ExclusiveGateway_fca89dd_Gxj?_BPMN-MOVE-NEXT|",
        "Activity_8caf908_iii_BPMN-MOVE-NEXT|",

        "Activity_8caf908_iii_BPMN-MOVE-NEXT|",
        "EndEvent_8caf000_end_BPMN-MOVE-NEXT|",
        #==============End
    ]

    b12 = json.dumps(b2)
    json_list_lane = json.loads(b12)

    list_lane = [
        "Lane_bd0972e_di",
    ]
```    

## Case 5

```json
    a1 = { 
        "1| A small company|Lane_bd0972a":[
            "StartEvent_a0aecaf",
            "Activity_8caf901"
        ],
        "2| BBB|Lane_bd0972b":[
            "Activity_8caf902",
            "ExclusiveGateway_fca89aa",
            "Activity_8caf903",
            "Activity_8caf904",
            "ExclusiveGateway_fca89bb",
            "EndEvent_8caf000"
        ],
    }

    a11 = json.dumps(a1)
    list_flow = json.loads(a11)

    b2 = {
        "Lane_bd0972a":[
            "StartEvent_a0aecaf",       
            "Activity_8caf901"         
        ],
        "Lane_bd0972b":[        
            "Activity_8caf902",         
            "ExclusiveGateway_fca89aa",  
            "Activity_8caf903",
            "Activity_8caf904",
            "ExclusiveGateway_fca89bb",
            "EndEvent_8caf000"
        ],
    }

    list_svo_to_generate_bpmn_in_out_diagram = [
        "StartEvent_a0aecaf_Start_BPMN-MOVE-NEXT|",
        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",

        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",
        "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",

        "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        
        # #gateway loop 1
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",
        
        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",
        "Activity_8caf905_eee_BPMN-MOVE-NEXT|",
        #End loop

        "Activity_8caf905_eee_BPMN-MOVE-NEXT|",
        "EndEvent_8caf000_end_BPMN-MOVE-NEXT|",
        #==============End
    ]

    b12 = json.dumps(b2)
    json_list_lane = json.loads(b12)

    list_lane = [
        "Lane_bd0972a_di",
        "Lane_bd0972b_di",
    ]
```

## Case 6

```json
    a1 = { 
        "1| A small company|Lane_bd0972a":[
            "StartEvent_a0aecaf",
            "Activity_8caf901",
        ],
        "2| BBB|Lane_bd0972b":[
            "Activity_8caf902",
            "Activity_8caf903",
            "Activity_8caf908",
            "EndEvent_8caf000"  
        ],
        "3| CCC|Lane_bd0972c":[
            "Activity_8caf904",
            "Activity_8caf905",
            "Activity_8caf907"
        ],
        "4| DDD|Lane_bd0972d":[
            "Activity_8caf906",
        ],
    }
    a11 = json.dumps(a1)
    list_flow = json.loads(a11)

    b2 = {
        "Lane_bd0972a":[
            "StartEvent_a0aecaf",       
            "Activity_8caf901",         
        ],
        "Lane_bd0972b":[
            "Activity_8caf902",         
            "Activity_8caf903",
            "Activity_8caf908",
            "EndEvent_8caf000"    
        ],
        "Lane_bd0972c":[
            "Activity_8caf904",         
            "Activity_8caf905",
            "Activity_8caf907"
        ],
        "Lane_bd0972d":[
            "Activity_8caf906",         
        ],
    }

    list_svo_to_generate_bpmn_in_out_diagram = [
        "StartEvent_a0aecaf_Start_BPMN-MOVE-NEXT|",
        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",

        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",
        "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",

        "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",
        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",

        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",
        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",

        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",

        #gateway loop 1
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf905_eee_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf906_fff_BPMN-MOVE-DOWN|",

        "Activity_8caf905_eee_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        "Activity_8caf906_fff_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",
        "Activity_8caf907_ggg_BPMN-MOVE-NEXT|",
        #End loop

        "Activity_8caf907_ggg_BPMN-MOVE-NEXT|",
        "Activity_8caf908_hhh_BPMN-MOVE-UP|",

        "Activity_8caf908_hhh_BPMN-MOVE-UP|",
        "EndEvent_8caf000_end_BPMN-MOVE-NEXT|",
    ]

    b12 = json.dumps(b2)
    json_list_lane = json.loads(b12)

    list_lane = [
        "Lane_bd0972a_di",
        "Lane_bd0972b_di",
        "Lane_bd0972c_di",
        "Lane_bd0972d_di"
    ]
```

## Case 7

```json
    a1 = { 
        "1| A small company|Lane_bd0972a":[
            "StartEvent_a0aecaf",
            "Activity_8caf901",
        ],
        "2| BBB|Lane_bd0972b":[
            "Activity_8caf902",
            "Activity_8caf903",
            "Activity_8caf908",
            "EndEvent_8caf000"  
        ],
        "3| CCC|Lane_bd0972c":[
            "Activity_8caf904",
            "Activity_8caf905",
            "Activity_8caf907"
        ],
        "4| DDD|Lane_bd0972d":[
            "Activity_8caf906",
        ],
    }
    a11 = json.dumps(a1)
    list_flow = json.loads(a11)

    b2 = {
        "Lane_bd0972a":[
            "StartEvent_a0aecaf",       
            "Activity_8caf901",   
            "Activity_8caf909",
            "EndEvent_8caf000"        
        ],
        "Lane_bd0972b":[
            "Activity_8caf902",         
            "Activity_8caf903",
            "Activity_8caf908",  
        ],
        "Lane_bd0972c":[
            "Activity_8caf904",         
            "Activity_8caf905",
            "Activity_8caf907"
        ],
        "Lane_bd0972d":[
            "Activity_8caf906",         
        ],
    }

    list_svo_to_generate_bpmn_in_out_diagram = [
        "StartEvent_a0aecaf_Start_BPMN-MOVE-NEXT|",
        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",

        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",
        "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",

        "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",
        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",

        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",
        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",

        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",

        #gateway loop 1
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf905_eee_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf906_fff_BPMN-MOVE-DOWN|",

        "Activity_8caf905_eee_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        "Activity_8caf906_fff_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",
        "Activity_8caf907_ggg_BPMN-MOVE-NEXT|",
        #End loop

        "Activity_8caf907_ggg_BPMN-MOVE-NEXT|",
        "Activity_8caf908_hhh_BPMN-MOVE-UP|",

        "Activity_8caf908_hhh_BPMN-MOVE-UP|",
        "Activity_8caf909_iii_BPMN-MOVE-UP|",

        "Activity_8caf909_iii_BPMN-MOVE-UP|",
        "EndEvent_8caf000_end_BPMN-MOVE-NEXT|",
    ]

    b12 = json.dumps(b2)
    json_list_lane = json.loads(b12)

    list_lane = [
        "Lane_bd0972a_di",
        "Lane_bd0972b_di",
        "Lane_bd0972c_di",
        "Lane_bd0972d_di"
    ]
```

## Case 8

```json
    a1 = { 
        "1| A small company|Lane_bd0972a":[
            "StartEvent_a0aecaf",
            "Activity_8caf901",
        ],
        "2| BBB|Lane_bd0972b":[
            "Activity_8caf902",
            "Activity_8caf903",
        ],
        "3| CCC|Lane_bd0972c":[
            "Activity_8caf904",
            "Activity_8caf905",
            "Activity_8caf907"
        ],
        "4| DDD|Lane_bd0972d":[
            "Activity_8caf906",
            "Activity_8caf908",
            "EndEvent_8caf000" 
        ],
    }

    a11 = json.dumps(a1)
    list_flow = json.loads(a11)

    b2 = {
        "Lane_bd0972a":[
            "StartEvent_a0aecaf",       
            "Activity_8caf901",        
        ],
        "Lane_bd0972b":[
            "Activity_8caf902",         
            "Activity_8caf903",
        ],
        "Lane_bd0972c":[
            "Activity_8caf904",         
            "Activity_8caf905",
            "Activity_8caf907"
        ],
        "Lane_bd0972d":[
            "Activity_8caf906",  
            "Activity_8caf908",  
            "EndEvent_8caf000"      
        ],
    }

    list_svo_to_generate_bpmn_in_out_diagram = [
        "StartEvent_a0aecaf_Start_BPMN-MOVE-NEXT|",
        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",

        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",
        "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",

        "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",
        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",

        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",
        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",

        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",

        #gateway loop 1
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf905_eee_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf906_fff_BPMN-MOVE-DOWN|",

        "Activity_8caf905_eee_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        "Activity_8caf906_fff_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",
        "Activity_8caf907_ggg_BPMN-MOVE-NEXT|",
        #End loop

        "Activity_8caf907_ggg_BPMN-MOVE-NEXT|",
        "Activity_8caf908_hhh_BPMN-MOVE-DOWN|",

        "Activity_8caf908_hhh_BPMN-MOVE-DOWN|",
        "EndEvent_8caf000_end_BPMN-MOVE-NEXT|",
    ]

    b12 = json.dumps(b2)
    json_list_lane = json.loads(b12)

    list_lane = [
        "Lane_bd0972a_di",
        "Lane_bd0972b_di",
        "Lane_bd0972c_di",
        "Lane_bd0972d_di",
    ]
```

## Case 8

```json
    a1 = { 
        "1| A small company|Lane_bd0972a":[
            "StartEvent_a0aecaf",
            "Activity_8caf901",
        ],
        "2| BBB|Lane_bd0972b":[
            "Activity_8caf902",
            "Activity_8caf903",
        ],
        "3| CCC|Lane_bd0972c":[
            "Activity_8caf904",
            "Activity_8caf905",
            "Activity_8caf907"
        ],
        "4| DDD|Lane_bd0972d":[
            "Activity_8caf906",
            "Activity_8caf908",
        ],
        "5| EEE|Lane_bd0972e":[
            "Activity_8caf909",
            "EndEvent_8caf000"  
        ],
    }
    a11 = json.dumps(a1)
    list_flow = json.loads(a11)

    b2 = {
        "Lane_bd0972a":[
            "StartEvent_a0aecaf",
            "Activity_8caf901",        
        ],
        "Lane_bd0972b":[
            "Activity_8caf902",
            "Activity_8caf903",  
        ],
        "Lane_bd0972c":[
            "Activity_8caf904",
            "Activity_8caf905",
            "Activity_8caf907"
        ],
        "Lane_bd0972d":[
            "Activity_8caf906",
            "Activity_8caf908",         
        ],
        "Lane_bd0972e":[
            "Activity_8caf909",
            "EndEvent_8caf000"          
        ],
    }

    list_svo_to_generate_bpmn_in_out_diagram = [
        "StartEvent_a0aecaf_Start_BPMN-MOVE-NEXT|",
        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",

        "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",
        "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",

        "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",
        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",

        "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",
        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",

        "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",

        #gateway loop 1
        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf905_eee_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        "Activity_8caf906_fff_BPMN-MOVE-DOWN|",

        "Activity_8caf905_eee_BPMN-MOVE-NEXT|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        "Activity_8caf906_fff_BPMN-MOVE-DOWN|",
        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",
        "Activity_8caf907_ggg_BPMN-MOVE-NEXT|",
        #End loop

        "Activity_8caf907_ggg_BPMN-MOVE-NEXT|",
        "Activity_8caf908_hhh_BPMN-MOVE-DOWN|",

        "Activity_8caf908_hhh_BPMN-MOVE-DOWN|",
        "Activity_8caf909_iii_BPMN-MOVE-DOWN|",

        "Activity_8caf909_iii_BPMN-MOVE-DOWN|",
        "EndEvent_8caf000_end_BPMN-MOVE-NEXT|",
    ]

    b12 = json.dumps(b2)
    json_list_lane = json.loads(b12)

    list_lane = [
        "Lane_bd0972a_di",
        "Lane_bd0972b_di",
        "Lane_bd0972c_di",
        "Lane_bd0972d_di"
    ]
```