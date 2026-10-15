---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D025",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Whose language preference?",
  "status": "confirmed",
  "round": 8,
  "created_at": "2026-10-15T14:38:24Z",
  "updated_at": "2026-10-15T14:45:47Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D016-booking-for-someone-else.md",
    ".planning/decisions/20261015T085738Z-3/D020-patient-conversation-languages.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Language preferences",
    "Communication contacts",
    "Patient profiles"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D016-booking-for-someone-else.md",
    ".planning/decisions/20261015T085738Z-3/D020-patient-conversation-languages.md"
  ],
  "reply_recorded_at": "2026-10-15T14:45:47Z"
}
---

# Context — why ask this?

Contacts can book for other patients and language preference is remembered. The preference owner must be explicit to avoid changing a represented patient's preferences based on another person's messages.

## Predecessor decisions

[D016](D016-booking-for-someone-else.md); [D020](D020-patient-conversation-languages.md). Their accepted outcomes are prerequisites; no other round 8 outcome is assumed. Where groups are relevant, see [the feasibility note](whatsapp-group-feasibility.md).

## Question

Q32 — Whose language preference?: Should the remembered chat language belong to the person/contact speaking, so a parent chatting in French does not automatically overwrite a child's patient-profile language?

## Recommendation and alternatives

Yes. Keep staff-account and communication-contact preferences separate from the patient being booked, and honor explicit language-change requests.

The current decision records the user reply below. Earlier recommendations are not automatically accepted where the user supplied a different configuration.

## User reply — original words

Round 8 reply, recorded 2026-10-15T14:45:47Z; original message timestamp unavailable:

> q32: yeah

## Interpretation

The user accepts remembering language for the person/contact speaking, separately from a represented patient. Staff-account preferences and external communication-contact preferences are distinct; explicit changes are honored.

## Decision and rationale

Confirmed: remembered chat language belongs to the speaking user/contact, not automatically to the patient they are booking for. A parent's language does not overwrite a child's patient-profile language.

## Consequences and affected components

Confirmed: remembered chat language belongs to the speaking user/contact, not automatically to the patient they are booking for. A parent's language does not overwrite a child's patient-profile language. Handling a phone/line shared by multiple speakers, mixed-language messages and identity changes remains open; the accepted distinction does not solve identifying each physical speaker.

## Assumptions, evidence, and open questions

Handling a phone/line shared by multiple speakers, mixed-language messages and identity changes remains open; the accepted distinction does not solve identifying each physical speaker.

## Extra notes and follow-ups

The linked-line follow-up holds remaining WhatsApp integration verification. These product questions stay in the active session.

## History

- 2026-10-15T14:38:24Z — Prepared the round 8 question after preserving the round 7 reply and checking relevant official documentation.

- 2026-10-15T14:45:47Z — Saved round 8 reply and confirmed its explicit scope. Prior interpretation: Pending. Prior decision: Pending.
