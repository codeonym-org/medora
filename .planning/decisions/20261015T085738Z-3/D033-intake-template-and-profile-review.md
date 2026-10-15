---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D033",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Who controls intake?",
  "status": "confirmed",
  "round": 10,
  "created_at": "2026-10-15T14:52:33Z",
  "updated_at": "2026-10-15T15:38:29Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D007-basic-patient-profile.md",
    ".planning/decisions/20261015T085738Z-3/D017-optional-conversational-intake.md",
    ".planning/decisions/20261015T085738Z-3/D027-approved-practice-information.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Intake templates",
    "Profile preparation",
    "Information provenance",
    "Staff correction"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D007-basic-patient-profile.md",
    ".planning/decisions/20261015T085738Z-3/D017-optional-conversational-intake.md",
    ".planning/decisions/20261015T085738Z-3/D027-approved-practice-information.md",
    "docs/product-vision.md"
  ],
  "reply_recorded_at": "2026-10-15T15:38:29Z"
}
---

# Context — why ask this?

Basic profiles and optional conversational intake are accepted. The first increment needs an explicit practice ownership and review workflow for the information it collects and presents.

## Predecessor decisions

[D007](D007-basic-patient-profile.md); [D017](D017-optional-conversational-intake.md); [D027](D027-approved-practice-information.md). Accepted outcomes supply the prerequisites; no answer to another round 10 question is assumed.

## Question

Q40 — Who controls intake?: Should doctors choose or approve the short intake questions for their appointment types, with Medora organizing the answers into a source-labelled profile and allowing authorized staff to correct it?

## Recommendation and alternatives

Yes. Use doctor-approved questions; keep patient statements, staff corrections and AI summaries distinguishable. Show unanswered questions and contradictions rather than filling gaps.

The current decision below distinguishes the accepted reply from tentative/unresolved details; earlier recommendation wording is historical.

## User reply — original words

Round 10 reply, recorded 2026-10-15T15:38:29Z; original message timestamp unavailable:

> q40: ok

## Interpretation

The user accepts doctors choosing/approving short intake questions by appointment type, organizing replies into source-labelled profiles, and authorized staff corrections while preserving provenance.

## Decision and rationale

Confirmed: doctor-owned/approved intake templates, source-labelled patient information, authorized correction, and explicit missing/contradictory information. Staff corrections and AI summaries remain distinguishable from the original patient statements.

## Consequences and affected components

Confirmed: doctor-owned/approved intake templates, source-labelled patient information, authorized correction, and explicit missing/contradictory information. Staff corrections and AI summaries remain distinguishable from the original patient statements. Exact template fields, versioning, correction permissions, review presentation and initial questionnaire limits remain implementation/product details. No clinician-authored diagnosis or prescription feature is added.

## Assumptions, evidence, and open questions

Exact template fields, versioning, correction permissions, review presentation and initial questionnaire limits remain implementation/product details. No clinician-authored diagnosis or prescription feature is added.

## Extra notes and follow-ups

The complete vision stays registered. No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:52:33Z — Prepared the round 10 question from accepted prerequisites.

- 2026-10-15T15:38:29Z — Saved round 10 reply; status confirmed. Prior interpretation: Pending. Prior decision: Pending.
