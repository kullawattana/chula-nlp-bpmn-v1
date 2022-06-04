## Step 0 : Get Sentence
- text = "The Vacation Request Process starts when an employee of the organization submits a vacation request. Once the requirement is registered, the request is received by the immediate supervisor; the supervisor must approve or reject the request. If the request is rejected the application is returned to the applicant/employee who can review the rejection reasons. If the request is approved a notification is generated to the Human Resources representative, who must complete the respective administrative procedures."
- process_name = "BPMN Process" 
- is_show_lane = True/False

# Processing with BPMN class
```python
bpmn = BPMN(text, process_name)
bpmn.bpmn_process(is_show_lane)
```

# Start Generate BPMN header, NLP
```python
# 1. header xml
header_bpmn = self.definitions_element()
# 2. NLP
list_flow, json_list_lane, list_lane, list_svo_to_generate_bpmn_in_out_diagram = nlpGenerate.prepare_list_flow()
```

# Get data BPMN Lane
```python
# 3. BPMN Lane
bpmn_lane = BPMNLane(list_flow=list_flow)
```

# Get BPMN Process
```python
process = CreateBPMNProcess(process_id=self.process_id)
process._prepare_task_in_out(list_svo_to_generate_bpmn_in_out_diagram)
_source_target_list = process._get_list_flow_incoming_outgoing()
result_process, res_group_by_event = process.bpmn_process(_source_target_list)
```

# Get BPMN Collaboration with Lane
```python
collaboration = bpmn_lane.prepare_collaboration(self.collaboration_id, self.participant_id, self.process_name, self.process_id)
header_bpmn.append(collaboration)
lane_process = bpmn_lane.prepare_lane_set()
result_process.append(lane_process)
```

# Add header
```python
header_bpmn.append(result_process)
```

# Get BPMN Diagram 
```python
diagram = CreateBPMNDiagram(res_group_by_event, list_lane, json_list_lane, self.participant_id, is_show_lane)
result_diagram = diagram.bpmn_edges(diagram_id=BPMNDI_ELEMENT_DIAGRAM_ID, plan_id=BPMNDI_ELEMENT_PLANE_ID, uuid=self.process_id, collaboration_id=self.collaboration_id)
header_bpmn.append(result_diagram)
```

# Get Result BPMN (.xml, .bpmn)
```python
print("RESULT DIAGRAM =>", ElementTree.tostring(header_bpmn).decode("utf-8"))
result_xml = gfg.ElementTree(header_bpmn)
gfg.indent(result_xml, space="\t", level=0)
result_xml.write("result_bpmn_process_from_nlp.xml", encoding="utf-8")
result_xml.write("result_bpmn_process_from_nlp.bpmn", encoding="utf-8")
```

## Step 1 : Generate NLP

| TAG           | Word |
| ---           | ---  |
| nsubj         | The Vacation Request Process |
| ROOT          | starts |
| advmod        | when |
| nsubj         | an employee |
| prep          | of |
| pobj          | the organization |
| advcl         | submits |
| dobj          | a vacation request |
| punct         | . |
| mark          | Once |
| nsubjpass     | the requirement |
| auxpass       | is |
| ...           | ... |

## Step 2 : Get SVOS
### Structure (seq, Subject, Verb, Object, bpmn_label, isPassive/isActive, signal_word)

```python
SVOS => [
    (1, '-', 'starts', The Vacation Request Process, 'VO_', 'isActive', []), 
    (2, 'employee', 'submits', a vacation request, 'VO_', 'isActive', []), 
    (3, '-', 'registered', the requirement, 'VO_', 'isPassive', []), 
    (4, 'the request', 'received', the immediate supervisor, 'VO_', 'isPassive', []), 
    (5, 'the supervisor', 'approve', the request, 'VO_', 'isActive', []), 
    (5, 'the supervisor', 'reject', the request, 'VO_', 'isActive', []), 
    (7, '-', 'rejected', the request, 'VO_', 'isPassive', []), 
    (8, 'the application', 'returned', the applicant/employee, 'VO_', 'isPassive', []), 
    (9, '-', 'review', the rejection reasons, 'VO_', 'isActive', []), 
    (10, '-', 'approved', the request, 'VO_', 'isPassive', []), 
    (11, 'a notification', 'generated', the Human Resources representative, 'VO_', 'isPassive', []), 
    (12, '-', 'complete', the respective administrative procedures, 'VO_', 'isActive', [])]
```

## Step 3 : Check subject with similarity
### similar = doc1.similarity(doc2)

0.43582738464452436     | the supervisor | employee
0.7503742116576682      | the supervisor | the request
1.0                     | the supervisor | the supervisor
0.7708459344636939      | the supervisor | the application
0.6570313688018999      | the supervisor | a notification

## Step 4 : finalist order role list
role_list_subject :: ['employee', 'the supervisor']

## Step 5 : Get new SVOS with direction of BPMN ["BPMN_MOVE_NEXT", "BPMN_MOVE_DOWN", "BPMN_MOVE_UP"] by role_list_subject
### Structure (seq, Subject, Verb, Object, bpmn_label, isPassive/isActive, signal_word, bpmn_direction)

```python
NEW SVOS => [
    (2, 'employee', 'submits', a vacation request, 'VO_', 'isActive', [], 'BPMN_MOVE_NEXT'), 
    (3, 'employee', 'registered', the requirement, 'VO_', 'isPassive', [], 'BPMN_MOVE_NEXT'), 
    (4, 'employee', 'received', the immediate supervisor, 'VO_', 'isPassive', [], 'BPMN_MOVE_NEXT'), 
    (5, 'the supervisor', 'approve', the request, 'VO_', 'isActive', [], 'BPMN_MOVE_DOWN'), 
    (5, 'the supervisor', 'reject', the request, 'VO_', 'isActive', [], 'BPMN_MOVE_NEXT'), 
    (7, 'the supervisor', 'rejected', the request, 'VO_', 'isPassive', [], 'BPMN_MOVE_NEXT'), 
    (8, 'the supervisor', 'returned', the applicant/employee, 'VO_', 'isPassive', [], 'BPMN_MOVE_NEXT'), 
    (9, 'the supervisor', 'review', the rejection reasons, 'VO_', 'isActive', [], 'BPMN_MOVE_NEXT'), 
    (10, 'the supervisor', 'approved', the request, 'VO_', 'isPassive', [], 'BPMN_MOVE_NEXT'), 
    (11, 'the supervisor', 'generated', the Human Resources representative, 'VO_', 'isPassive', [], 'BPMN_MOVE_NEXT'), 
    (12, 'the supervisor', 'complete', the respective administrative procedures, 'VO_', 'isActive', [], 'BPMN_MOVE_NEXT')]
```

## Step 6.1 : Get value, lane_label_id, pairs event (Employee)

```python
#role subject 2-4 : employee

#1
value ::: [
    'VO_submits a vacation request|Activity_89a46c8', 
    'VO_registered the requirement|Activity_c5a12e8', 
    'VO_received the immediate supervisor|Activity_f741cb1'
    ]

#2
#lane_label_id : 1|employee|Lane_56a987b

#3
#pairs event
_event ['VO_submits a vacation request', 'Activity_89a46c8']
_event ['VO_registered the requirement', 'Activity_c5a12e8']
_event ['VO_received the immediate supervisor', 'Activity_f741cb1']

#4
event_list :: ['Activity_89a46c8', 'Activity_c5a12e8', 'Activity_f741cb1']

#5
json_list_lane ::: {'Lane_56a987b': ['Activity_89a46c8', 'Activity_c5a12e8', 'Activity_f741cb1']}
```

## Step 6.2 : Get value, lane_label_id, pairs event (supervisor)

```python
#role subject 5-12 : supervisor

#1
value ::: [
    'VO_approve the request|Activity_0506b6b', 
    'VO_reject the request|Activity_2fb3966', 
    'VO_rejected the request|Activity_461464b', 
    'VO_returned the applicant/employee|Activity_4711643', 
    'VO_review the rejection reasons|Activity_1b2d6fc', 
    'VO_approved the request|Activity_59772d2', 
    'VO_generated the Human Resources representative|Activity_50abe62', 
    'VO_complete the respective administrative procedures|Activity_ca9b524', 
    'EndEvent_End|EndEvent_47e076f'
    ]

#2
#lane_label_id : 2|the supervisor|Lane_f6ad04f

#3
#pairs event
_event ['VO_approve the request', 'Activity_0506b6b']
_event ['VO_reject the request', 'Activity_2fb3966']
_event ['VO_rejected the request', 'Activity_461464b']
_event ['VO_returned the applicant/employee', 'Activity_4711643']
_event ['VO_review the rejection reasons', 'Activity_1b2d6fc']
_event ['VO_approved the request', 'Activity_59772d2']
_event ['VO_generated the Human Resources representative', 'Activity_50abe62']
_event ['VO_complete the respective administrative procedures', 'Activity_ca9b524']
_event ['EndEvent_End', 'EndEvent_47e076f']

#4
event_list :: ['Activity_0506b6b', 'Activity_2fb3966', 'Activity_461464b', 'Activity_4711643', 'Activity_1b2d6fc', 'Activity_59772d2', 'Activity_50abe62', 'Activity_ca9b524', 'EndEvent_47e076f']

#5
json_list_lane ::: {'Lane_f6ad04f': ['Activity_0506b6b', 'Activity_2fb3966', 'Activity_461464b', 'Activity_4711643', 'Activity_1b2d6fc', 'Activity_59772d2', 'Activity_50abe62', 'Activity_ca9b524', 'EndEvent_47e076f']}
```

## Step 7 : get list_svo_to_generate_bpmn_in_out_diagram

```python
= [
    'Activity_89a46c8_submits a vacation request|', 
    'Activity_c5a12e8_registered the requirement|', 
    'Activity_f741cb1_received the immediate supervisor|', 
    'Activity_0506b6b_approve the request|', 
    'Activity_2fb3966_reject the request|', 
    'Activity_461464b_rejected the request|', 
    'Activity_4711643_returned the applicant/employee|', 
    'Activity_1b2d6fc_review the rejection reasons|', 
    'Activity_59772d2_approved the request|', 
    'Activity_50abe62_generated the Human Resources representative|', 
    'Activity_ca9b524_complete the respective administrative procedures|', 
    'EndEvent_47e076f_End|'
]

#CHECK ADD NEW SEQUENCE BEFORE END :: 
Flow_75baf12 [
    'Flow_75baf12_Activity_50abe62_generated the Human Resources representative', 
    'Flow_75baf12_Activity_ca9b524_complete the respective administrative procedures'
]
```

## Step 8 : get source - target list
```python
_source_target_list :: {
    'bpmn:outgoing|Flow_3c6274c|submits a vacation request|Activity': 'Activity_89a46c8', 
    'bpmn:incoming|Flow_3c6274c|registered the requirement|Activity': 'Activity_c5a12e8', 
    'bpmn:outgoing|Flow_7640dbd|received the immediate supervisor|Activity': 'Activity_f741cb1', 
    'bpmn:incoming|Flow_7640dbd|approve the request|Activity': 'Activity_0506b6b', 
    'bpmn:outgoing|Flow_d9d3430|reject the request|Activity': 'Activity_2fb3966', 
    'bpmn:incoming|Flow_d9d3430|rejected the request|Activity': 'Activity_461464b', 
    'bpmn:outgoing|Flow_2ce1cb9|returned the applicant/employee|Activity': 'Activity_4711643', 
    'bpmn:incoming|Flow_2ce1cb9|review the rejection reasons|Activity': 'Activity_1b2d6fc', 
    'bpmn:outgoing|Flow_a9affd3|approved the request|Activity': 'Activity_59772d2', 
    'bpmn:incoming|Flow_a9affd3|generated the Human Resources representative|Activity': 'Activity_50abe62', 
    'bpmn:outgoing|Flow_75baf12|generated the Human Resources representative|Activity': 'Activity_50abe62', 
    'bpmn:incoming|Flow_75baf12|complete the respective administrative procedures|Activity': 'Activity_ca9b524', 'bpmn:outgoing|Flow_234ea3c|complete the respective administrative procedures|Activity': 'Activity_ca9b524', 'bpmn:incoming|Flow_234ea3c|End|EndEvent': 'Event_47e076f'
}
```

## Step 9 Get Sequence Flow

```python
# flow_id : Flow_3c6274c 
    sourceRef : Activity_89a46c8 targetRef : Activity_c5a12e8 
    event_name : 
# flow_id : Flow_d1e102c 
    sourceRef : Activity_c5a12e8 targetRef : Activity_f741cb1 
    event_name : 
# flow_id : Flow_7640dbd 
    sourceRef : Activity_f741cb1 targetRef : Activity_0506b6b 
    event_name : 
# flow_id : Flow_cc89254 
    sourceRef : Activity_0506b6b targetRef : Activity_2fb3966 
    event_name : 
# flow_id : Flow_d9d3430 
    sourceRef : Activity_2fb3966 targetRef : Activity_461464b 
    event_name : 
# flow_id : Flow_ab61582 
    sourceRef : Activity_461464b targetRef : Activity_4711643 
    event_name : 
# flow_id : Flow_2ce1cb9 
    sourceRef : Activity_4711643 targetRef : Activity_1b2d6fc 
    event_name : 
# flow_id : Flow_c5bdb5b 
    sourceRef : Activity_1b2d6fc targetRef : Activity_59772d2 
    event_name : 
# flow_id : Flow_a9affd3 
    sourceRef : Activity_59772d2 targetRef : Activity_50abe62 
    event_name : 
# flow_id : Flow_75baf12 
    sourceRef : Activity_50abe62 targetRef : Activity_ca9b524 
    event_name : 
# flow_id : Flow_234ea3c 
    sourceRef : Activity_ca9b524 targetRef : Event_47e076f 
    event_name : 
```

## Step 10 Start IN-OUT Collaboration Diagram

## Step 11 Start Edges (x1,x2,y1,y2)
```python
self.counter_split_gateway ==> 0 : Activity : Activity
ACT-ACT x1, x2, y1, y2 :: 100 160 0 0
self.counter_split_gateway ==> 0 : Activity : Activity
ACT-ACT x1, x2, y1, y2 :: 260 320 0 0
self.counter_split_gateway ==> 0 : Activity : Activity
ACT-ACT x1, x2, y1, y2 :: 420 480 0 0
self.counter_split_gateway ==> 0 : Activity : Activity
ACT-ACT x1, x2, y1, y2 :: 580 640 0 0
self.counter_split_gateway ==> 0 : Activity : Activity
ACT-ACT x1, x2, y1, y2 :: 740 800 0 0
self.counter_split_gateway ==> 0 : Activity : Activity
ACT-ACT x1, x2, y1, y2 :: 900 960 0 0
self.counter_split_gateway ==> 0 : Activity : Activity
ACT-ACT x1, x2, y1, y2 :: 1060 1120 0 0
self.counter_split_gateway ==> 0 : Activity : Activity
ACT-ACT x1, x2, y1, y2 :: 1220 1280 0 0
self.counter_split_gateway ==> 0 : Activity : Activity
ACT-ACT x1, x2, y1, y2 :: 1380 1440 0 0
self.counter_split_gateway ==> 0 : Activity : Activity
ACT-ACT x1, x2, y1, y2 :: 1540 1600 0 0
self.counter_split_gateway ==> 0 : Activity : Event
ACT-END x1, x2, y1, y2 :: 1700 1722 0 0
```

## Step 12 Get [activity|x2] (x2 is a position scale of BPMN)
```python
LIST RENEW ===> [
    'Activity_89a46c8|160', 
    'Activity_c5a12e8|160', 
    'Activity_f741cb1|320', 
    'Activity_0506b6b|480', 
    'Activity_2fb3966|640', 
    'Activity_461464b|800', 
    'Activity_4711643|960', 
    'Activity_1b2d6fc|1120', 
    'Activity_59772d2|1280', 
    'Activity_50abe62|1440', 
    'Activity_ca9b524|1600', 
    'EndEvent_47e076f|1722'
]
```

## Step 13 Get Result XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" xmlns:modeler="http://camunda.org/schema/modeler/1.0" id="Definitions_143w97m" targetNamespace="http://bpmn.io/schema/bpmn" exporter="Camunda Modeler" exporterVersion="4.11.0" modeler:executionPlatform="Camunda Platform" modeler:executionPlatformVersion="7.15.0">
   <bpmn:collaboration id="Collaboration_0b9bb33">
      <bpmn:participant id="Participant_ecd836c" name="BPMN Process" processRef="Process_1453a23" />
   </bpmn:collaboration>
   <bpmn:process id="Process_1453a23" isExecutable="false">
      <bpmn:sequenceFlow id="Flow_3c6274c" sourceRef="Activity_89a46c8" targetRef="Activity_c5a12e8" />
      <bpmn:endEvent id="Event_47e076f" name="End">
         <bpmn:incoming>Flow_234ea3c</bpmn:incoming>
      </bpmn:endEvent>
      <bpmn:task id="Activity_ca9b524" name="complete the respective administrative procedures">
         <bpmn:incoming>Flow_75baf12</bpmn:incoming>
         <bpmn:outgoing>Flow_234ea3c</bpmn:outgoing>
      </bpmn:task>
      <bpmn:task id="Activity_50abe62" name="generated the Human Resources representative">
         <bpmn:incoming>Flow_a9affd3</bpmn:incoming>
         <bpmn:outgoing>Flow_75baf12</bpmn:outgoing>
      </bpmn:task>
      <bpmn:task id="Activity_59772d2" name="approved the request">
         <bpmn:outgoing>Flow_a9affd3</bpmn:outgoing>
      </bpmn:task>
      <bpmn:task id="Activity_1b2d6fc" name="review the rejection reasons">
         <bpmn:incoming>Flow_2ce1cb9</bpmn:incoming>
      </bpmn:task>
      <bpmn:task id="Activity_4711643" name="returned the applicant/employee">
         <bpmn:outgoing>Flow_2ce1cb9</bpmn:outgoing>
      </bpmn:task>
      <bpmn:task id="Activity_461464b" name="rejected the request">
         <bpmn:incoming>Flow_d9d3430</bpmn:incoming>
      </bpmn:task>
      <bpmn:task id="Activity_2fb3966" name="reject the request">
         <bpmn:outgoing>Flow_d9d3430</bpmn:outgoing>
      </bpmn:task>
      <bpmn:task id="Activity_0506b6b" name="approve the request">
         <bpmn:incoming>Flow_7640dbd</bpmn:incoming>
      </bpmn:task>
      <bpmn:task id="Activity_f741cb1" name="received the immediate supervisor">
         <bpmn:outgoing>Flow_7640dbd</bpmn:outgoing>
      </bpmn:task>
      <bpmn:task id="Activity_c5a12e8" name="registered the requirement">
         <bpmn:incoming>Flow_3c6274c</bpmn:incoming>
      </bpmn:task>
      <bpmn:task id="Activity_89a46c8" name="submits a vacation request">
         <bpmn:outgoing>Flow_3c6274c</bpmn:outgoing>
      </bpmn:task>
      <bpmn:sequenceFlow id="Flow_234ea3c" sourceRef="Activity_ca9b524" targetRef="Event_47e076f" />
      <bpmn:sequenceFlow id="Flow_75baf12" sourceRef="Activity_50abe62" targetRef="Activity_ca9b524" />
      <bpmn:sequenceFlow id="Flow_a9affd3" sourceRef="Activity_59772d2" targetRef="Activity_50abe62" />
      <bpmn:sequenceFlow id="Flow_c5bdb5b" sourceRef="Activity_1b2d6fc" targetRef="Activity_59772d2" />
      <bpmn:sequenceFlow id="Flow_2ce1cb9" sourceRef="Activity_4711643" targetRef="Activity_1b2d6fc" />
      <bpmn:sequenceFlow id="Flow_ab61582" sourceRef="Activity_461464b" targetRef="Activity_4711643" />
      <bpmn:sequenceFlow id="Flow_d9d3430" sourceRef="Activity_2fb3966" targetRef="Activity_461464b" />
      <bpmn:sequenceFlow id="Flow_cc89254" sourceRef="Activity_0506b6b" targetRef="Activity_2fb3966" />
      <bpmn:sequenceFlow id="Flow_7640dbd" sourceRef="Activity_f741cb1" targetRef="Activity_0506b6b" />
      <bpmn:sequenceFlow id="Flow_d1e102c" sourceRef="Activity_c5a12e8" targetRef="Activity_f741cb1" />
      <bpmn:laneSet id="LaneSet_d168056">
         <bpmn:lane id="Lane_56a987b" name="employee">
            <bpmn:flowNodeRef>Activity_89a46c8</bpmn:flowNodeRef>
            <bpmn:flowNodeRef>Activity_c5a12e8</bpmn:flowNodeRef>
            <bpmn:flowNodeRef>Activity_f741cb1</bpmn:flowNodeRef>
         </bpmn:lane>
         <bpmn:lane id="Lane_f6ad04f" name="the supervisor">
            <bpmn:flowNodeRef>Activity_0506b6b</bpmn:flowNodeRef>
            <bpmn:flowNodeRef>Activity_2fb3966</bpmn:flowNodeRef>
            <bpmn:flowNodeRef>Activity_461464b</bpmn:flowNodeRef>
            <bpmn:flowNodeRef>Activity_4711643</bpmn:flowNodeRef>
            <bpmn:flowNodeRef>Activity_1b2d6fc</bpmn:flowNodeRef>
            <bpmn:flowNodeRef>Activity_59772d2</bpmn:flowNodeRef>
            <bpmn:flowNodeRef>Activity_50abe62</bpmn:flowNodeRef>
            <bpmn:flowNodeRef>Activity_ca9b524</bpmn:flowNodeRef>
            <bpmn:flowNodeRef>Event_47e076f</bpmn:flowNodeRef>
         </bpmn:lane>
      </bpmn:laneSet>
   </bpmn:process>
   <bpmndi:BPMNDiagram id="BPMNDiagram_1">
      <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Collaboration_0b9bb33">
         <bpmndi:BPMNEdge id="Flow_3c6274c_di" bpmnElement="Flow_3c6274c">
            <di:waypoint x="100" y="0" />
            <di:waypoint x="160" y="0" />
         </bpmndi:BPMNEdge>
         <bpmndi:BPMNEdge id="Flow_d1e102c_di" bpmnElement="Flow_d1e102c">
            <di:waypoint x="260" y="0" />
            <di:waypoint x="320" y="0" />
         </bpmndi:BPMNEdge>
         <bpmndi:BPMNEdge id="Flow_7640dbd_di" bpmnElement="Flow_7640dbd">
            <di:waypoint x="420" y="0" />
            <di:waypoint x="480" y="0" />
         </bpmndi:BPMNEdge>
         <bpmndi:BPMNEdge id="Flow_cc89254_di" bpmnElement="Flow_cc89254">
            <di:waypoint x="580" y="0" />
            <di:waypoint x="640" y="0" />
         </bpmndi:BPMNEdge>
         <bpmndi:BPMNEdge id="Flow_d9d3430_di" bpmnElement="Flow_d9d3430">
            <di:waypoint x="740" y="0" />
            <di:waypoint x="800" y="0" />
         </bpmndi:BPMNEdge>
         <bpmndi:BPMNEdge id="Flow_ab61582_di" bpmnElement="Flow_ab61582">
            <di:waypoint x="900" y="0" />
            <di:waypoint x="960" y="0" />
         </bpmndi:BPMNEdge>
         <bpmndi:BPMNEdge id="Flow_2ce1cb9_di" bpmnElement="Flow_2ce1cb9">
            <di:waypoint x="1060" y="0" />
            <di:waypoint x="1120" y="0" />
         </bpmndi:BPMNEdge>
         <bpmndi:BPMNEdge id="Flow_c5bdb5b_di" bpmnElement="Flow_c5bdb5b">
            <di:waypoint x="1220" y="0" />
            <di:waypoint x="1280" y="0" />
         </bpmndi:BPMNEdge>
         <bpmndi:BPMNEdge id="Flow_a9affd3_di" bpmnElement="Flow_a9affd3">
            <di:waypoint x="1380" y="0" />
            <di:waypoint x="1440" y="0" />
         </bpmndi:BPMNEdge>
         <bpmndi:BPMNEdge id="Flow_75baf12_di" bpmnElement="Flow_75baf12">
            <di:waypoint x="1540" y="0" />
            <di:waypoint x="1600" y="0" />
         </bpmndi:BPMNEdge>
         <bpmndi:BPMNEdge id="Flow_234ea3c_di" bpmnElement="Flow_234ea3c">
            <di:waypoint x="1700" y="0" />
            <di:waypoint x="1722" y="0" />
         </bpmndi:BPMNEdge>
         <bpmndi:BPMNShape id="Activity_89a46c8_di" bpmnElement="Activity_89a46c8">
            <dc:Bounds x="160" y="58" width="100" height="80" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Activity_c5a12e8_di" bpmnElement="Activity_c5a12e8">
            <dc:Bounds x="160" y="58" width="100" height="80" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Activity_f741cb1_di" bpmnElement="Activity_f741cb1">
            <dc:Bounds x="320" y="58" width="100" height="80" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Activity_0506b6b_di" bpmnElement="Activity_0506b6b">
            <dc:Bounds x="480" y="58" width="100" height="80" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Activity_2fb3966_di" bpmnElement="Activity_2fb3966">
            <dc:Bounds x="640" y="58" width="100" height="80" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Activity_461464b_di" bpmnElement="Activity_461464b">
            <dc:Bounds x="800" y="58" width="100" height="80" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Activity_4711643_di" bpmnElement="Activity_4711643">
            <dc:Bounds x="960" y="58" width="100" height="80" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Activity_1b2d6fc_di" bpmnElement="Activity_1b2d6fc">
            <dc:Bounds x="1120" y="58" width="100" height="80" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Activity_59772d2_di" bpmnElement="Activity_59772d2">
            <dc:Bounds x="1280" y="58" width="100" height="80" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Activity_50abe62_di" bpmnElement="Activity_50abe62">
            <dc:Bounds x="1440" y="58" width="100" height="80" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Activity_ca9b524_di" bpmnElement="Activity_ca9b524">
            <dc:Bounds x="1600" y="58" width="100" height="80" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Event_47e076f_di" bpmnElement="Event_47e076f">
            <dc:Bounds x="1722" y="80" width="36" height="36" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Lane_f6ad04f_id" bpmnElement="Lane_f6ad04f" isHorizontal="true">
            <dc:Bounds x="100" y="20" width="1732" height="175" />
         </bpmndi:BPMNShape>
         <bpmndi:BPMNShape id="Participant_ecd836c_di" bpmnElement="Participant_ecd836c" isHorizontal="true">
            <dc:Bounds x="70" y="20" width="1762" height="175" />
         </bpmndi:BPMNShape>
      </bpmndi:BPMNPlane>
   </bpmndi:BPMNDiagram>
</bpmn:definitions>
```