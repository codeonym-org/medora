# Medora

The language of coordinating a practice, its patients, and its appointments. These terms describe the domain independently of the application stack.

## Practices and people

**Practice**:
The organization whose doctors, staff, schedules, and patient information are managed together in Medora. A solo practice and a clinic organization are both practices.
_Avoid_: Clinic when it could mean either the organization or one of its locations; tenant in product language.

**Practice Membership**:
A person's participation in a particular practice, with the roles and permissions granted there.
_Avoid_: Global role when describing authority in one practice.

**Practice Owner**:
The practice's designated administrative account holder, responsible for its administration, staff access, and connected communication lines. This responsibility alone does not establish clinical authority.
_Avoid_: Global administrator; Owner/Admin when the precise domain term is needed.

**Doctor**:
A clinician practicing within a practice who retains responsibility for clinical decisions and approval of clinical intake content.
_Avoid_: Provider when specifically referring to a doctor rather than an external service.

**Receptionist**:
A practice staff member authorized to coordinate administrative work such as appointment review and patient communication.
_Avoid_: Practice Owner when describing routine reception responsibilities.

**Patient**:
The person for whom care or a consultation is sought. The patient may be different from the person arranging the appointment.
_Avoid_: WhatsApp user; phone-number holder as a synonym for Patient.

**Communication Contact**:
The person communicating with the practice about an appointment or patient. A contact may communicate for themselves or for another patient.
_Avoid_: Patient when the speaker and recipient of care may differ; phone number as a synonym for the person.

**Patient Profile**:
A practice's organized administrative information about a patient, including appointment context and attributed patient-reported information.
_Avoid_: Full medical record; global patient account.

## Scheduling

**Appointment Request**:
A request to arrange a consultation, expressing the patient's needs and scheduling preferences.
_Avoid_: Confirmed appointment; Reservation when referring to the request itself.

**Reservation**:
A temporary, exclusive hold on a proposed appointment time while the required review or agreement is pending.
_Avoid_: Confirmed booking; Appointment as a synonym for an unconfirmed hold.

**Appointment**:
A scheduled consultation between a patient and a doctor. A confirmed appointment represents the practice-approved commitment to that consultation.
_Avoid_: Reservation when referring to a confirmed consultation.

**Booking**:
The process of arranging an appointment, from the request through the required review and confirmation.
_Avoid_: Booking as an unqualified synonym for either a temporary hold or a confirmed appointment.

**Rescheduling Request**:
A request to replace an existing appointment with an agreed appointment time.
_Avoid_: Cancellation when the intention is to retain an appointment at another time.

**Intake**:
Preliminary information collected for an appointment using practice-approved questions, with the origin of the answers identified.
_Avoid_: Diagnosis; clinician-verified findings when the information is patient-reported.

## Communication and coordination

**Communication Line**:
A practice-connected, externally reachable communication endpoint through which contacts converse with the practice, initially a WhatsApp line. The line may represent one doctor or a group of doctors.
_Avoid_: Communication Contact when referring to the endpoint; global Medora number as an assumed routing model.

**Patient Conversation**:
A conversation between the practice and a communication contact concerning a patient or appointment.
_Avoid_: Private Staff Conversation when referring to messages involving the contact.

**Staff Conversation**:
A private conversation between a staff user and Medora's assistant in the practice-management platform.
_Avoid_: Shared patient chat; practice-wide transcript as the default meaning.

**Handoff**:
A transfer of active responsibility for a patient conversation from the agent to authorized staff, initially the practice-configured default staff member.
_Avoid_: Patient group as a synonym for every Handoff.

**Appointment Notification**:
A communication about an appointment request, reservation, confirmed appointment, or subsequent change. Its delivery outcome is distinct from the appointment's outcome.
_Avoid_: Appointment confirmation when describing delivery alone.
