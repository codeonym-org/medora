---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D006",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "First booking experience",
  "status": "confirmed",
  "round": 3,
  "created_at": "2026-10-15T11:08:19Z",
  "updated_at": "2026-10-15T13:46:49Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Appointment requests",
    "Receptionist scheduling",
    "Patient experience"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md",
    "docs/product-vision.md"
  ],
  "reply_recorded_at": "2026-10-15T13:46:49Z",
  "rounds": [
    3,
    4
  ]
}
---

# Context — why ask this?

The user confirmed basic booking as the starting capability, but the entry journey is unspecified. The channel affects identity, availability presentation, and required confirmations.

## Predecessor decisions

[D002](D002-anchor-problem.md) confirms basic booking and profiling as the first increment. This question does not require an answer to the organization-model recommendation.

## Question

Q10 — First booking experience: For the first version, should patients book directly through a practice link, should receptionists enter bookings, or do you need both? Are messaging and telephone assistants required immediately?

### Round 4 clarification — Q13 — Booking inside messaging

For the first release, must a patient complete the entire booking conversation inside WhatsApp, or is receiving a link to a booking page sufficient?

## Recommendation and alternatives

Start with patient self-booking through a practice link and receptionist-created bookings. Record messaging and telephone automation for later unless they are essential to your first users.

The alternatives in the question remain available. This is a recommendation, not an accepted scope decision.

Round 4 recommendation: Make WhatsApp the first complete patient conversation channel if messaging is central to Medora. Add other messaging apps gradually; keep a booking link as an optional fallback.

The round 4 reply is recorded below. Earlier recommendations are historical proposals; the current decision is authoritative.

## User reply — original words



Round 3 reply, recorded 2026-10-15T12:13:49Z; original message timestamp unavailable:

> q10: yes both, patient will likely use channels such as whatsapp and other messaging apps to book an appointment , staff on the otherside uses the chat interface ( a private realm to mgmt)

Round 4 reply, recorded 2026-10-15T13:46:49Z; original message timestamp unavailable:

> q13: idk how are you interpretting the project, but the overaall goal is to make booking an easy task for patients, why would they need a UI for such thing (there are already solutions like those!) they do regular chitchat with the agent and the whatsapp agent do the booking for them, and they can ask about there approintements and other staff throught the whatsapp, thets the core idea!

## Interpretation

The user corrects the assistant: the core patient experience is natural conversation with the WhatsApp agent, which performs booking and handles appointment questions directly in chat. Requiring a patient booking UI would defeat that intended experience. WhatsApp is a core initial product channel, not merely a speculative future integration. The phrase other staff is preserved verbatim and not interpreted as access to private staff conversations; additional patient questions remain to be bounded.

## Decision and rationale

Confirmed: patients converse naturally with the WhatsApp agent to book and ask about their appointments. No separate patient booking UI is required for this core journey. Staff retain a separate private management chat. The assistant's booking-page-first recommendation is not adopted.

## Consequences and affected components

Correct the agent guidance, product vision, and feature register to prevent drifting toward a patient booking form. Availability checks, provisional reservations, appointment inquiries, and outcome notifications must be achievable conversationally. Other messaging channels remain part of the broader vision; their sequence is unspecified.

## Assumptions, evidence, and open questions

The scope of additional patient questions, identity verification, supported conversational languages, doctor selection, cancellation/rescheduling details, and human handoff remain unresolved. This confirmation does not imply that a reservation is already a confirmed appointment.

## Extra notes and follow-ups

Related questions are continuing within this product session. No unrelated follow-up was introduced by this reply.

## History

- 2026-10-15T11:08:19Z — Assistant prepared this question after the initial-capability decision was confirmed.

- 2026-10-15T12:13:49Z — Saved round 3 reply; status needs-clarification.
  - Prior interpretation: Pending.
  - Prior decision summary: Pending.

- 2026-10-15T13:46:49Z — Saved round 4 reply and confirmed the explicit choice.
  - Prior interpretation: Both patients and staff can initiate appointment management. The intended patient experience uses messaging channels, with WhatsApp specifically named as likely; staff use a private management chat. This does not confirm a standalone booking-page requirement, a mandatory first-release WhatsApp integration, a list of other apps, shared staff transcripts, or telephone support.
  - Prior decision summary: Confirmed portions: patient and staff entry paths; private staff management chat; patient messaging is the intended direction, with WhatsApp a likely channel. Initial channel commitments and whether booking is completed inside messaging remain open.

- 2026-10-15T13:46:49Z — Assistant acknowledged misunderstanding the central patient experience and corrected the booking-page-first framing. No patient UI fallback is introduced as a requirement.
