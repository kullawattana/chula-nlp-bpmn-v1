import uuid
from bpmn_process import BPMNProcess
from bpmn_diagram import BPMNDiagram
from bpmn_lane import BPMNLane
from xml.etree import ElementTree
import xml.etree.ElementTree as gfg
from main_nlp_generate_bpmn import NLPGenerateBPMN

import json

BPMNDI_ELEMENT_DIAGRAM_ID = "BPMNDiagram_1"
BPMNDI_ELEMENT_PLANE_ID = "BPMNPlane_1"

class CreateBPMNProcess(BPMNProcess):
    def __init__(self, process_id):
        super().__init__(process_id)

class CreateBPMNDiagram(BPMNDiagram):
    def __init__(self, res_group_by_event, list_lane, json_list_lane, participant_id, is_show_lane):
        super().__init__(res_group_by_event, list_lane, json_list_lane, participant_id, is_show_lane)

class BPMN():
    def __init__(self, sentence, process_name):
        self.text = sentence
        self.process_name = process_name
        self.process_id = "Process_"+str(uuid.uuid4())[:7]
        self.collaboration_id = "Collaboration_"+str(uuid.uuid4())[:7]
        self.participant_id = "Participant_"+str(uuid.uuid4())[:7]

    def definitions_element(self):
        root = gfg.Element("bpmn:definitions")
        root.set("xmlns:bpmn", "http://www.omg.org/spec/BPMN/20100524/MODEL")
        root.set("xmlns:bpmndi", "http://www.omg.org/spec/BPMN/20100524/DI")
        root.set("xmlns:dc", "http://www.omg.org/spec/DD/20100524/DC")
        root.set("xmlns:di", "http://www.omg.org/spec/DD/20100524/DI")
        root.set("xmlns:modeler", "http://camunda.org/schema/modeler/1.0")
        root.set("id", "Definitions_143w97m")
        root.set("targetNamespace", "http://bpmn.io/schema/bpmn")
        root.set("exporter", "Camunda Modeler")
        root.set("exporterVersion", "4.11.0")
        root.set("modeler:executionPlatform", "Camunda Platform")
        root.set("modeler:executionPlatformVersion", "7.15.0")
        return root    

    #for python >= 3.7
    def indent(self, elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def bpmn_process(self, is_show_lane, is_show_gateway):
        header_bpmn = self.definitions_element()

        print("================================Generate NLP...================================")
        nlpGenerate = NLPGenerateBPMN(self.text)
        list_flow, json_list_lane, list_lane, list_svo_to_generate_bpmn_in_out_diagram = nlpGenerate.prepare_list_flow(is_show_gateway)
        #print("list_flow: ", list_flow)
        #print("json_list_lane: ", json_list_lane)
        #print("list_lane: ", list_lane)
        #print("list_svo_to_generate_bpmn_in_out_diagram: ", list_svo_to_generate_bpmn_in_out_diagram)


        #Case 8 =====================================================
        # a1 = { 
        #     "1| A small company|Lane_bd0972a":[
        #         "StartEvent_a0aecaf",
        #         "Activity_8caf901",
        #     ],
        #     "2| BBB|Lane_bd0972b":[
        #         "Activity_8caf902",
        #         "Activity_8caf903",
        #     ],
        #     "3| CCC|Lane_bd0972c":[
        #         "Activity_8caf904",
        #         "Activity_8caf905",
        #         "Activity_8caf907"
        #     ],
        #     "4| DDD|Lane_bd0972d":[
        #         "Activity_8caf906",
        #         "Activity_8caf908",
        #     ],
        #     "5| EEE|Lane_bd0972e":[
        #         "Activity_8caf909",
        #         "EndEvent_8caf000"  
        #     ],
        # }
        # a11 = json.dumps(a1)
        # list_flow = json.loads(a11)

        # b2 = {
        #     "Lane_bd0972a":[
        #         "StartEvent_a0aecaf",
        #         "Activity_8caf901",        
        #     ],
        #     "Lane_bd0972b":[
        #         "Activity_8caf902",
        #         "Activity_8caf903",  
        #     ],
        #     "Lane_bd0972c":[
        #         "Activity_8caf904",
        #         "Activity_8caf905",
        #         "Activity_8caf907"
        #     ],
        #     "Lane_bd0972d":[
        #         "Activity_8caf906",
        #         "Activity_8caf908",         
        #     ],
        #     "Lane_bd0972e":[
        #         "Activity_8caf909",
        #         "EndEvent_8caf000"          
        #     ],
        # }

        # list_svo_to_generate_bpmn_in_out_diagram = [
        #     "StartEvent_a0aecaf_Start_BPMN-MOVE-NEXT|",
        #     "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",

        #     "Activity_8caf901_aaa_BPMN-MOVE-NEXT|",
        #     "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",

        #     "Activity_8caf902_bbb_BPMN-MOVE-DOWN|",
        #     "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",

        #     "Activity_8caf903_ccc_BPMN-MOVE-NEXT|",
        #     "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",

        #     "Activity_8caf904_ddd_BPMN-MOVE-DOWN|",
        #     "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",

        #     #gateway loop 1
        #     "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        #     "Activity_8caf905_eee_BPMN-MOVE-NEXT|",

        #     "ExclusiveGateway_fca89aa_Gxs?_BPMN-MOVE-NEXT|",
        #     "Activity_8caf906_fff_BPMN-MOVE-DOWN|",

        #     "Activity_8caf905_eee_BPMN-MOVE-NEXT|",
        #     "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        #     "Activity_8caf906_fff_BPMN-MOVE-DOWN|",
        #     "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",

        #     "ExclusiveGateway_fca89bb_Gxj?_BPMN-MOVE-NEXT|",
        #     "Activity_8caf907_ggg_BPMN-MOVE-NEXT|",
        #     #End loop

        #     "Activity_8caf907_ggg_BPMN-MOVE-NEXT|",
        #     "Activity_8caf908_hhh_BPMN-MOVE-DOWN|",

        #     "Activity_8caf908_hhh_BPMN-MOVE-DOWN|",
        #     "Activity_8caf909_iii_BPMN-MOVE-DOWN|",

        #     "Activity_8caf909_iii_BPMN-MOVE-DOWN|",
        #     "EndEvent_8caf000_end_BPMN-MOVE-NEXT|",
        # ]

        # b12 = json.dumps(b2)
        # json_list_lane = json.loads(b12)

        # list_lane = [
        #     "Lane_bd0972a_di",
        #     "Lane_bd0972b_di",
        #     "Lane_bd0972c_di",
        #     "Lane_bd0972d_di"
        # ]

        print("================================START BPMN=====================================")
        bpmn_lane = BPMNLane(list_flow=list_flow)
        
        print("================================START BPMN PROCESS=============================")
        process = CreateBPMNProcess(process_id=self.process_id)
        process._prepare_task_in_out(list_svo_to_generate_bpmn_in_out_diagram)
        _source_target_list = process._get_list_flow_incoming_outgoing()
        result_process, res_group_by_event = process.bpmn_process(_source_target_list)

        print("================================START Collaboration============================")
        if is_show_lane == True:
            collaboration = bpmn_lane.prepare_collaboration(self.collaboration_id, self.participant_id, self.process_name, self.process_id)
            header_bpmn.append(collaboration)
            lane_process = bpmn_lane.prepare_lane_set()
            result_process.append(lane_process)

        header_bpmn.append(result_process)
        print("================================START BPMN DIAGRAM=============================")
        diagram = CreateBPMNDiagram(res_group_by_event, list_lane, json_list_lane, self.participant_id, is_show_lane)
        result_diagram = diagram.bpmn_edges(diagram_id=BPMNDI_ELEMENT_DIAGRAM_ID, plan_id=BPMNDI_ELEMENT_PLANE_ID, uuid=self.process_id, collaboration_id=self.collaboration_id)
        header_bpmn.append(result_diagram)
        print("RESULT DIAGRAM =>", ElementTree.tostring(header_bpmn).decode("utf-8"))

        print("================================Generate BPMN...===============================")
        #for python >= 3.9 
        #result_xml = gfg.ElementTree(header_bpmn)
        #gfg.indent(result_xml, space="\t", level=0)
        #result_xml.write("result_bpmn_process_from_nlp.xml", encoding="utf-8")
        #result_xml.write("result_bpmn_process_from_nlp.bpmn", encoding="utf-8")

        #for python >= 3.7
        tree = gfg.ElementTree(header_bpmn)    
        xml_data = self.indent(header_bpmn)
        tree.write("data/result_bpmn_process_from_nlp.xml", encoding="utf-8", xml_declaration=True)
        tree.write("data/result_bpmn_process_from_nlp.bpmn", encoding="utf-8", xml_declaration=True)
        return list_flow, json_list_lane, list_svo_to_generate_bpmn_in_out_diagram