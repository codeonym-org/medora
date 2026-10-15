---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D007",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Meaning of profiling",
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
    "Patient profiles",
    "Intake",
    "Consultation preparation"
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

The user confirmed profiling as part of the initial increment. Its boundaries determine what information is collected and whether the product expands into clinical-record management.

## Predecessor decisions

[D002](D002-anchor-problem.md) confirms basic booking and profiling as the first increment. This question does not require an answer to the organization-model recommendation.

## Question

Q11 — Meaning of profiling: Does basic profiling mean contact details plus the reason for the visit and a short pre-appointment intake, or do you also expect a longitudinal clinical record with diagnoses, prescriptions, and documents?

### Round 4 clarification — Q15 — A concrete basic profile

For the first release, shall a profile contain identity/contact details, appointment history, and patient-reported visit reasons with short intake attached to each appointment, while clinician-authored diagnoses, prescriptions, and full medical-record management remain later possibilities?

## Recommendation and alternatives

Start with a persistent administrative patient profile and intake linked to each appointment. Keep patient-reported information clearly identified; defer full clinical-record functionality.

The alternatives in the question remain available. This is a recommendation, not an accepted scope decision.

Round 4 recommendation: Use that administrative profile plus appointment-specific intake as the starting scope. It gives the doctor preparation context without committing this increment to a complete clinical-record system.

No reply to round 4 has been received.

## User reply — original words



Round 3 reply, recorded 2026-10-15T12:13:49Z; original message timestamp unavailable:

> q11: hmm, maybe ?

## Interpretation

The user is uncertain about the proposed profile boundary. No choice between administrative intake and a fuller clinical record has been made. The assistant must explain the proposed first-increment scope concretely and obtain a choice.

## Decision and rationale

No profile-content decision is confirmed. Basic profiling remains part of the first increment, but its content and clinical-record boundary are unresolved.

## Consequences and affected components

Affected areas: Patient profiles, Intake, Consultation preparation. Detailed downstream decisions will depend on the reply.

## Assumptions, evidence, and open questions

The user has not accepted either profile scope. No clinical-record editing, document storage, or specific intake fields are confirmed. Present a concrete administrative profile with per-appointment intake for confirmation in Q15.

## Extra notes and follow-ups

No follow-up captured for this unanswered in-scope question.

## History

- 2026-10-15T11:08:19Z — Assistant prepared this question after the initial-capability decision was confirmed.

- 2026-10-15T12:13:49Z — Saved round 3 reply; status needs-clarification.
  - Prior interpretation: Pending.
  - Prior decision summary: Pending.
