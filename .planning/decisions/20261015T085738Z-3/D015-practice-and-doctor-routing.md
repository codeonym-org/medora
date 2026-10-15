---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D015",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Which practice are they messaging?",
  "status": "confirmed",
  "round": 6,
  "created_at": "2026-10-15T13:52:30Z",
  "updated_at": "2026-10-15T14:24:28Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Patient entry",
    "Practice identity",
    "Doctor selection"
  ],
  "follow_ups": [
    ".planning/follow-ups/20261015T142428Z-validate-whatsapp-linked-line-onboarding/follow-up.md"
  ],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md"
  ],
  "reply_recorded_at": "2026-10-15T14:24:28Z"
}
---

# Context — why ask this?

A WhatsApp-first product needs an explicit relationship between the conversation and the practice it represents. The organization model does not decide whether the patient starts with a practice-specific or shared contact.

## Predecessor decisions

[D001](D001-first-practice.md); [D006](D006-booking-entry.md). The confirmed outcomes establish this question's prerequisites. No answer to another round 6 question is assumed.

## Question

Q22 — Which practice are they messaging?: Should patients message the practice's own WhatsApp contact, with Medora acting as that practice's secretary, or a shared Medora contact that first finds their practice and doctor?

## Recommendation and alternatives

Start with the practice's own contact and identity. Within a multi-doctor practice, ask which doctor they want if that is not already clear.

The current decision below records the reply. For Q21 the user delegated the choice; the rationale is attributed to the assistant. Earlier framing is retained as history.

## User reply — original words

Round 6 reply, recorded 2026-10-15T14:24:28Z; original message timestamp unavailable:

> q22: medora is a platform, it requires its users (practice) to link a client facing communication app (currently only whatsapp will be used) so, the whatsapp app will need a linked line (like whatsapp busniess etc ...) so it can be either one of their personal phone numbers, or a shared one, the idea is that modera attaches to a line for edge communication

## Interpretation

Medora is the practice management platform. A practice links a client-facing communication app/line, currently WhatsApp only. The linked phone number may be personal to a practitioner or shared. Medora attaches to that line for external patient conversation; this is not a requirement for a single platform-wide Medora contact. Number ownership does not itself establish doctor routing or platform permissions.

## Decision and rationale

Confirmed: a linked communication-line model for patient communication, with WhatsApp as the only initial app and support for personally used or shared phone numbers as a product requirement. Staff use Medora privately; patients communicate over the linked external line.

## Consequences and affected components

Confirmed: a linked communication-line model for patient communication, with WhatsApp as the only initial app and support for personally used or shared phone numbers as a product requirement. Staff use Medora privately; patients communicate over the linked external line. How a line maps to practice/doctors, whether a practice may attach multiple lines, and coexistence with manual replies remain open product details. No particular WhatsApp account type, API, migration path, or personal-account integration compatibility is claimed; technical feasibility is a separate follow-up.

## Assumptions, evidence, and open questions

How a line maps to practice/doctors, whether a practice may attach multiple lines, and coexistence with manual replies remain open product details. No particular WhatsApp account type, API, migration path, or personal-account integration compatibility is claimed; technical feasibility is a separate follow-up.

## Extra notes and follow-ups

[Linked-line onboarding research](../../follow-ups/20261015T142428Z-validate-whatsapp-linked-line-onboarding/follow-up.md) preserves the later technical feasibility work.

## History

- 2026-10-15T13:52:30Z — Assistant prepared the round 6 question from confirmed prerequisites.

- 2026-10-15T14:24:28Z — Saved round 6 reply and current decision. Prior interpretation: Pending. Prior decision: Pending.
