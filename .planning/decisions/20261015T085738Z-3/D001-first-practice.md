---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D001",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "First practice",
  "status": "confirmed",
  "round": 1,
  "created_at": "2026-10-15T08:57:38Z",
  "updated_at": "2026-10-15T15:44:38Z",
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
  "reply_recorded_at": "2026-10-15T12:13:49Z",
  "rounds": [
    1,
    2,
    3
  ],
  "amended_by": [
    ".planning/decisions/20261015T085738Z-3/D034-practice-configuration-ownership.md"
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

### Round 3 clarification — Q9 — Long-term practice model

Shall we use a practice/clinic organization as the home for one or more doctors and receptionists, with optional locations and people able to work across practices under separate permissions?

## Recommendation and alternatives

Start with one practitioner, with or without a receptionist, and name one primary daily operator. Expand to shared clinic coordination after that workflow is understood.

This is an assistant recommendation, not a user decision. Alternatives remain open until the user replies.

Round 2 recommendation: Use a practice as the working group: one or more doctors, with receptionists assigned to the doctors they support. Treat a solo practice as the one-doctor case.

No reply to the round 2 clarification has been received.

Round 3 recommendation: Yes. This supports solo doctors and growing clinics without making patient records automatically visible across independent practices.

No reply to round 3 has been received.

## User reply — original words

Recorded 2026-10-15T10:28:02Z. Source: current conversation; original message timestamps were not supplied.

> q1. its a doctor(s) and receptionist(s) (its three roles: Doctor, Receptionist, Patient)

Round 2 reply, recorded 2026-10-15T11:08:19Z; original message timestamp unavailable:

> Q5: think about far future, what will be the most natural choice here

Round 3 reply, recorded 2026-10-15T12:13:49Z; original message timestamp unavailable:

> q9: ok

## Interpretation

The user accepts the previously described practice/clinic organization model. It supports one or more doctors/receptionists, optional locations, and separate memberships for people working across practices. Access remains practice-scoped; this is not permission to expose records across practices.

## Decision and rationale

Confirmed: practice/clinic organization as the long-term operating model, with the solo practice as the smallest case. Multiple-location delivery timing and granular staff permissions remain to be decided.

Current role-set amendment: [D034](D034-practice-configuration-ownership.md) adds the user-requested explicit practice Owner/Admin account. Doctor, Receptionist and Patient remain the operational roles; the earlier three-role-only framing is no longer the complete role model. The accepted practice/clinic grouping remains valid.

## Consequences and affected components

Practice membership and role-aware staff workflows can now be explored. A person may work across practices without automatic cross-practice data access. Locations are supported by the long-term model; the first-release location depth remains open.

## Assumptions, evidence, and open questions

Practice ownership/configuration capabilities, staff assignment scope, shared calendars, staff chat visibility, and first-increment location support remain open. The three user roles are retained; no additional administrator role has been introduced.

## Extra notes and follow-ups

Technical stack selection is outside this session. No follow-up captured for this unanswered question.

## History

- 2026-10-15T08:57:38Z — Assistant prepared the first-round question; user response is pending.

- 2026-10-15T10:28:02Z — Assistant saved the actual reply and its interpretation; status is needs-clarification. Original recommendations remain historical proposals.

- 2026-10-15T11:08:19Z — Recorded round 2 answer; status needs-clarification.
  - Previous interpretation: The user explicitly establishes three roles: Doctor, Receptionist, Patient, and includes doctors and receptionists rather than accepting a doctor-only starting point. The plural forms allow multiple people; they do not establish whether staff share one practice, serve assigned doctors, or operate independently. A single primary daily operator was not selected.
  - Previous decision summary: Confirmed portion: the product has Doctor, Receptionist, and Patient roles. Practice grouping and how receptionists support doctors remain open; the assistant's single-practitioner recommendation was not accepted as a constraint. The user did not supply a further rationale; none is attributed to them.

- 2026-10-15T12:13:49Z — Saved round 3 reply; status confirmed.
  - Prior interpretation: The user requests a long-term product recommendation instead of choosing a practice grouping. The three roles remain confirmed; the assistant must not report its recommended organization model as user-approved.
  - Prior decision summary: The assistant recommends a practice/clinic organization with one or more locations, doctors, and receptionists. A person can work with multiple practices through separate memberships; record access stays scoped to the practice. A solo practice is the smallest instance. Exact location depth and cross-practice sharing are not first-release commitments.

- 2026-10-15T15:44:38Z — Linked the partial role-set amendment from Q42; preserved original replies and the organization decision.
