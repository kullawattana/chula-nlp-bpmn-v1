import xml.etree.ElementTree as gfg
from models.json_model import JsonDictionary

class BPMNDiagram():
    def __init__(self, res_group_by_event, list_lane, json_list_lane, participant_id, is_show_lane):
        self.res_group_by_event = res_group_by_event
        self.list_lane = list_lane
        self.json_list_lane = json_list_lane
        self.participant_id = participant_id
        self.is_show_lane = is_show_lane

        # Start Element Shape
        self.start_x = 160
        self.start_event_y = 80
        self.start_activity_y = 80
        self.start_end_y = 80
        self.bpmn_shape_y = 0

        # Start
        self.x = 160
        self.y = 80

        #Lane
        self.lane_x = 160
        self.lane_y = 110
        self.position_lane_x = 70            #initial X
        self.position_lane_y = 20            #initial Y
        self.shape_participant_h = 0
        self.shape_lane_y = 0
        self.shape_lane_h = 0
        self.shape_lane_w = 0
        
        #Waypoint
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
        self.y1 = 0
        self.y2 = 0
        self.y3 = 0

        self.gateway_flag = ""
        self.firstActivityCount = 0
    
    #====================================================================
    #[START] - ACT
    def startWithActivityFlow(self):
        self.x1 = 36 + self.x                  #x1 += 36 = 196
        self.x2 = 90 + self.x                  #x2 += 90 = 250
        self.y1 = 18 + self.y                  #y1 += 18 = 98
        self.y2 = 18 + self.y                  #y2 += 18 = 98
        return self.x1, self.x2, self.y1, self.y2
    
    #[START] - ACT - ACT
    def activityWithActivityFlow(self):
        self.x1 = 100 + self.x2                #(x1) = x2 + 100 = 350
        self.x2 = 60 + self.x1                 #x2 = (x1) + 60 = 410
        return self.x1, self.x2, self.y1, self.y2

    #[START] - ACT - move down ACT
    def activityMoveDownWithActivityFlow(self):
        self.x1 = 50 + self.x2                #(x1) = x2 + 50 = 300
        self.x2 = self.x1                     #x2 = (x1)      = 300     
        self.y1 += 40                         #y1 = 40 + (y1) = 138
        self.y2 = 52 + self.y1 + 40           #y2 = 52 + (y1) = 190     //Note : + 40 เพราะว่าความกว้างของเลน
        return self.x1, self.x2, self.y1, self.y2
    
    #[START] - ACT - move up ACT
    def activityMoveUpWithActivityFlow(self):
        self.x1 = 50 + self.x2                #(x1) = x2 + 50 = 300
        self.x2 = self.x1                     #x2 = (x1)      = 300     
        self.y1 -= 40                         #y1 = (y1) - 40 = 190
        self.y2 = self.y1 - 52 - 40           #y2 = (y1) - 52 = 138     //Note : + 40 เพราะว่าความกว้างของเลน
        return self.x1, self.x2, self.y1, self.y2    

    #[START] - ACT - (move down) ACT - (next) ACT
    def activityMoveNextActivityFlow(self):
        self.x1 += 50                          #(x1) = x1 + 50 = 350
        self.x2 = 50 + self.x1                 #x2 = (x1) + 50 = 400
        self.y2 += 50                          #y2 = 50 + (190) = 230      
        self.y1 = self.y2                      #y1 = 230
        return self.x1, self.x2, self.y1, self.y2   

    def activityMoveFromUptoNextActivityFlow(self):
        self.x1 = 50 + self.x2                 #(x1) = x2 + 50 = 350
        self.x2 = 50 + self.x1                 #x2 = (x1) + 50 = 400
        self.y1 = 18 + self.y                  #y1 += 18 = 98
        self.y2 = 18 + self.y                  #y2 += 18 = 98
        return self.x1, self.x2, self.y1, self.y2  

    def activityDoubleUp(self):
        self.y1 -= 172 
        y2 = self.y2 - 160
        return self.x1, self.x2, self.y1, y2  

    def activityDoubleDown(self):
        self.y1 += 172
        y2 = self.y2 + 180 
        return self.x1, self.x2, self.y1, y2              
    
    #[START] - ACT - GATEWAY
    def startWithGatewayFlow(self):
        self.x1 = 100 + self.x2                #(x1) = 100 + X2 = 350
        self.x2 = 55 + self.x1                 #x2 = 55 + X1 = 405
        return self.x1, self.x2, self.y1, self.y2

    #[START] - ACT - SPLIT GATEWAY - ACT 1
    def gatewayWithSplitActivityFlow(self):
        self.x1 = 50 + self.x2                 #(x1) = 50 + X2 = 455
        self.x2 = 55 + self.x1                 #x2 = 55 + X1 = 510
        return self.x1, self.x2, self.y1, self.y2
    
    #[START] - ACT - SPLIT GATEWAY - ACT 2
    def gatewaySplitFlow(self):
        self.x1 = self.x2 - 80                  #(x1) - 80 = 430
        self.x2 = self.x1                       #x2 = 430    
        self.x3 = self.x2 + 80                  #x3 = 430 + 80 = 510    
        self.y1 += 25                           #y1 + 25 = 123
        self.y2 += 112                          #y2 + 112 = 210
        self.y3 = self.y2                       #y3 = 210
        return self.x1, self.x2, self.x3, self.y1, self.y2, self.y3

    #JOIN GATEWAY - ACT 1 - END
    def gatewayWithJoinActivityFlow(self):
        self.x1 = 100 + self.x3                 #(x1) = 100 + X3 = 610
        self.x2 = 55 + self.x1                  #x2 = 55 + X1 = 665
        self.y1 -= 25                           #98
        self.y2 -= 112                          #98
        return self.x1, self.x2, self.y1, self.y2
    
    #JOIN GATEWAY - ACT 2 ... - END
    def gatewayJoinFlow(self):
        self.x1 = self.x3 + 100                 #(x3) = 510 + 100 = 610
        self.x2 = self.x1 + 80                  #(x2) = 610 + 80 = 690
        self.x3 = self.x2                       #(x3) = 690
        self.y1 = self.y3                       #y1 = 210
        self.y2 = self.y3                       #y2 = 210
        self.y3 -= 87                           #y3 - 87 = 123
        return self.x1, self.x2, self.x3, self.y1, self.y2, self.y3

    def joinGatewayWithActivityFlow(self):
        self.x1 += 105                          # 610 + 105 = 715       
        self.x2 = self.x1 + 55                  # 715 + 55 = 770
        self.y1 = self.y3 - 25                  #Reset กลับมาใหม่ ***
        self.y2 = self.y3 - 25                  #Reset กลับมาใหม่ ***
        return self.x1, self.x2, self.y1, self.y2
    
    def joinGatewayWithEndFlow(self):
        self.x1 += 105
        self.x2 = self.x1 + 57
        self.y1 = 98                            #Reset กลับมา 98 ใหม่ ***
        self.y2 = 98                            #Reset กลับมา 98 ใหม่ ***
        return self.x1, self.x2, self.y1, self.y2
    
    def endEventFlow(self):
        self.x1 = 100 + self.x2                 #(x1) = 100 + 50 = 455
        self.x2 = 62 + self.x1                  #x2 = 55 + 55 = 510
        return self.x1, self.x2, self.y1, self.y2

    def activityAndEndEventFlow(self):
        self.x1 = 100 + self.x2                 #(x1) = 100 + x2 = 510
        self.x2 = 22 + self.x1                  #x2 = 22 + x1 = 532
        return self.x1, self.x2, self.y1, self.y2
    
    #====================================================================
    def improve_lane_activity(self):
        result = []
        for ls in self.list_lane:
            list_id = str(ls).split("_",2)
            _bpmn_element_list_id = list_id[0]+"_"+list_id[1]
            result.append({"id": str(ls), "bpmnElement": _bpmn_element_list_id})
        return result

    #====================================================================
    def startActivity(self):
        self.start_x += 0               #x += 0 = 160
        self.start_event_y += 0         #y += 0 = 80
        return self.start_x, self.start_event_y
        
    def startWithfirstActivity(self):
        self.start_x += 90              #x += 90 = 250
        self.start_activity_y -= 22     #y -= 22 = 58
        return self.start_x, self.start_activity_y

    def gotoOthersActivity(self):
        self.start_x += 160             #x += 160 = 420 
        return self.start_x, self.start_activity_y

    def gotoEvent(self):
        self.start_x += 155             #x += 160 = 420 
        self.start_gateway_y = 73       #x -= 7 = 73
        return self.start_x, self.start_gateway_y
    
    def gotoEnd(self):
        return self.start_end_y

    #====================================================================
    def get_source_target_event(self, value):
        event_name_source_out_going = str(value[0]).split("_", 1)
        event_name_target_in_coming = str(value[1]).split("_", 1)
        _source_out_going = str(event_name_source_out_going[1]).split("|", 1)[1]
        _target_in_coming = str(event_name_target_in_coming[1]).split("|", 1)[1]
        return event_name_source_out_going, event_name_target_in_coming, _source_out_going, _target_in_coming
    
    def get_is_source_and_target_want(self, _source_out_going, _target_in_coming):
        if _source_out_going == "Event" and _target_in_coming == "Activity":
            return True
        elif _source_out_going == "Activity" and _target_in_coming == "Activity":
            return True
        elif _source_out_going == "Gateway" and _target_in_coming == "Activity":
            return True
        elif _source_out_going == "Activity" and _target_in_coming == "Gateway":
            return True
        elif _source_out_going == "Gateway" and _target_in_coming == "Event":
            return True
        elif _source_out_going == "Activity" and _target_in_coming == "Event":
            return True
        else:
            return False

    def _renew_list_bpmn_element(self):
        _all_event_list = []
        _renew_list =[]
        for _, value in self.res_group_by_event.items():
            _source_out_going, _target_in_coming , _ , _ = self.get_source_target_event(value)
            is_source_and_target_want = self.get_is_source_and_target_want(str(_source_out_going[0]), str(_target_in_coming[0]))       
            if is_source_and_target_want == True:
                _all_event_list.append(str(value[0]))
                _all_event_list.append(str(value[1]))

        for i in _all_event_list:
            if i not in _renew_list:
                _renew_list.append(i)
        return _renew_list

    #====================================================================
    def _bpmn_diagram(self, diagram_id):
        element = gfg.Element("bpmndi:BPMNDiagram", id=diagram_id)
        return element
    
    def _bpmn_plan(self, plan_id, uuid):
        element = gfg.Element("bpmndi:BPMNPlane", id=plan_id, bpmnElement=uuid)
        return element
    
    def bpmn_edges(self, diagram_id, plan_id, uuid, collaboration_id):
        self.diagram_id = diagram_id
        self.plan_id = plan_id
        self.uuid = uuid
        self.collaboration_id = collaboration_id

        # XML Waypoint Start
        self.start_x = 160
        self.start_y = 80
        self.counter_split_gateway = 0
        self.counter_join_gateway = 0

        print("---------------START EDGES-------------------")
        diagram = self._bpmn_diagram(self.diagram_id)
        if self.is_show_lane == True:           #Connection lane with element
            plan = self._bpmn_plan(self.plan_id, uuid=self.collaboration_id)
        else:
            plan = self._bpmn_plan(self.plan_id, uuid=self.uuid)

        """
        event_name_source_out_going : ['Event', '0e3f7bb']            OUT
        event_name_target_in_coming : ['Activity', '0e3f7bb']         IN
        """
        #START EVENT
        #ACT - ACT
        #ACT - END
        #ACT - GATEWAY          [START SPLIT GATEWAY]   and self.counter_split_gateway == 0:
        #GATEWAY - ACT 1        [SPLIT GATEWAY]         and self.counter_split_gateway == 1:
        #GATEWAY - ACT 2 ...    [SPLIT GATEWAY]         and self.counter_split_gateway >= 2:
        #ACT - GATEWAY 1        [JOIN GATEWAY]          and self.counter_join_gateway == 1:
        #ACT - GATEWAY 2 ...    [JOIN GATEWAY]          and self.counter_join_gateway >= 2
        #GATEWAY = ACT          [CLOSE JOIN GATEWAY]    and self.counter_split_gateway == 0
        
        ls = []
        _renew_list = self._renew_list_bpmn_element()
        for flow_id, value in self.res_group_by_event.items():
            event_id_out_going = str(value[0]).split("|", 1)
            event_id_in_coming = str(value[1]).split("|", 1)
            #print("event_id_out_going :", event_id_out_going[0], "||", "event_id_in_coming :", event_id_in_coming[0])

            flow_id_element = flow_id+"_di"
            event_name_source_out_going, event_name_target_in_coming, bpmn_directional_out_going, bpmn_directional_in_coming = self.get_source_target_event(value)

            #START EVENT
            if str(event_name_source_out_going[0]) == "Event":
                self.gateway_flag = ""
                edge = gfg.Element("bpmndi:BPMNEdge", id=flow_id_element, bpmnElement=flow_id)
                
                if bpmn_directional_out_going == "BPMN-MOVE-NEXT" and bpmn_directional_in_coming == "BPMN-MOVE-NEXT":
                    print("Next-Next (Start)")
                    self.x1, self.x2, self.y1, self.y2 = self.startWithActivityFlow()

                print("START-ACT x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2, "|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])
                
                waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                edge.insert(1, waypoint_1)
                waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                edge.insert(1, waypoint_2)

                for item in _renew_list[:]:
                    if item in value[0]:
                        event_name_source_out_going = str(value[0]).split("_", 1)
                        event_id = "StartEvent_"+str(event_name_source_out_going[1])
                        ls.append(str(event_id)+"|"+str(self.x)+"|"+str(self.y2)+"|"+"StartEvent-Activity")
                        _renew_list.remove(item)
                    elif item in value[1]:
                        ls.append(str(value[1])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+"StartEvent-Activity")
                        _renew_list.remove(item)
                
                plan.append(edge)

            # ===========================================================================================================
            #ACT - ACT EVENT
            if str(event_name_source_out_going[0]) == "Activity" and str(event_name_target_in_coming[0]) == "Activity":
                #ไม่อยู่ใน loop ของการสร้าง Gateway และ ID ของ กิจกรรมไม่ตรงกัน (ตรวจสอบการสร้าง scale)
                if self.gateway_flag != "Split-Join-Gateway" and (event_id_out_going != event_id_in_coming): 
                    edge = gfg.Element("bpmndi:BPMNEdge", id=flow_id_element, bpmnElement=flow_id)

                    bpmn_activity_direction = ""
                    if bpmn_directional_out_going == "BPMN-MOVE-NEXT" and bpmn_directional_in_coming == "BPMN-MOVE-NEXT":
                        bpmn_activity_direction = "Activity-Next-Activity-Next"
                        self.x1, self.x2, self.y1, self.y2 = self.activityWithActivityFlow()
                        print("ACT next - ACT next :: x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])
                        waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                        edge.insert(1, waypoint_1)
                        waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                        edge.insert(1, waypoint_2)
                    elif bpmn_directional_out_going == "BPMN-MOVE-NEXT" and bpmn_directional_in_coming == "BPMN-MOVE-DOWN":
                        bpmn_activity_direction = "Activity-Next-Activity-Down"
                        self.x1, self.x2, self.y1, self.y2 = self.activityMoveDownWithActivityFlow()
                        print("ACT next - ACT down :: x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])
                        waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                        edge.insert(1, waypoint_1)
                        waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                        edge.insert(1, waypoint_2)
                    elif bpmn_directional_out_going == "BPMN-MOVE-DOWN" and bpmn_directional_in_coming == "BPMN-MOVE-NEXT": 
                        bpmn_activity_direction = "Activity-Down-Activity-Next"
                        self.x1, self.x2, self.y1, self.y2 = self.activityMoveNextActivityFlow()
                        print("ACT down - ACT next :: x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])
                        waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                        edge.insert(1, waypoint_1)
                        waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                        edge.insert(1, waypoint_2)
                    elif bpmn_directional_out_going == "BPMN-MOVE-NEXT" and bpmn_directional_in_coming == "BPMN-MOVE-UP":
                        bpmn_activity_direction = "Activity-Next-Activity-Up"
                        self.x1, self.x2, self.y1, self.y2 = self.activityMoveUpWithActivityFlow()
                        print("ACT next - ACT up :: x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])
                        waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                        edge.insert(1, waypoint_1)
                        waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                        edge.insert(1, waypoint_2)
                    elif bpmn_directional_out_going == "BPMN-MOVE-UP" and bpmn_directional_in_coming == "BPMN-MOVE-NEXT":
                        bpmn_activity_direction = "Activity-Up-Activity-Next"
                        self.x1, self.x2, self.y1, self.y2 = self.activityMoveFromUptoNextActivityFlow()
                        print("ACT up - ACT next :: x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])
                        waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                        edge.insert(1, waypoint_1)
                        waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                        edge.insert(1, waypoint_2)
                    elif bpmn_directional_out_going == "BPMN-MOVE-UP" and bpmn_directional_in_coming == "BPMN-MOVE-UP":
                        bpmn_activity_direction = "Activity-Up-Activity-Up"
                        #Double skip from role 3 to role 1
                        self.x1, self.x2, self.y1, y2 = self.activityDoubleUp()
                        print("ACT up - ACT up :: x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])
                        waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                        edge.insert(1, waypoint_1)
                        waypoint_2 = self._bpmn_diagram_waypoint(self.x2, y2)
                        edge.insert(1, waypoint_2)
                    elif bpmn_directional_out_going == "BPMN-MOVE-DOWN" and bpmn_directional_in_coming == "BPMN-MOVE-DOWN":
                        bpmn_activity_direction = "Activity-Down-Activity-Down"
                        self.x1, self.x2, self.y1, self.y2 = self.activityDoubleDown()
                        print("ACT Down - ACT Down :: x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])
                        waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                        edge.insert(1, waypoint_1)
                        waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                        edge.insert(1, waypoint_2)

                    for item in _renew_list[:]:
                        if item in value[0]:
                            ls.append(str(value[0])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+bpmn_activity_direction)
                            _renew_list.remove(item)
                        elif item in value[1]:
                            ls.append(str(value[1])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+bpmn_activity_direction)
                            _renew_list.remove(item)
                    
                    plan.append(edge)
        
            #ACT - END EVENT
            elif str(event_name_source_out_going[0]) == "Activity" and str(event_name_target_in_coming[0]) == "Event":
                self.gateway_flag = ""
                edge = gfg.Element("bpmndi:BPMNEdge", id=flow_id_element, bpmnElement=flow_id)

                self.x1, self.x2, self.y1, self.y2 = self.activityAndEndEventFlow()
                print("ACT-END x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0], bpmn_directional_out_going, bpmn_directional_in_coming)

                if bpmn_directional_out_going == "BPMN-MOVE-UP" and bpmn_directional_in_coming == "BPMN-MOVE-NEXT":
                    #Double skip from role 3 to role 2 or role 2 to role 1
                    self.x1 -= 50
                    self.y1 -= 132
                    self.y2 = self.y1
                elif bpmn_directional_out_going == "BPMN-MOVE-DOWN" and bpmn_directional_in_coming == "BPMN-MOVE-NEXT":
                    #Double skip from role 3 to role 2 or role 2 to role 1
                    self.x1 -= 50
                    self.y1 += 132
                    self.y2 = self.y1    

                waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                edge.insert(1, waypoint_1)
                waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                edge.insert(1, waypoint_2)

                for item in _renew_list[:]:
                    if item in value[0]:
                        ls.append(str(value[0])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+"Activity-EndEvent")
                        _renew_list.remove(item)
                    elif item in value[1]:
                        event_id = "EndEvent_"+str(event_name_target_in_coming[1])
                        ls.append(str(event_id)+"|"+str(self.x2)+"|"+str(self.y2)+"|"+"Activity-EndEvent")
                        _renew_list.remove(item)
                
                plan.append(edge)
            
            #==========================GATEWAY SPLIT LOOP================================    
            #ACT - GATEWAY [START SPLIT GATEWAY]
            elif str(event_name_source_out_going[0]) == "Activity" and str(event_name_target_in_coming[0]) == "Gateway" and self.counter_split_gateway == 0:  
                self.gateway_flag = "Split-Join-Gateway"  
                edge = gfg.Element("bpmndi:BPMNEdge", id=flow_id_element, bpmnElement=flow_id)

                self.x1, self.x2, self.y1, self.y2 = self.startWithGatewayFlow()
                print("ACT-Gateway -1 x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0], bpmn_directional_out_going, bpmn_directional_in_coming)

                if bpmn_directional_out_going == "BPMN-MOVE-DOWN" and bpmn_directional_in_coming == "BPMN-MOVE-NEXT":
                    self.x1 -= 50
                    self.x2 -= 50
                    self.y2 += 40
                    self.y1 = self.y2

                waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                edge.insert(1, waypoint_1)
                waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                edge.insert(1, waypoint_2)

                # ADD
                self.counter_split_gateway += 1

                for item in _renew_list[:]:
                    if item in value[0]:
                        ls.append(str(value[0])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+"Activity-Gateway")
                        _renew_list.remove(item)
                    elif item in value[1]:
                        ls.append(str(value[1])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+"Activity-Gateway")
                        _renew_list.remove(item)
                
                plan.append(edge)
            
            #GATEWAY - ACT 1 [SPLIT GATEWAY]
            elif str(event_name_source_out_going[0]) == "Gateway" and str(event_name_target_in_coming[0]) == "Activity" and self.counter_split_gateway == 1: 
                self.gateway_flag = "Split-Join-Gateway" 
                edge = gfg.Element("bpmndi:BPMNEdge", id=flow_id_element, bpmnElement=flow_id)

                self.x1, self.x2, self.y1, self.y2 = self.gatewayWithSplitActivityFlow()
                print("GATEWAY-ACT -2 x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0], bpmn_directional_out_going, bpmn_directional_in_coming)

                waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                edge.insert(1, waypoint_1)
                waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                edge.insert(1, waypoint_2)

                self.counter_split_gateway += 1

                for item in _renew_list[:]:
                    if item in value[0]:
                        ls.append(str(value[0])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+"Gateway-Activity-move-next-and-split")
                        _renew_list.remove(item)
                    elif item in value[1]:
                        ls.append(str(value[1])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+"Gateway-Activity-move-next-and-split")
                        _renew_list.remove(item)

                plan.append(edge)
            
            #GATEWAY - ACT 2 ... [SPLIT GATEWAY]
            elif str(event_name_source_out_going[0]) == "Gateway" and str(event_name_target_in_coming[0]) == "Activity" and self.counter_split_gateway >= 2:
                self.gateway_flag = "Split-Join-Gateway" 
                edge = gfg.Element("bpmndi:BPMNEdge", id=flow_id_element, bpmnElement=flow_id)

                self.x1, self.x2, self.x3, self.y1, self.y2, self.y3 = self.gatewaySplitFlow()
                print("GATEWAY-ACT -3 x1, x2, x3, y1, y2, y3 ::", self.x1, self.x2, self.x3, self.y1, self.y2, self.y3 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0], bpmn_directional_out_going, bpmn_directional_in_coming)

                waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                edge.insert(1, waypoint_1)
                waypoint_2 = self._bpmn_diagram_waypoint(self.x3, self.y2 + 30)
                edge.insert(1, waypoint_2)
                waypoint_3 = self._bpmn_diagram_waypoint(self.x2, self.y3 + 30)
                edge.insert(1, waypoint_3)

                #CLEAR
                self.counter_split_gateway = -1
                self.counter_join_gateway += 1

                for item in _renew_list[:]:
                    if item in value[0]:
                        ls.append(str(value[0])+"|"+str(self.x3)+"|"+str(self.y3)+"|"+"Gateway-Activity-move-down-and-split")
                        _renew_list.remove(item)
                    elif item in value[1]:
                        event_id = "ActivityGateway_"+str(event_name_target_in_coming[1])
                        ls.append(str(event_id)+"|"+str(self.x3)+"|"+str(self.y3)+"|"+"Gateway-Activity-move-down-and-split")
                        _renew_list.remove(item)
                
                plan.append(edge)
                        
            #==========================GATEWAY JOIN LOOP================================  
            #ACT - GATEWAY 1 [JOIN GATEWAY]
            elif str(event_name_source_out_going[0]) == "Activity" and str(event_name_target_in_coming[0]) == "Gateway" and self.counter_join_gateway == 1:
                self.gateway_flag = "Split-Join-Gateway" 
                edge = gfg.Element("bpmndi:BPMNEdge", id=flow_id_element, bpmnElement=flow_id)

                self.x1, self.x2, self.y1, self.y2 = self.gatewayWithJoinActivityFlow()
                print("ACT-GATEWAY -4 x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])

                waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                edge.insert(1, waypoint_1)
                waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                edge.insert(1, waypoint_2)

                # ADD
                self.counter_join_gateway += 1

                for item in _renew_list[:]:
                    if item in value[0]:
                        ls.append(str(value[0])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+"Activity-Gateway-move-next-and-join")
                        _renew_list.remove(item)
                    elif item in value[1]:
                        ls.append(str(value[1])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+"Activity-Gateway-move-next-and-join")
                        _renew_list.remove(item)

                plan.append(edge)

            #ACT - GATEWAY 2 ... [JOIN GATEWAY]
            elif str(event_name_source_out_going[0]) == "Activity" and str(event_name_target_in_coming[0]) == "Gateway" and self.counter_join_gateway >= 2:
                self.gateway_flag = "Split-Join-Gateway" 
                edge = gfg.Element("bpmndi:BPMNEdge", id=flow_id_element, bpmnElement=flow_id)

                self.x1, self.x2, self.x3, self.y1, self.y2, self.y3 = self.gatewayJoinFlow()
                print("ACT-GATEWAY -5 x1, x2, y1, y2 ::", self.x1, self.x2, self.x3, self.y1, self.y2, self.y3 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])

                waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1 + 30)
                edge.insert(1, waypoint_1)
                waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y3)
                edge.insert(1, waypoint_2)
                waypoint_3 = self._bpmn_diagram_waypoint(self.x3, self.y2 + 30)
                edge.insert(1, waypoint_3)

                #CLEAR
                self.counter_split_gateway = 0
                self.counter_join_gateway = 0

                for item in _renew_list[:]:
                    if item in value[0]:
                        ls.append(str(value[0])+"|"+str(self.x2)+"|"+str(self.y1)+"|"+"Activity-Gateway-move-up-to-join")
                        _renew_list.remove(item)
                    elif item in value[1]:
                        ls.append(str(value[1])+"|"+str(self.x2)+"|"+str(self.y1)+"|"+"Activity-Gateway-move-up-to-join")
                        _renew_list.remove(item)

                plan.append(edge)

            #==========================GATEWAY CLOSE================================ 
            #GATEWAY = ACT [CLOSE JOIN GATEWAY] and continue with Activity
            elif str(event_name_source_out_going[0]) == "Gateway" and str(event_name_target_in_coming[0]) == "Activity" and self.counter_split_gateway == 0:
                self.gateway_flag = "" 
                edge = gfg.Element("bpmndi:BPMNEdge", id=flow_id_element, bpmnElement=flow_id)
                
                self.x1, self.x2, self.y1, self.y2 = self.joinGatewayWithActivityFlow()
                print("GATEWAY-ACT -6 x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])

                waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                edge.insert(1, waypoint_1)
                waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                edge.insert(1, waypoint_2)

                # ไม่ใช้
                # self.counter_split_gateway += 1

                for item in _renew_list[:]:
                    if item in value[0]:
                        ls.append(str(value[0])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+"Gateway-Activity-Start")
                        _renew_list.remove(item)
                    elif item in value[1]:
                        ls.append(str(value[1])+"|"+str(self.x2)+"|"+str(self.y2)+"|"+"Gateway-Activity-Start")
                        _renew_list.remove(item)

                plan.append(edge)
            
            #GATEWAY = END [CLOSE JOIN GATEWAY] 
            elif str(event_name_source_out_going[0]) == "Gateway" and str(event_name_target_in_coming[0]) == "Event" and self.counter_split_gateway == 0:
                self.gateway_flag = "Split-Join-Gateway" 
                edge = gfg.Element("bpmndi:BPMNEdge", id=flow_id_element, bpmnElement=flow_id)

                self.x1, self.x2, self.y1, self.y2 = self.joinGatewayWithEndFlow()
                print("GATEWAY-END -7 x1, x2, y1, y2 ::", self.x1, self.x2, self.y1, self.y2 ,"|", event_name_source_out_going[0],"|", event_name_target_in_coming[0])

                waypoint_1 = self._bpmn_diagram_waypoint(self.x1, self.y1)
                edge.insert(1, waypoint_1)
                waypoint_2 = self._bpmn_diagram_waypoint(self.x2, self.y2)
                edge.insert(1, waypoint_2)

                # ไม่ใช้
                #self.counter_split_gateway += 1

                for item in _renew_list[:]:
                    if item in value[0]:
                        ls.append(str(value[0])+"|"+str(self.x)+"|"+str(self.y)+"|"+"Gateway-EndEvent")
                        _renew_list.remove(item)
                    elif item in value[1]:
                        event_id = "EndEvent_"+str(event_name_target_in_coming[1])
                        ls.append(str(event_id)+"|"+str(self.x2)+"|"+str(self.y)+"|"+"Gateway-EndEvent")
                        _renew_list.remove(item)
                
                plan.append(edge)
                print("===================================================================================")
        
        print("LIST RENEW ===>", ls)
        print("===================================================================================")
        
        #=============================================================================================
        #SHAPE 
        json_list_flow_id = JsonDictionary()
        for lane_id, members_list in self.json_list_lane.items():
            list_for_calculation_lane = self._bpmn_shape(members_list)
            json_list_flow_id.add(lane_id, list_for_calculation_lane)

        #=============================================================================================
        # ADD SHAPE
        _firstActivity = 0
        for bpmnElement in ls:
            _element_bpmn = str(bpmnElement).split("|", 1)           #Activity_9604271|BPMN-MOVE-UP|250|98|Event-Activity'
            _bpmn_direction = str(_element_bpmn[1]).split("|",2)[0]  #BPMN-MOVE-NEXT
            _bpmn_scale_x = str(_element_bpmn[1]).split("|",2)[1]    #250
            _bpmn_scale = str(_element_bpmn[1]).split("|",2)[2]      #98|Event-Activity
            _bpmn_scale_y = str(_bpmn_scale).split("|",1)[0]         #98
            _bpmn_pairs_event = str(_bpmn_scale).split("|",1)[1]     #Event-Activity
            print("BPMN, X, Y ::", _bpmn_direction, _bpmn_scale_x, _bpmn_scale_y, _bpmn_pairs_event)

            bpmn_ = str(_element_bpmn[0]).split("_",1)               #Activity_9604271, 250
            bpmn_event = str(bpmn_[0])                               #Activity
            bpmn_event_id = str(bpmn_[1])                            #9604271

            print("bpmn_event :", bpmn_event)
            #StartEvent
            if bpmn_event == "StartEvent":
                start_event = "Event_"+str(bpmn_event_id)
                self.bpmn_shape_y = self.y
                shape = gfg.Element("bpmndi:BPMNShape", id=str(start_event)+"_di", bpmnElement=start_event)
                gfg.SubElement(shape, "dc:Bounds", x=str(_bpmn_scale_x), y=str(self.y), width="36", height="36")
                plan.append(shape)
            
            #Activity
            elif bpmn_event == "Activity":
                _firstActivity += 1
                if _firstActivity == 1:
                    _, self.bpmn_shape_y = self.startWithfirstActivity()
                    shape = gfg.Element("bpmndi:BPMNShape", id=str(_element_bpmn[0])+"_di", bpmnElement=str(_element_bpmn[0]))
                    gfg.SubElement(shape, "dc:Bounds", x=str(_bpmn_scale_x), y=str(int(self.bpmn_shape_y) + 22), width="100", height="80")
                    plan.append(shape)
                else:
                    _scale_x = 0
                    if _bpmn_direction == "BPMN-MOVE-DOWN":
                        if _bpmn_pairs_event == "Gateway-Activity-move-next-and-split":
                            self.bpmn_shape_y = _bpmn_scale_y 
                            shape = gfg.Element("bpmndi:BPMNShape", id=str(_element_bpmn[0])+"_di", bpmnElement=str(_element_bpmn[0]))
                            gfg.SubElement(shape, "dc:Bounds", x=str(_bpmn_scale_x), y=str(int(self.bpmn_shape_y) + 10), width="100", height="80")
                            plan.append(shape)
                        elif _bpmn_pairs_event != "Activity-Gateway-move-up-to-join":
                            _scale_x = int(_bpmn_scale_x) - 50
                            shape = gfg.Element("bpmndi:BPMNShape", id=str(_element_bpmn[0])+"_di", bpmnElement=str(_element_bpmn[0]))
                            gfg.SubElement(shape, "dc:Bounds", x=str(_scale_x), y=str(_bpmn_scale_y), width="100", height="80")
                            plan.append(shape)
                    elif _bpmn_direction == "BPMN-MOVE-UP":
                        if _bpmn_pairs_event == "Activity-Next-Activity-Up":
                            shape = gfg.Element("bpmndi:BPMNShape", id=str(_element_bpmn[0])+"_di", bpmnElement=str(_element_bpmn[0]))
                            gfg.SubElement(shape, "dc:Bounds", x=str(int(_bpmn_scale_x) - 50), y=str(int(_bpmn_scale_y) - 80), width="100", height="80")
                            plan.append(shape)
                        elif _bpmn_pairs_event in ["Activity-Up-Activity-Up"]:
                            shape = gfg.Element("bpmndi:BPMNShape", id=str(_element_bpmn[0])+"_di", bpmnElement=str(_element_bpmn[0]))
                            gfg.SubElement(shape, "dc:Bounds", x=str(int(_bpmn_scale_x) - 50), y=str(int(_bpmn_scale_y) - 240), width="100", height="80")
                            plan.append(shape)
                        elif _bpmn_pairs_event in ["Activity-Down-Activity-Down"]:
                            shape = gfg.Element("bpmndi:BPMNShape", id=str(_element_bpmn[0])+"_di", bpmnElement=str(_element_bpmn[0]))
                            gfg.SubElement(shape, "dc:Bounds", x=str(int(_bpmn_scale_x)), y=str(int(_bpmn_scale_y)), width="100", height="80")
                            plan.append(shape)
                    elif _bpmn_pairs_event not in ["Activity-Gateway-move-up-to-join", "Activity-Next-Activity-Up"]:
                        shape = gfg.Element("bpmndi:BPMNShape", id=str(_element_bpmn[0])+"_di", bpmnElement=str(_element_bpmn[0]))
                        gfg.SubElement(shape, "dc:Bounds", x=str(_bpmn_scale_x), y=str(int(_bpmn_scale_y) - 40), width="100", height="80")
                        plan.append(shape)
                    elif _bpmn_pairs_event not in ["Gateway-Activity-Start"]:
                        shape = gfg.Element("bpmndi:BPMNShape", id=str(_element_bpmn[0])+"_di", bpmnElement=str(_element_bpmn[0]))
                        gfg.SubElement(shape, "dc:Bounds", x=str(_bpmn_scale_x), y=str(_bpmn_scale_y), width="100", height="80")
                        plan.append(shape)

            #Activity-Gateway
            elif bpmn_event == "ActivityGateway":
                activity_event = "Activity_"+str(bpmn_event_id)
                shape = gfg.Element("bpmndi:BPMNShape", id=str(activity_event)+"_di", bpmnElement=str(activity_event))
                gfg.SubElement(shape, "dc:Bounds", x=str(_bpmn_scale_x), y=str(_bpmn_scale_y), width="100", height="80")
                plan.append(shape)
            
            #Gateway
            elif bpmn_event == "Gateway":
                _element_id = str("Gateway_"+str(bpmn_event_id))       
                shape = gfg.Element("bpmndi:BPMNShape", id=str(_element_id)+"_di", bpmnElement=_element_id)  
                gfg.SubElement(shape, "dc:Bounds", x=str(_bpmn_scale_x), y=str(int(_bpmn_scale_y) - 25), width="50", height="50")
                plan.append(shape)

            #End
            elif bpmn_event == "EndEvent":
                end_event = "Event_"+str(bpmn_event_id) 
                shape = gfg.Element("bpmndi:BPMNShape", id=str(end_event)+"_di", bpmnElement=end_event)
                gfg.SubElement(shape, "dc:Bounds", x=str(_bpmn_scale_x), y=str(int(_bpmn_scale_y) - 10), width="36", height="36")
                plan.append(shape)
            
        #=============================================================================================
        #LANE
        if self.is_show_lane == True:
            _role_count = 0
            _lane_id_list = self.get_lane_id_and_number_of_role(json_list_flow_id)
            _shape_lane_x, _shape_participant_w = self.get_lane_x_and_participant_width()

            for _lane_id in _lane_id_list:
                _role_count += 1
                shape = self.get_more_role_shape(_role_count, _lane_id, _shape_lane_x)
                plan.append(shape)

            shape = gfg.Element("bpmndi:BPMNShape", id=str(self.participant_id)+"_di", bpmnElement=str(self.participant_id), isHorizontal="true")
            gfg.SubElement(shape, "dc:Bounds", x=str(self.position_lane_x), y=str(self.position_lane_y), width=str(_shape_participant_w), height=str(int(self.shape_participant_h) * _role_count))
            plan.append(shape)

        diagram.append(plan)
        return diagram

    def _bpmn_shape(self, members_list):
        element_scale_list_for_calculation_lane = []
        for bpmnElement in members_list:
            bpmn_ = str(bpmnElement).split("_", 1)
            bpmn_event_id = str(bpmn_[0])

            #StartEvent
            if bpmn_event_id == "StartEvent":
                start_event = "Event_"+str(bpmn_[1])
                x, y = self.startActivity()
                element_scale_list_for_calculation_lane.append(str(start_event)+"|"+str(x)+"|"+str(self.y))

            #Activity
            elif bpmn_event_id == "Activity":
                self.firstActivityCount += 1
                if self.firstActivityCount == 1:
                    x, y = self.startWithfirstActivity()
                else:
                    x, y = self.gotoOthersActivity()
                element_scale_list_for_calculation_lane.append(str(bpmnElement)+"|"+str(x)+"|"+str(y))

            #Gateway
            elif bpmn_event_id == "ExclusiveGateway" or bpmn_event_id == "ParallelGateway":
                _element = str(bpmnElement).split("_", 1)
                _element_id = str("Gateway_"+_element[1])       
                x, y = self.gotoEvent()
                element_scale_list_for_calculation_lane.append(str(_element_id)+"|"+str(x)+"|"+str(y))
            
            #End
            elif bpmn_event_id == "EndEvent":
                end_event = "Event_"+str(bpmn_[1])              
                end_y = self.gotoEnd()
                element_scale_list_for_calculation_lane.append(str(end_event)+"|"+str(self.x2)+"|"+str(end_y))

        return element_scale_list_for_calculation_lane 

    def get_lane_id_and_number_of_role(self, json_list_flow_id):
        _lane_id_list = []
        for lane_id, members_list in json_list_flow_id.items():
            # lane_id, members_list Lane_bd0972a ['Event_a0aecaf_1_|250|80', 'Activity_8caf901_1_|340|36']
            # lane_id, members_list Lane_bd0972b ['Activity_8caf902|500|36', 'Activity_8caf903|660|36']
            # lane_id, members_list Lane_bd0972c ['Activity_8caf904_3_|820|36', 'Activity_8caf905|980|36', 'Activity_8caf907|1140|36']
            # lane_id, members_list Lane_bd0972d ['Activity_8caf906|1300|36']
            print("lane_id, members_list", lane_id, members_list )
            _lane_id_list.append(lane_id)                                # Add list ID 
            _last_element_id_scale = str(members_list[-1])               ## Extraction Element to 'Event_3b2b3c9|160|80'
            _event = str(_last_element_id_scale).split("|", 2)           #by event => 'Event_3b2b3c9|160|80'

            #START SHAPE
            self.lane_x = _event[1]                 #X
            self.lane_y = _event[2]                 #Y
            self.shape_participant_h = 175          #Start H

        return _lane_id_list       
    
    def get_lane_x_and_participant_width(self):
        _shape_participant_w = int(self.lane_x) + 40                 # shape_participant_w = maximun (lane X) + 40
        _shape_lane_x = self.position_lane_x + 30                    # Start lane X (ทุกเลน) = 70 + 30 = 100 
        self.shape_lane_w = _shape_participant_w - 30                # ลดความกว้าง จะได้เป็นกรอบข้างในของแต่ละกรอบ
        return _shape_lane_x, _shape_participant_w
    
    def get_more_role_shape(self, _role_count, _lane_id, shape_lane_x): 
        if _role_count == 1:                            
            self.shape_lane_h += int(self.shape_participant_h)                                             
            shape = self._bpmn_lane_shape(_lane_id, shape_lane_x, self.position_lane_y, self.shape_lane_w, self.shape_lane_h)
            return shape
        elif _role_count == 2:
            self.shape_lane_y += self.position_lane_y + self.shape_lane_h    
            shape = self._bpmn_lane_shape(_lane_id, shape_lane_x, self.shape_lane_y, self.shape_lane_w, self.shape_lane_h)
            return shape
        elif _role_count > 2:
            self.shape_lane_y += self.shape_lane_h    
            shape = self._bpmn_lane_shape(_lane_id, shape_lane_x, self.shape_lane_y, self.shape_lane_w, self.shape_lane_h)
            return shape
    
    def _bpmn_lane_shape(self, lane_id, shape_lane_x, shape_lane_y, shape_lane_w, shape_lane_h):
        shape = gfg.Element("bpmndi:BPMNShape", id=str(lane_id+"_id"), bpmnElement=str(lane_id), isHorizontal="true")
        gfg.SubElement(shape, "dc:Bounds", x=str(shape_lane_x), y=str(shape_lane_y), width=str(shape_lane_w), height=str(shape_lane_h))
        return shape
        
    def _bpmn_diagram_waypoint(self, x, y):
        waypoint = gfg.Element("di:waypoint", x=str(x), y=str(y))
        return waypoint