# Medora — Product Vision

**Your practice, thoughtfully organized.**

Medora is an AI-powered medical secretary that helps doctors manage daily practice, coordinate appointments, highlight requests needing attention, and prepare structured patient context before consultations. Its purpose is to reduce administrative work and help doctors spend more time caring for patients.

The brand is professional, intelligent, calm, proactive, discreet, and human. The intended market is international, with multilingual product support. Medora should feel like a reliable medical office assistant. Product behavior follows the safety, privacy, and execution boundaries in [AGENTS.md](../AGENTS.md).

## Current discovery decisions

These confirmed choices refine the original roadmap. The [active product session](../.planning/decisions/20261015T085738Z-3/session.md) preserves their questions, user replies, rationale, and unresolved details.

- **Patient communication:** Medora connects to a practice-linked line; initially WhatsApp only. A personally used or shared number is a product requirement; supported onboarding modes still need technical evaluation. Patients book and ask appointment questions naturally in chat.
- **Routing and identity:** A line can represent one doctor or a group. Keep the communication contact separate from the patient, support booking for another person, and reuse verified returning contact-patient details. Staff verify uncertain relationships before existing-record access or changes.
- **Language:** Reply in the speaker's language and remember the speaker/contact preference until changed. This is distinct from patient-profile language and the initial UI locales.
- **Booking approval:** Reserve provisionally and exclusively, then obtain authorized doctor/receptionist review. Notify the patient of actual confirmation, rejection, or scheduling changes; never call a reservation confirmed.
- **Reservation expiry:** Count the configured review budget during staffed hours and cap it at a pre-appointment cutoff. Expire at the earlier limit, release the slot, and notify the patient. Exact durations remain practice configuration.
- **Replacement times:** Obtain patient agreement to a different time. The patient may decline and cancel when the replacement does not fit their schedule.
- **Profiles and intake:** Begin with administrative identity/contact details, appointment history, patient-reported visit reasons, and short appointment-specific intake. Gather minimum booking data first; optional intake follows without blocking confirmation merely because nonessential answers are missing.
- **Staff conversation:** Private management conversations may share selected read-only messages with named authorized same-practice colleagues, respecting patient-record permissions.
- **Human handoff:** Route to a default staff member configured in Medora. Patient groups are optional for eligible consenting participants, with one-to-one fallback. During human handling, retain authorized context silently and reply on invocation/control return; invocation alone does not authorize record changes. Native tag behavior and group lifecycle remain unresolved.
- **Schedule and practice information:** Staff maintain real availability in Medora initially; external calendar sync comes later. Answer approved practical information such as hours, address, fees and preparation, escalating missing information to staff.
- **Delivery failures:** Keep a successfully confirmed appointment even if notification delivery fails; surface the failure to staff and retry under policy. Do not claim the patient was informed without evidence.

## Users and control

- **Doctors** manage availability, appointments, practice policies, review queues, and patient preparation. They retain authority over clinical decisions and required approvals.
- **Patients** request, reschedule, and cancel appointments; communicate preferences and visit reasons; complete relevant intake; and receive confirmed next steps and approved instructions.
- **Authorized clinic staff**, when supported, coordinate care administration on behalf of doctors within role-specific permissions.

## Core capabilities

### Scheduling and calendar

Understand natural-language appointment requests, identify the practitioner and appointment type, collect preferences, and offer actual eligible slots. Support creation, rescheduling, cancellation, and explicit appointment status.

Provide day, week, and month calendar views, variable consultation durations, working hours, breaks, holidays, leave, blocked time, buffers, notice periods, and cancellation policies. Detect conflicts and offer alternatives. Support waiting lists and proposed schedule improvements as the roadmap progresses.

### Request prioritization

Configurable criteria may include patient-reported concerns, requests for urgent review, doctor-defined follow-up deadlines, recent procedures, time-sensitive administrative needs, and explicit doctor instructions.

| Level | Intended workflow |
| --- | --- |
| Routine | Follow ordinary scheduling rules. |
| Priority | Surface the need for earlier review or an earlier eligible appointment. |
| Urgent review | Route promptly to human clinical review or an established escalation workflow. |
| Emergency warning signs | Deliver configured emergency guidance immediately under the approved protocol. |

Each flag exposes its reason, contributing patient statements or configured rules, arrival time, review status, and outstanding action. An AI severity score alone is insufficient to determine urgency, and sparse symptom reporting does not establish safety.

### Intake, profiles, and briefings

Use short, relevant, practice-approved questionnaires covering the reason for a visit, patient-reported concerns and duration, changes over time, new concern versus follow-up, previous professional review, relevant conditions or medications, and optional additional context.

Profiles organize necessary identity and contact information, communication preferences, appointment history, upcoming visit context, intake answers, missing information, scheduling preferences, and explained priority flags. Preserve provenance and timestamps as specified in the agent guidance.

Pre-consultation briefings present the appointment time and type, patient identity, reported reason for the visit, relevant intake, missing information, administrative history, and review status. Preparation prompts may point to reported concerns and authorized existing records. Briefings are administrative summaries; any clinical suggestions require appropriate constraints, sources, and qualified review.

### Conversational assistant

Doctors and authorized staff can query schedules, find eligible slots, identify unconfirmed appointments or missing intake, summarize upcoming patients, review flagged requests, block time, and request daily briefings. Translate requests into structured, permission-checked operations with required clarification and confirmation.

### Notifications and configuration

Support confirmations, reminders, pending-confirmation requests, cancellations, schedule changes, intake prompts, review alerts, and daily or weekly summaries. Make notifications configurable to limit fatigue and follow patient preferences and applicable consent requirements.

Practice settings cover working hours, appointment durations, unavailable periods, booking notice, cancellation and rescheduling policies, new-patient rules, communication templates, intake questionnaires, priority and escalation protocols, reminders, languages, and automation approvals.

## Essential workflows

1. **Patient booking:** converse through WhatsApp; identify practitioner and appointment type; resolve missing date and timezone details; retrieve availability; offer suitable slots; obtain the patient's selection and minimum required information; create a provisional reservation and communicate its pending status; route it to staff; communicate confirmation, rejection, or scheduling changes only after the relevant operation succeeds; collect configured intake conversationally. Apply the confirmed exclusive-hold, expiry, staff-approval, and replacement-time agreement rules; exact deadline behavior and notification failures remain under discussion.
2. **Potentially urgent concern:** gather only appropriate limited clarification; apply the approved escalation protocol; provide emergency guidance without routine scheduling delays when triggered; route clinical review requests to a human; record review status and communicate confirmed next steps.
3. **Doctor's morning:** retrieve the authorized schedule; summarize appointments, pending reviews, incomplete intake, cancellations, conflicts, and changes; provide upcoming patient briefings and actionable administrative tasks.
4. **Cancellation:** identify the appointment; verify identity and authorization through the practice's approved process; explain applicable policy; obtain required confirmation; cancel; communicate success; assess eligible waiting-list candidates for the released slot; update records.
5. **Doctor schedule change:** interpret the affected interval and appointments; inspect conflicts; propose an impact-aware change plan; obtain required approval; execute authorized changes; communicate confirmed changes; report failures and incomplete work.

## Interface direction

Use a calm, precise, trustworthy SaaS interface with a light background, restrained navy, blue, teal, white, and neutral gray, clear typography, and useful spacing. Support desktop, tablet, and mobile with accessible contrast and readable status labels.

Suggested navigation:

- **Overview:** today's schedule, upcoming appointments, attention queue, daily briefing, quick actions.
- **Calendar:** day/week/month views, availability, blocked time, appointment details, conflicts.
- **Patients:** authorized profiles, history, intake, administrative notes.
- **Requests:** booking, rescheduling, cancellation, review, and escalation queues.
- **AI Assistant:** schedule queries, authorized actions, briefings, administrative coordination.
- **Settings:** profiles, hours, policies, templates, notifications, languages, permissions, integrations.

## Architecture direction

Maintain conceptual boundaries for authentication and authorization; doctor and clinic management; patient records and consent; appointments; availability; prioritization and escalation; intake and profile generation; AI orchestration; notifications; audit logging; reporting and monitoring; and external integration adapters. These boundaries do not prescribe separate services or a technology stack.

The AI interprets intent, collects required details, retrieves authorized data, invokes validated application tools, verifies results, and communicates outcomes. Persistence and connected systems supply authoritative state. External calendars and healthcare records require explicit integration boundaries and documented operational limitations.

## Incremental delivery

### Phase 1 — Reliable medical secretary MVP

Doctor authentication and profile; calendar and availability management; appointment creation, rescheduling, and cancellation; natural-language scheduling assistance; intake questionnaires; basic patient profiles; confirmations; a doctor dashboard and daily overview; explicit permission and confirmation flows.

Build the dependable scheduling foundation first. Basic conflict prevention belongs in this foundation even though broader conflict resolution tooling comes later.

### Phase 2 — Intelligent coordination

Configurable prioritization; human review queues and escalation; structured pre-consultation summaries; reminders; waiting-list management; conflict detection and suggested resolutions; configurable doctor preferences and automation.

### Phase 3 — Advanced practice assistant

Deeper calendar integrations; multilingual conversations; multi-doctor and multi-clinic management; advanced workflow automation; analytics and workload insights; authorized electronic health record integrations; clinically governed triage support where appropriate.

## Evaluation

Measure administrative time per appointment, request processing time, conflicts and duplicate bookings, missed confirmations, intake completeness, flagged-request review timeliness, consultation preparation time, patient satisfaction, doctor adoption and satisfaction, booking and notification reliability, and privacy/security/safety incidents. Establish baselines and targets using actual usage data.

## Initialization state

At initialization, the workspace contained no application source, dependency manifests, build or test configuration, or readable Git metadata. No framework, database, AI provider, communication channel, deployment target, or target-market regulatory scope has been selected. This document describes intended behavior, not implemented functionality. Reinspect the repository before choosing the first implementation slice.
