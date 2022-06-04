import uuid
import xml.etree.ElementTree as gfg

class BPMNLane():
    def __init__(self, list_flow):
        self.list_flow = list_flow
    
    def bpmn_diagram_plan(self, event_id, uuid):
        element = gfg.Element("bpmndi:BPMNPlane", id=event_id, bpmnElement=uuid)
        return element
        
    def bpmn_collaboration(self, collaboration_id):
        collaboration = gfg.Element("bpmn:collaboration", id=collaboration_id)
        return collaboration
    
    def bpmn_participant(self, participant_id, event_name, process_ref_id):
        participant = gfg.Element("bpmn:participant", id=participant_id, name=event_name, processRef=process_ref_id)
        return participant
    
    def split_text(self, text):
        split_string = text.split("|", 1)
        return split_string[0], split_string[1]

    def prepare_collaboration(self, collaboration_id, participant_id, event_name, process_ref_id):
        collaboration = self.bpmn_collaboration(collaboration_id)
        participant = self.bpmn_participant(participant_id, event_name, process_ref_id)
        collaboration.append(participant)
        return collaboration

    def prepare_lane_set(self):
        lane_set = gfg.Element("bpmn:laneSet", id="LaneSet_"+str(uuid.uuid4())[:7])
        for key, values in self.list_flow.items():
            _, extract_lane_id = self.split_text(key)
            lane_name, lane_id = self.split_text(extract_lane_id)
            elements = self.add_lane_flow_node_ref(values, lane_id, lane_name)
            lane_set.append(elements)
        return lane_set

    def add_lane_flow_node_ref(self, values, lane_id, lane_name):
        element = gfg.Element("bpmn:lane", id=lane_id, name=lane_name)
        for bpmn_event in values:
            _event = str(bpmn_event).split("_",1)
            start_end_event = _event[0]
            if start_end_event == "StartEvent" or start_end_event == "EndEvent":
                event_id = "Event_"+_event[1]
                gfg.SubElement(element, "bpmn:flowNodeRef").text = event_id
            else:
                _label_event = str(bpmn_event).split("_",1)
                if _label_event[0] == "ExclusiveGateway" or _label_event[0] == "ParallelGateway":
                    gfg.SubElement(element, "bpmn:flowNodeRef").text = "Gateway_"+_label_event[1]
                else:
                    gfg.SubElement(element, "bpmn:flowNodeRef").text = bpmn_event
        return element