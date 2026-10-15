---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D023",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Which staff joins?",
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
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D011-staff-approval-permissions.md",
    ".planning/decisions/20261015T085738Z-3/D021-staff-takeover-of-patient-chat.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Handoff assignment",
    "Staff visibility",
    "Practice workflow"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D011-staff-approval-permissions.md",
    ".planning/decisions/20261015T085738Z-3/D021-staff-takeover-of-patient-chat.md"
  ],
  "reply_recorded_at": "2026-10-15T14:45:47Z"
}
---

# Context — why ask this?

The user explicitly left one staff versus all staff undecided. This question applies to either groups or the existing patient conversation.

## Predecessor decisions

[D001](D001-first-practice.md); [D011](D011-staff-approval-permissions.md); [D021](D021-staff-takeover-of-patient-chat.md). Their accepted outcomes are prerequisites; no other round 8 outcome is assumed. Where groups are relevant, see [the feasibility note](whatsapp-group-feasibility.md).

## Question

Q30 — Which staff joins?: Should a handoff go to an assigned receptionist first, with the doctor involved when needed, rather than automatically exposing the conversation to all staff?

## Recommendation and alternatives

Use named responsible staff, with an authorized backup if unavailable. For optional groups, invite only the people needed for that patient/request.

The current decision records the user reply below. Earlier recommendations are not automatically accepted where the user supplied a different configuration.

## User reply — original words

Round 8 reply, recorded 2026-10-15T14:45:47Z; original message timestamp unavailable:

> q30: a default staff (configured on modera platform)

## Interpretation

The user selects a default staff member configured in Medora as the handoff recipient. They do not require that person to be a receptionist, add all staff by default, or settle automatic backup/escalation behavior.

## Decision and rationale

Confirmed: route handoffs to the default staff member configured on Medora, subject to the existing permissions and practice scope.

## Consequences and affected components

Confirmed: route handoffs to the default staff member configured on Medora, subject to the existing permissions and practice scope. Configuration scope (practice versus line/doctor), who may change the setting, unavailability handling and reassignment remain open. Do not invent a mandatory receptionist-first role or all-staff group.

## Assumptions, evidence, and open questions

Configuration scope (practice versus line/doctor), who may change the setting, unavailability handling and reassignment remain open. Do not invent a mandatory receptionist-first role or all-staff group.

## Extra notes and follow-ups

The linked-line follow-up holds remaining WhatsApp integration verification. These product questions stay in the active session.

## History

- 2026-10-15T14:38:24Z — Prepared the round 8 question after preserving the round 7 reply and checking relevant official documentation.

- 2026-10-15T14:45:47Z — Saved round 8 reply and confirmed its explicit scope. Prior interpretation: Pending. Prior decision: Pending.
