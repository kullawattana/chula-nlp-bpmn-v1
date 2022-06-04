from main_generate_bpmn_xml import BPMN
from neural_coref import NeuralCoref

#Scenario 1 (Exception Gateway)
#sentence = "The party sends a warrant possession request asking a warrant to be released. The Client Service Back Office as part of the Small Claims Registry Operations receives the request and retrieves the SCT file. Then, the SCT Warrant Possession is forwarded to Queensland Police. The SCT physical file is stored by the Back Office awaiting a report to be sent by the Police. When the report is received, the respective SCT file is retrieved. Then, Back Office attaches the new SCT document, and stores the expanded SCT physical file. After that, some other MC internal staff receives the physical SCT file (out of scope)."

#scenario 2 
#sentence = "Each morning, the files which have yet to be processed need to be checked, to make sure they are in order for the court hearing that day. If some files are missing, a search is initiated, otherwise the files can be physically tracked to the intended location. Once all the files are ready, these are handed to the Associate, and meantime the Judges Lawlist is distributed to the relevant people."
#Exception :: sentence = "Each morning, the files which have yet to be processed need to be checked, to make sure they are in order for the court hearing that day. If some files are missing, a search is initiated, otherwise the files can be physically tracked to the intended location. Once all the files are ready, these are handed to the Associate, and meantime the Judges Lawlist is distributed to the relevant people. [Afterwards, the directions hearings are conducted.]"

#scenario 3
#sentence = "After a claim is registered, it is examined by a claims officer. The claims officer then writes a “settlement recommendation”. This recommendation is then checked by a senior claims officer who may mark the claim as “OK” or “Not OK”."
#Exception :: sentence = "After a claim is registered, it is examined by a claims officer. The claims officer then writes a “settlement recommendation”. This recommendation is then checked by a senior claims officer who may mark the claim as “OK” or “Not OK”. [If the claim is marked as “Not OK”, it is sent back to the claims officer and the recommendation is repeated. If the claim is OK, the claim handling process proceeds.]"

#scenario 4
#sentence = "When a claim is received, it is first checked whether the claimant is insured by the organization. If not, the claimant is informed that the claim must be rejected. Otherwise, the severity of the claim is evaluated. Based on the outcome (simple or complex claims), relevant forms are sent to the claimant. Once the forms are returned, they are checked for completeness."
#Exception :: sentence = "When a claim is received, it is first checked whether the claimant is insured by the organization. If not, the claimant is informed that the claim must be rejected. Otherwise, the severity of the claim is evaluated. Based on the outcome (simple or complex claims), relevant forms are sent to the claimant. Once the forms are returned, they are checked for completeness. [If the forms provide all relevant details, the claim is registered in the Claims Management system, which ends the Claims Notification process. Otherwise, the claimant is informed to update the forms. Upon reception of the updated forms, they are checked again.]"

#scenario 5 (Exception Gateway)
#sentence = "The Police Report related to the car accident is searched within the Police Report database and put in a file together with the Claim Documentation. This file serves as input to a claims handler who calculates an initial claim estimate. Then, the claims handler creates an Action Plan based on an Action Plan Checklist available in the Document Management system. Based on the Action Plan, a claims manager tries to negotiate a settlement on the claim estimate. The claimant is informed of the outcome, which ends the process."

#scenario 6
#sentence = "The process starts when a customer submits a claim by sending in relevant documentation. The Notification department at the car insurer checks the documents upon completeness and registers the claim. Then, the Handling department picks up the claim and checks the insurance. Then, an assessment is performed. If the assessment is positive, a garage is phoned to authorize the repairs and the payment is scheduled (in this order). Otherwise, the claim is rejected. In any case (whether the outcome is positive or negative), a letter is sent to the customer and the process is considered to be complete."

#scenario 7
#sentence = "First, the Manager checks the open leads. Afterwards, he selects the top five ones. He then tells his Sales Assistant to call the contact person of the leads. The Sales Assistant calls each customer. If someone is interested, he sends a note to the Manager. The Manager then processes the lead. Otherwise, he calls the next customer."

#scenario 8 (is_show_gateway = False (Worked), is_show_gateway = True (not work))
#sentence = "The Vacation Request Process starts when an employee of the organization submits a vacation request. Once the requirement is registered, the request is received by the immediate supervisor; the supervisor must approve or reject the request. If the request is rejected the application is returned to the applicant/employee who can review the rejection reasons. If the request is approved a notification is generated to the Human Resources representative, who must complete the respective administrative procedures."

#scenario 9 
#sentence = "This process starts whenever a purchase order has been received from a customer. The first activity that is carried out is confirming the order. Next, the shipment address is received so that the product can be shipped to the customer. Afterwards, the invoice is emitted and once the payment is received the order is archived, thus completing the process."

#scenario 10
#sentence = "Once the boarding pass has been received, passengers proceed to the security check. Here they need to pass the personal security screening and the luggage screening. Afterwards, they can proceed to the departure level."

#scenario 11
#sentence = "As soon as an invoice is received from a customer, it needs to be checked for mismatches. The check may result in either of these three options: i) there are no mismatches, in which case the invoice is posted; ii) there are mismatches but these can be corrected, in which case the invoice is re-sent to the customer; and iii) there are mismatches but these cannot be corrected, in which case the invoice is blocked. Once one of these three activities is performed the invoice is parked and the process completes."

#scenario 12 (is_show_gateway = False (Worked), is_show_gateway = True (not work))
#sentence = "A loan application is approved if it passes two checks: (i) the applicant’s loan risk assessment, done automatically by a system, and (ii) the appraisal of the property for which the loan has been asked, carried out by a property appraiser. The risk assessment requires a credit history check on the applicant, which is performed by a financial officer. Once both the loan risk assessment and the property appraisal have been performed, a loan officer can assess the applicant’s eligibility. If the applicant is not eligible, the application is rejected, otherwise the acceptance pack is prepared and sent to the applicant."

#scenario 13 (Exception Critical on first sentence [By assuming that a purchase order is only confirmed if the product is in stock])
#sentence = "By assuming that a purchase order is only confirmed if the product is in stock, otherwise the process completes by rejecting the order. Further, if the order is confirmed, the shipment address is received and the requested product is shipped while the invoice is emitted and the payment is received. Afterwards, the order is archived and the process completes."

#scenario 14 (is_show_gateway = False (Worked), is_show_gateway = True (not work))
#sentence = "In the treasury minister’s office, once a ministerial inquiry has been received, it is first registered into the system. Then the inquiry is investigated so that a ministerial response can be prepared. The finalization of a response includes the preparation of the response itself by the cabinet officer and the review of the response by the principal registrar. If the registrar does not approve the response, the latter needs to be prepared again by the cabinet officer for review. The process finishes only once the response has been approved."

#Demo
sentence = "The Vacation Request Process starts when an employee of the organization submits a vacation request. Once the requirement is registered, the request is received by the immediate supervisor; the supervisor must approve or reject the request. If the request is rejected the application is returned to the applicant/employee who can review the rejection reasons. If the request is approved a notification is generated to the Human Resources representative, who must complete the respective administrative procedures."

neuralCoref = NeuralCoref(sentence)
text = neuralCoref.get_sentence()

if __name__ == "__main__":
    process_name = "BPMN Process"
    is_show_lane = True
    is_show_gateway = False
    bpmn = BPMN(text, process_name)
    bpmn.bpmn_process(is_show_lane, is_show_gateway)   