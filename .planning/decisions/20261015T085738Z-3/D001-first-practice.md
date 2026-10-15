---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D001",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "First practice",
  "status": "needs-clarification",
  "round": 1,
  "created_at": "2026-10-15T08:57:38Z",
  "updated_at": "2026-10-15T10:28:02Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Doctor experience",
    "Staff workflows"
  ],
  "follow_ups": [],
  "sources": [
    "docs/product-vision.md",
    "Current conversation: first-round user answers; later user message completes Q4"
  ],
  "reply_recorded_at": "2026-10-15T10:28:02Z",
  "rounds": [
    1,
    2
  ]
}
---

# Context — why ask this?

The intended audience includes several operating models; the initial daily user and division of work are unsettled.

## Predecessor decisions

Root product question; no predecessor product decision is required. The supplied product vision and session scope remain constraints.

## Question

For the first version, are we serving a doctor working alone, a doctor with a receptionist, or a small multi-doctor clinic? Who would use Medora every day?

### Round 2 clarification — Q5 — Shared practice

Do doctors and receptionists belong to a shared practice, with receptionists managing several doctors, or does each doctor have a separate team? Should both arrangements be supported?

## Recommendation and alternatives

Start with one practitioner, with or without a receptionist, and name one primary daily operator. Expand to shared clinic coordination after that workflow is understood.

This is an assistant recommendation, not a user decision. Alternatives remain open until the user replies.

Round 2 recommendation: Use a practice as the working group: one or more doctors, with receptionists assigned to the doctors they support. Treat a solo practice as the one-doctor case.

No reply to the round 2 clarification has been received.

## User reply — original words

Recorded 2026-10-15T10:28:02Z. Source: current conversation; original message timestamps were not supplied.

> q1. its a doctor(s) and receptionist(s) (its three roles: Doctor, Receptionist, Patient)

## Interpretation

The user explicitly establishes three roles: Doctor, Receptionist, Patient, and includes doctors and receptionists rather than accepting a doctor-only starting point. The plural forms allow multiple people; they do not establish whether staff share one practice, serve assigned doctors, or operate independently. A single primary daily operator was not selected.

## Decision and rationale

Confirmed portion: the product has Doctor, Receptionist, and Patient roles. Practice grouping and how receptionists support doctors remain open; the assistant's single-practitioner recommendation was not accepted as a constraint. The user did not supply a further rationale; none is attributed to them.

## Consequences and affected components

Role-specific experiences are in scope. Shared schedules, staff assignments, and access boundaries require a product decision about practice grouping before deeper permission questions.

## Assumptions, evidence, and open questions

No practice size, specialty, team-assignment policy, or single primary operator is established. Q5 clarifies the operating model without adding a fourth role. The user reply is the source; no practitioner evidence has been gathered.

## Extra notes and follow-ups

Technical stack selection is outside this session. No follow-up captured for this unanswered question.

## History

- 2026-10-15T08:57:38Z — Assistant prepared the first-round question; user response is pending.

- 2026-10-15T10:28:02Z — Assistant saved the actual reply and its interpretation; status is needs-clarification. Original recommendations remain historical proposals.
