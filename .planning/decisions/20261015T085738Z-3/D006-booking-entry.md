---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D006",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "First booking experience",
  "status": "needs-clarification",
  "round": 3,
  "created_at": "2026-10-15T11:08:19Z",
  "updated_at": "2026-10-15T12:13:49Z",
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
  "reply_recorded_at": "2026-10-15T12:13:49Z",
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

No reply to round 4 has been received.

## User reply — original words



Round 3 reply, recorded 2026-10-15T12:13:49Z; original message timestamp unavailable:

> q10: yes both, patient will likely use channels such as whatsapp and other messaging apps to book an appointment , staff on the otherside uses the chat interface ( a private realm to mgmt)

## Interpretation

Both patients and staff can initiate appointment management. The intended patient experience uses messaging channels, with WhatsApp specifically named as likely; staff use a private management chat. This does not confirm a standalone booking-page requirement, a mandatory first-release WhatsApp integration, a list of other apps, shared staff transcripts, or telephone support.

## Decision and rationale

Confirmed portions: patient and staff entry paths; private staff management chat; patient messaging is the intended direction, with WhatsApp a likely channel. Initial channel commitments and whether booking is completed inside messaging remain open.

## Consequences and affected components

Treat the staff chat as a distinct management experience. Clarify first patient channel and booking completion within messaging, then identity, handoff, confirmation, and conversation language behavior. Staff chat privacy requires its own decision.

## Assumptions, evidence, and open questions

WhatsApp is likely, not yet a first-release obligation. Other messaging apps are unnamed. A private staff realm does not specify whether colleagues share transcripts. A booking-page fallback and telephone automation are not confirmed.

## Extra notes and follow-ups

No follow-up captured for this unanswered in-scope question.

## History

- 2026-10-15T11:08:19Z — Assistant prepared this question after the initial-capability decision was confirmed.

- 2026-10-15T12:13:49Z — Saved round 3 reply; status needs-clarification.
  - Prior interpretation: Pending.
  - Prior decision summary: Pending.
