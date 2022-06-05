import uuid
import json
import xml.etree.ElementTree as gfg
from models.json_model import JsonDictionary
_source_target_list = JsonDictionary() 

class BPMNProcess():
    def __init__(self, process_id):
        self.event_id = process_id
        self.renew_sequence_list_flow = None
        self.list_flow = None
    
    def get_flow_id(self):
        return "Flow_" + str(uuid.uuid4())[:7]

    def get_zip_data(self, list_svo):
        data = list_svo
        result = ([x + y for x, y in zip(data, data[1:] + data[:0])])  
        return result
    
    def get_compose_data(self, result):
        re = []
        x = []
        
        for ls in result:
            re.append(ls[:-1])      #Remove "|"

        #composed data
        for (i, item) in enumerate(re):
            a = (i, str(item).split('|'))
            x.append(a)
        return x
    
    def _split_text(self, text):
        split_string = text.split("_", 1)
        return split_string[0]
    
    def _split_incoming_outgoing_flow(self, text):
        split_string = text.split("|", 1)
        return split_string[0], split_string[1]

    def get_is_source_and_target_want(self, _source_out_going, _target_in_coming):
        if _source_out_going == "StartEvent" and _target_in_coming == "Activity":
            return True
        elif _source_out_going == "Activity" and _target_in_coming == "Activity":
            return True
        elif _source_out_going == "ExclusiveGateway" and _target_in_coming == "Activity":
            return True
        elif _source_out_going == "Activity" and _target_in_coming == "ExclusiveGateway":
            return True
        elif _source_out_going == "ExclusiveGateway" and _target_in_coming == "EndEvent":
            return True
        elif _source_out_going == "Activity" and _target_in_coming == "EndEvent":
            return True
        else:
            return False

    def get_source_target_event(self, value):
        #['Activity_71f6291_manufactures customized bicycles_BPMN-MOVE-NEXT', 'ExclusiveGateway_83ebd9e_Gxs?_BPMN-MOVE-NEXT']
        _flow_value = []
        _flow_id = ""
        event_name_source_out_going = str(value[0]).split("_", 3)
        event_name_target_in_coming = str(value[1]).split("_", 3)

        is_source_and_target_want = self.get_is_source_and_target_want(str(event_name_source_out_going[0]), str(event_name_target_in_coming[0]))       
        if is_source_and_target_want == True:
            _flow_id = self.get_flow_id()
            _out_going = str(self.get_flow_id() + "_") + str(value[0])
            _flow_value.append(_out_going)
            _in_coming = str(self.get_flow_id() + "_") + str(value[1])
            _flow_value.append(_in_coming)
        return _flow_id, _flow_value
        
    def generate_flow_id_in_out_task(self, x):
        json_dict = JsonDictionary()
        for _, value in x:
            flow_id = self.get_flow_id()
            flow_value = []
            for v in value:
                a = str(flow_id+"_")+str(v)
                flow_value.append(a)
            json_dict.add(flow_id, flow_value)
        self.renew_sequence_list_flow = json_dict
    
    def renew_generate_flow_id_in_out_task(self):
        idx = 0
        idy = 0
        last_idx = 0
        result_json_dict = JsonDictionary()

        members = len(self.renew_sequence_list_flow)
        for x, y in self.renew_sequence_list_flow.items():            
            idx += 1
            if idx % 2 != 0: 
                last_idx = idx
                result_json_dict.add(x,y)
            if idx == members - 1:              #Fixed Duplicate list 
                result_json_dict.add(x,y)
        
        #Join Gateway
        for x, y in self.renew_sequence_list_flow.items():            
            idy += 1
            if idy == last_idx + 1:         #For Exclusive Gateway
                result_json_dict.add(x,y)
        self.list_flow = result_json_dict
        return result_json_dict

    def _prepare_task_in_out(self, list_svo):
        result = []
        x = []
        result_json_dict = JsonDictionary()

        result = self.get_zip_data(list_svo)
        x = self.get_compose_data(result)
        self.generate_flow_id_in_out_task(x)
        result_json_dict = self.renew_generate_flow_id_in_out_task()

        return result_json_dict
        
    def _get_sequence_list(self):
        json_sequence_lists = []
        list_setup = JsonDictionary()
        for flow_id, value in self.list_flow.items(): 
            _in = value[0].split("_") 
            _out = value[1].split("_") 
            i = _in[0]+"_"+_in[1]
            if i in flow_id:
                #ถ้ามี Exclusive gateway ให้ใช้ list นี้ แก้เรื่อง Duplicate
                if _in[2] == "ExclusiveGateway" or _out[2] == "ExclusiveGateway":
                    list_setup = self.list_flow 
                    break
                #ถ้าเป็น Sequence ให้ใช้ list นี้
                else:
                    list_setup = self.renew_sequence_list_flow    
        
        # key   = 'Flow_5081e20'
        # value = 'Flow_5081e20_StartEvent_f283baa_Start_BPMN-MOVE-UP
        #           0     1        2         3      4        5 
        for flow_id, value in list_setup.items():                               
            id_element_in = ""
            id_element_out = ""
            _in = value[0].split("_") 
            _out = value[1].split("_")

            i = _in[0]+"_"+_in[1]
            if i in flow_id:
                if _in[2] == "StartEvent":
                    id_element_in = "Event_"+_in[3]
                elif _in[2] == "Activity":
                    id_element_in = "Activity_"+_in[3]
                elif _in[2] == "ExclusiveGateway" or _in[2] == "ParallelGateway":
                    id_element_in = "Gateway_"+_in[3]
                elif _in[2] == "Event":
                    id_element_in = "Event_"+_in[3]
                elif _in[2] == "EndEvent":
                    id_element_in = "Event_"+_in[3]
                bpmn_direction_in = id_element_in+"|"+str(_in[5])
                    
            o = _out[0]+"_"+_out[1]          
            if o in flow_id:
                if(_out[2] == "StartEvent"):                    
                    id_element_out = "Event_"+_out[3]
                elif _out[2] == "Activity":
                    id_element_out = "Activity_"+_out[3]
                elif _out[2] == "ExclusiveGateway" or _out[2] == "ParallelGateway":
                    id_element_out = "Gateway_"+_out[3]
                elif _out[2] == "Event":
                    id_element_out = "Event_"+_out[3]
                elif _out[2] == "EndEvent":
                    id_element_out = "Event_"+_out[3]
                bpmn_direction_out = id_element_out+"|"+str(_out[5])

            json_sequence_lists.append({"id":flow_id, "sourceRef":bpmn_direction_in, "targetRef":bpmn_direction_out, "event_name":""})
        return json_sequence_lists
            
    def _get_list_flow_incoming_outgoing(self):
        for key, value in self.list_flow.items():
            _label_in = value[0].split("_") 
            _label_out = value[1].split("_") 
            event_name_in = ""
            event_name_out = ""

            _in = value[0].split("_")
            _out = value[1].split("_")  
            is_source_and_target_want = self.get_is_source_and_target_want(str(_in[2]), str(_out[2]))       
            if is_source_and_target_want == True:

                # key   = 'Flow_5081e20'
                # value = 'Flow_5081e20_StartEvent_f283baa_Start_BPMN-MOVE-UP
                #           0     1        2         3      4        5 
                i = _in[0]+"_"+_in[1]  
                if i in key:
                    id_element = ""
                    if _in[2] == "StartEvent":
                        id_element = "Event_"+_in[3]
                    elif _in[2] == "Activity":
                        id_element = "Activity_"+_in[3]
                    elif _in[2] == "ExclusiveGateway" or _in[2] == "ParallelGateway":
                        id_element = "Gateway_"+_in[3]
                    elif _in[2] == "Event":
                        id_element = "Event_"+_in[3]
                    elif _in[2] == "EndEvent":
                        id_element = "Event_"+_in[3]

                    #Event Name
                    if len(str(_label_in[4])) > 0:
                        event_name_out = str(_label_in[4])
                    else:
                        event_name_out = ""
                    
                    _source_target_list.add("bpmn:outgoing|"+key+"|"+event_name_out+"|"+str(_in[2]), id_element)
                      
                o = _out[0]+"_"+_out[1]              
                if o in key:
                    id_element = ""
                    if(_out[2] == "StartEvent"):                    
                        id_element = "Event_"+_out[3]
                    elif _out[2] == "Activity":
                        id_element = "Activity_"+_out[3]
                    elif _out[2] == "ExclusiveGateway" or _out[2] == "ParallelGateway":
                        id_element = "Gateway_"+_out[3]
                    elif _out[2] == "Event":
                        id_element = "Event_"+_out[3]
                    elif _out[2] == "EndEvent":
                        id_element = "Event_"+_out[3]

                    #Event Name
                    if len(str(_label_out[4])) > 0:
                        event_name_in = str(_label_out[4])
                    else:
                        event_name_in = ""

                    _source_target_list.add("bpmn:incoming|"+key+"|"+event_name_in+"|"+str(_out[2]), id_element)

        return _source_target_list
    
    def _split_text(self, text):
        split_string = text.split("_", 1)
        return split_string[0]
    
    def _split_incoming_outgoing_flow(self, text):
        split_string = text.split("|", 1)
        return split_string[0], split_string[1]
    
    def get_is_source_and_target_event_want(self, _source_out_going, _target_in_coming):
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
    
    def _bpmn_sequence_flow(self, flow_id, source_ref, target_ref):
        element = gfg.Element("bpmn:sequenceFlow", id=flow_id, sourceRef=source_ref, targetRef=target_ref)
        return element
      
    def bpmn_process(self, _get_list_flow_incoming_outgoing):
        print("---------------START PROCESS-------------------")
        process = gfg.Element("bpmn:process", id=self.event_id, isExecutable="false")

        print("---------------SEQUENCE-FLOW-------------------")
        list_edges = JsonDictionary() 
        for ls in self._get_sequence_list():
            json_object = json.dumps(ls, indent = 4)
            load_json = json.loads(json_object)
            flow_id = str(load_json['id'])
            sourceRef = str(load_json['sourceRef'])
            targetRef = str(load_json['targetRef'])

            key_source_target = []
            key_source_target.append(sourceRef)
            key_source_target.append(targetRef)
            list_edges.add(flow_id , key_source_target)
            
            _source = str(sourceRef).split("|",1)[0]
            _target = str(targetRef).split("|",1)[0]
            _source_in = str(_source).split("_",1)[0]
            _target_out = str(_target).split("_",1)[0]
            
            is_source_and_target_want = self.get_is_source_and_target_event_want(str(_source_in), str(_target_out))       
            if is_source_and_target_want == True:
                sequence_element = self._bpmn_sequence_flow(flow_id, _source, _target) 
                process.insert(1, sequence_element)
        
        print("---------------START IN-OUT-------------------")
        d_input = _get_list_flow_incoming_outgoing
        res = {}
        for i, v in d_input.items():
            res[v] = [i] if v not in res.keys() else res[v] + [i]

        for key, value in res.items():
            event_label = str(value[0]).split("|",3)
            tag = str(event_label[0])
            bpmn_event_tag_ = str(event_label[3])

            bpmn_tag = ""
            event_name = ""
            if bpmn_event_tag_ == "StartEvent":
                if tag == "bpmn:outgoing":              #FIRST START
                    event_name = str(event_label[2])    #LABEL ['bpmn:outgoing|Flow_936f2ad|manufactures customized bicycles']
                bpmn_tag = "bpmn:startEvent"
            elif bpmn_event_tag_ == "Activity":
                bpmn_tag = "bpmn:task"
            elif bpmn_event_tag_ == "ExclusiveGateway":
                bpmn_tag = "bpmn:exclusiveGateway"
            elif bpmn_event_tag_ == "ParallelGateway":
                bpmn_tag = "bpmn:parallelGateway"
            elif bpmn_event_tag_ == "EndEvent":
                bpmn_tag = "bpmn:endEvent"

            #Label
            event_name = str(event_label[2])
            if bpmn_event_tag_ == "StartEvent":
                event_name = "Start"
            elif bpmn_event_tag_ == "EndEvent":
                event_name = "End"
            
            element = gfg.Element(bpmn_tag, id=key, name=event_name)
            for x in value:
                _event = x.split("|", 2)
                bpmn_in_out = _event[0]
                flow_id = _event[1]
                if bpmn_in_out == "bpmn:incoming":
                    gfg.SubElement(element, bpmn_in_out).text = flow_id
                elif bpmn_in_out == "bpmn:outgoing":
                    gfg.SubElement(element, bpmn_in_out).text = flow_id
            process.insert(1, element)

        return process, list_edges