---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D007",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Meaning of profiling",
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
    "Patient profiles",
    "Intake",
    "Consultation preparation"
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

The round 4 reply is recorded below. Earlier recommendations are historical proposals; the current decision is authoritative.

## User reply — original words



Round 3 reply, recorded 2026-10-15T12:13:49Z; original message timestamp unavailable:

> q11: hmm, maybe ?

Round 4 reply, recorded 2026-10-15T13:46:49Z; original message timestamp unavailable:

> q15: ok

## Interpretation

The user accepts the concrete initial profile proposed in Q15: patient identity/contact details, appointment history, patient-reported visit reasons, and short intake attached to each appointment. Clinician-authored diagnoses, prescriptions, and full medical-record management remain later possibilities rather than initial features.

## Decision and rationale

Confirmed: start with an administrative patient profile and appointment-specific preliminary intake, retaining patient-reported attribution. Full clinical-record functionality is outside the initial increment.

## Consequences and affected components

The booking conversation can collect minimal identity/contact details and relevant intake, and prepare useful doctor context. Profile lifecycle, exact required fields, skip behavior, access, and conversation-to-profile review remain product questions.

## Assumptions, evidence, and open questions

Exact identity/contact fields, optional intake, matching returning patients, who may edit a profile, and patient visibility/correction workflows are not yet chosen. Acceptance of this profile is not approval of medical diagnosis or prescribing.

## Extra notes and follow-ups

Related questions are continuing within this product session. No unrelated follow-up was introduced by this reply.

## History

- 2026-10-15T11:08:19Z — Assistant prepared this question after the initial-capability decision was confirmed.

- 2026-10-15T12:13:49Z — Saved round 3 reply; status needs-clarification.
  - Prior interpretation: Pending.
  - Prior decision summary: Pending.

- 2026-10-15T13:46:49Z — Saved round 4 reply and confirmed the explicit choice.
  - Prior interpretation: The user is uncertain about the proposed profile boundary. No choice between administrative intake and a fuller clinical record has been made. The assistant must explain the proposed first-increment scope concretely and obtain a choice.
  - Prior decision summary: No profile-content decision is confirmed. Basic profiling remains part of the first increment, but its content and clinical-record boundary are unresolved.
