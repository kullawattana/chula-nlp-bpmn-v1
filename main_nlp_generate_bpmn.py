import spacy
import uuid
from extract.merge_phrases import Phrases
from models.json_model import JsonDictionary
from itertools import combinations 
from constants.word import SIGNAL_WORDS, ANTONYM_WORDS

nlp = spacy.load("en_core_web_sm")

class NLPGenerateBPMN():
    def __init__(self, text):
        self.text = text
        self.last_subject = []
        self.gateway_tag = []
        self.gateway_svo_list_split = []
        self.list_svo_to_generate_bpmn_in_out_diagram = []
        self.result_vo_subject = []
        self.signal_word_list = []
        self.sequence = 0
        self.subject = ""
        self.verb = ""
        self.objects = ""
        self.event_tag = ""
        self.signal_word = ""
        self.bpmn_direction = ""
        self.isPassiveActive = ""
        self.list_lane = []
        self.activity_list = JsonDictionary() 
        self.list_flow = JsonDictionary()

    def get_flow_id(self):
        return str(uuid.uuid4())[:7] 
    
    def record_subject(self):
        return "Subject_" + str(self.subject)

    def select_group_of_hashing_word(self, signal_word):
        if signal_word in SIGNAL_WORDS:
            self.signal_word_list.append(ANTONYM_WORDS)
            self.gateway_tag.append("ExclusiveGateway_")
        elif signal_word in ANTONYM_WORDS:
            self.signal_word_list.clear()  

    def prepare_task_in_out(self, list_svo):
        result = []
        new_list = []

        data = list_svo
        result = ([x + y for x, y in zip(data, data[1:] + data[:0])])     
        for x in result:
            split_text = x[:-1]
            re_format = str(split_text)
            ls = str(re_format).split("|")
            for y in ls:
                new_list.append(str(y)+"|")
        return new_list

    def startActivity(self, flow_id):
        #====================================================
        #1 START WITH [START EVENT + ACTIVITY EVENT] Rs, Es
        #====================================================
        flow_id = self.get_flow_id()
        _event_flow_id = "StartEvent_"+str(flow_id)
        vo_label = str("Start_" + "Start|" + str(_event_flow_id))
        self.list_svo_to_generate_bpmn_in_out_diagram.append(str(_event_flow_id) + "_Start_" + self.bpmn_direction + "|")
        self.result_vo_subject.append((vo_label, self.record_subject()))
        return flow_id   

    def createActivity(self, flow_id, vo):
        #====================================================
        #1 START WITH [START EVENT + ACTIVITY EVENT] Rs, Es
        #====================================================
        event_id = "Activity_" + flow_id
        vo_label = str("VO_" + vo + "|" + event_id)
        self.list_svo_to_generate_bpmn_in_out_diagram.append(str(event_id) + "_" + vo + "_" + self.bpmn_direction + "|")
        self.result_vo_subject.append((vo_label, self.record_subject()))           

    def activityEvent(self, vo):
        #====================================================
        #ACTIVITY EVENT
        #====================================================
        event_id = "Activity_" + self.get_flow_id()
        vo_label = str(self.event_tag + vo + "|" + event_id)
        #Rx, R+, Gxs G+s Gos
        if len(self.gateway_tag) != 0:
            if str(self.gateway_tag[0]) == "ExclusiveGateway_":
                self.gateway_svo_list_split.append(str(event_id) + "_" + vo + "_" + self.bpmn_direction + "|")
        else:
            self.list_svo_to_generate_bpmn_in_out_diagram.append(str(event_id) + "_" + vo + "_" + self.bpmn_direction + "|")
            self.result_vo_subject.append((vo_label, self.record_subject())) 

    def duplicateActivity(self, vo):
        #====================================================
        #GATEWAY START JOIN EVENT Rx, R+, Gxs G+s Gos
        #====================================================
        event_id = "Activity_" + self.get_flow_id()
        vo_label = str(self.event_tag + vo + "|" + event_id)
        self.result_vo_subject.append((vo_label, self.record_subject()))

        if str(self.gateway_tag[0]) == "ExclusiveGateway_":
            label_gateway = str(event_id) + "_" + vo + "_" + self.bpmn_direction + "|"
            self.gateway_svo_list_split.append(label_gateway)

    def gatewayStartSplit(self, vo):
        #====================================================
        #1 IF START WITH [GATEWAY SPLIT] EVENT FIRST Rx, R+ Gxs G+s Gos
        #====================================================
        if self.event_tag == "ExclusiveGateway_" :
            self.select_group_of_hashing_word(self.signal_word)
            event_id = "ExclusiveGateway_"+self.get_flow_id()
            _label = str(self.event_tag + vo + "|" + event_id)
            self.list_svo_to_generate_bpmn_in_out_diagram.append(str(event_id) + "_" + "Gxs?" + "_" + self.bpmn_direction + "|")
            self.result_vo_subject.append((_label, self.record_subject()))
        elif self.event_tag == "ParallelGateway_" :
            self.select_group_of_hashing_word(self.signal_word)
            event_id = "ParallelGateway_"+self.get_flow_id()
            _label = str(self.event_tag+vo + "|" + event_id)
            self.list_svo_to_generate_bpmn_in_out_diagram.append(str(event_id) + "_" + "G+s?" + "_" + self.bpmn_direction + "|")
            self.result_vo_subject.append((_label, self.record_subject()))        

    def tuplePairsJoinGateway(self):
        #====================================================
        #tuple pairs Gxs VO1 VO1 => [("Gxs|VO1"),("Gxs|VO2")]
        #====================================================
        split_value_list_pairs = []
        event_split = []
        open_join = []

        arr = (self.gateway_svo_list_split)
        for i in list(combinations(self.gateway_svo_list_split, 2)):
            if(i[0] == arr[0]):
                split_value_list_pairs.append(i)

        for key, val in split_value_list_pairs:
            #EVENT SPLIT
            event_split.append(key)
            event_split.append(val)
            #START OPEN JOIN GATEWAY
            if self.event_tag == "ExclusiveGateway_" or self.event_tag == "ParallelGateway_":
                open_join.append((val, self.event_tag + self.get_flow_id()))
        for members in event_split:
            self.list_svo_to_generate_bpmn_in_out_diagram.append(members)
        return open_join    

    def joinGateway(self, open_join):
        #====================================================
        #JOIN GATEWAY Rx, R+, Gxj, Goj, G+j
        #====================================================
        if str(self.gateway_tag[0]) == "ExclusiveGateway_":
            flow_gateway_id = "ExclusiveGateway_" + self.get_flow_id()
            for _in, _ in open_join:
                self.list_svo_to_generate_bpmn_in_out_diagram.append(_in)
                renew_label_gateway = flow_gateway_id + "_" + "Gxj" + "_" + self.bpmn_direction + "|"
                self.list_svo_to_generate_bpmn_in_out_diagram.append(renew_label_gateway)
        elif str(self.gateway_tag[0]) == "ParallelGateway_" :
            flow_gateway_id = "ParallelGateway_" + self.get_flow_id()
            for _in, _ in open_join:
                self.list_svo_to_generate_bpmn_in_out_diagram.append(_in)
                renew_label_gateway = flow_gateway_id + "_" + "G+j" + "_" + self.bpmn_direction + "|"
                self.list_svo_to_generate_bpmn_in_out_diagram.append(renew_label_gateway) 

    def startGateway(self):
        #====================================================
        #START GATEWAY Rx, R+ Gxs G+s Gos
        #====================================================
        if str(self.gateway_tag[0]) == "ExclusiveGateway_" or str(self.gateway_tag[0]) == "ParallelGateway_":
            event_id = str(self.gateway_tag[0]) + self.get_flow_id()
            _label = str(self.event_tag + "Gxs?" + "|" + event_id)
            self.result_vo_subject.append((_label, "Subject_" + str(self.subject)))
            self.list_svo_to_generate_bpmn_in_out_diagram.clear()   
            return event_id

    def interruptFlowAdjustListSplitGateway(self):  
        #====================================================
        # INTERRUPT FLOW TO ADJUST LIST BEFORE [Es, Ac, Gxs] => [Es,Ac | Ac,Gxs] and Continue gateway list Sequence  
        #====================================================
        ls = []
        for key, _ in self.result_vo_subject:
            internal_event_id = str(key).split("|",1)
            vo_label = "_" + str(internal_event_id[0]).split("_",1)[1]
            event_form = str(internal_event_id[1])
            ls.append(event_form + vo_label + "_" + self.bpmn_direction + "|")
        new_svo_list = self.prepare_task_in_out(ls)
        for _new in new_svo_list:
            self.list_svo_to_generate_bpmn_in_out_diagram.append(_new)  

    def endEvent(self):
        #====================================================
        #END FLOW  #Ee
        #====================================================
        flow_id = self.get_flow_id()
        event_id = "EndEvent_" + str(flow_id)
        vo_label = str("EndEvent_End|" + event_id)
        self.list_svo_to_generate_bpmn_in_out_diagram.append(str(event_id) + "_End_" + self.bpmn_direction + "|")  

        if len(self.last_subject) > 0:
            self.result_vo_subject.append((vo_label, "Subject_" + str(self.last_subject[-1])))
        else:
            self.result_vo_subject.append((vo_label, "Subject_"))    

    def svo_merge_order_sequence(self, d_input):
        res = {}
        for i, v in d_input.items():
            res[v] = [i] if v not in res.keys() else res[v] + [i]
        return res  

    def createLane(self, key, sequence_order):
        #====================================================
        #Create Lane
        #====================================================
        _lane = key.split("|", 1)
        _extract_lane_label = _lane[0].split("_", 1)
        lane_id = _extract_lane_label[1] + "|" +"Lane_" + self.get_flow_id()
        lane_label_id = str(sequence_order)+"|"+str(lane_id)
        return lane_label_id
            
    def getDataLane(self, value, lane_label_id):
        #====================================================
        #Get data from Lane
        #====================================================
        event_list = []
        data = []
        for l in value:
            _event = l.split("|", 1)
            event_label_id = str(_event[1])
            event_list.append(event_label_id)  
        print("event_list ::", event_list)
        print("=================================") 
        data.append((lane_label_id, event_list))
        return data            

    def startGroupSubjectForLane(self): 
        sequence_order = 0
        for sv in self.result_vo_subject:
            self.activity_list.add(sv[0], sv[1])
            print("sv[0], sv[1]", sv[0], sv[1])
        flow_svo = self.svo_merge_order_sequence(self.activity_list)  
        print("====================================")
        print("flow_svo::", flow_svo)
        json_list_lane = JsonDictionary()
        for key, value in flow_svo.items():
            print("====================================")
            print("value :::", value)
            sequence_order += 1            
            lane_label_id = self.createLane(key, sequence_order)
            print("====================================")
            print("lane_label_id :", lane_label_id)
            data = self.getDataLane(value, lane_label_id) 
            print("data :::", lane_label_id) 
            for sv in data:
                _list_lane_id = str(sv[0]).split("|",3)
                lane_id = str(_list_lane_id[2])
                self.list_flow.add(sv[0], sv[1])
                self.list_lane.append(str(lane_id)+"_di")
                json_list_lane.add(lane_id, sv[1])  
            print("json_list_lane :::", json_list_lane)   
            print("====================================")   
        return json_list_lane       

    def nlp_process(self, sent, is_show_gateway):
        custom = Phrases(sent)
        #TODO fix gateway later, not_show_gateway=True
        svos = custom.get_svo(sent, is_show_gateway)
        print("============================================")
        print("SVOS =>", svos)
        print("============================================")
        new_svos = custom.get_new_svos()
        print("============================================")
        print("NEW SVOS =>", new_svos)
        print("============================================")

        for svo in new_svos:
            self.signal_word = ""
            print("EXTRACT !!", svo[0], "|", svo[1], "|", svo[2], "|", svo[3], "|", svo[4], "|", svo[5], "|", svo[6], "|", svo[7])
            if svo[0] > 0:
                self.sequence = svo[0]
            if len(svo[1]) > 0:
                self.subject = str(svo[1])
                self.last_subject.append(self.subject)
            if len(svo[2]) > 0:
                self.verb = str(svo[2]).replace("!","")
            if len(svo[3]) > 0:
                self.objects = svo[3]
            if len(svo[4]) > 0:
                self.event_tag = str(svo[4])   
            if len(svo[5]) > 0:
                self.isPassiveActive = str(svo[5])        
            if len(svo[6]) > 0:
                self.signal_word = str(svo[6])
            if len(svo[7]) > 0:
                self.bpmn_direction = str(svo[7])
                
            vo = str(self.verb)+" "+str(self.objects).replace(",","").replace(".","")
            if self.sequence > 1:
                #ACTIVITY EVENT
                if self.event_tag == "VO_":
                    self.activityEvent(vo)
                #GATEWAY START JOIN EVENT Rx, R+, Gxs G+s Gos
                elif self.event_tag == "ExclusiveGateway_" or self.event_tag == "ParallelGateway_":
                    self.get_gateway(vo)
            else:
                #1 START WITH [START EVENT + ACTIVITY EVENT] Rs, Es
                flow_id = self.get_flow_id()
                self.startActivity(flow_id)
                self.createActivity(flow_id, vo)
                self.gatewayStartSplit(vo)
        
        return self.result_vo_subject 

    def get_gateway(self, vo):
        #GATEWAY START JOIN EVENT Rx, R+, Gxs G+s Gos
        self.select_group_of_hashing_word(self.signal_word)
        if len(self.signal_word_list) == 0 and len(self.gateway_tag) > 0:
            if str(self.signal_word) in ANTONYM_WORDS:
                print("33 - self.signal_word OTHERWISE :", self.signal_word)
                self.duplicateActivity(vo)
                #tuple pairs Gxs VO1 VO1 => [("Gxs|VO1"),("Gxs|VO2")]
                open_join = self.tuplePairsJoinGateway()
                #JOIN GATEWAY Rx, R+, Gxj, Goj, G+j
                self.joinGateway(open_join)
                #CLOSE JOIN
                self.gateway_tag.clear()
        else:
            # 3 START GATEWAY Rx, R+ Gxs G+s Gos
            if len(self.signal_word) > 0:
                if str(self.signal_word) in SIGNAL_WORDS:
                    print("22 - self.signal_word IF :", self.signal_word)
                    event_id = self.startGateway()
                    self.interruptFlowAdjustListSplitGateway()
                    self.start_open_split_gateway(event_id)

    def start_open_split_gateway(self, event_id): 
        # 3 START OPEN SPLIT GATEWAY Rx, R+ Gxs G+s Gos
        if str(self.gateway_tag[0]) == "ExclusiveGateway_":
            self.gateway_svo_list_split.append(str(event_id) + "_" + "Gxs?" + "_" + self.bpmn_direction + "|")
        elif str(self.gateway_tag[0]) == "ParallelGateway_":
            self.gateway_svo_list_split.append(str(event_id) + "_" + "G+s?" + "_" + self.bpmn_direction + "|") 
    
    def prepare_list_flow(self, is_show_gateway):
        self.nlp_process(self.text, is_show_gateway)
        self.endEvent()        
        json_list_lane = self.startGroupSubjectForLane()
        return self.list_flow, json_list_lane, self.list_lane, self.list_svo_to_generate_bpmn_in_out_diagram    