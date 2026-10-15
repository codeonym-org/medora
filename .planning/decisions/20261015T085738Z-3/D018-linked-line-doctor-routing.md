---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D018",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Routing a linked line",
  "status": "unanswered",
  "round": 7,
  "created_at": "2026-10-15T14:24:28Z",
  "updated_at": "2026-10-15T14:24:28Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D015-practice-and-doctor-routing.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Linked lines",
    "Doctor selection",
    "Practice onboarding"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D015-practice-and-doctor-routing.md"
  ]
}
---

# Context — why ask this?

A personal or shared connected line is confirmed, but the doctors it represents have not been defined. This is a product routing decision, independent of the eventual integration implementation.

## Predecessor decisions

[D001](D001-first-practice.md); [D015](D015-practice-and-doctor-routing.md). Only their accepted requirements are prerequisites; unresolved details and other round 7 answers are not assumed.

## Question

Q25 — Routing a linked line: Should each linked line be configurable for one doctor or a group of doctors, so Medora knows when to use a default doctor and when to ask the patient to choose?

## Recommendation and alternatives

Yes. A doctor-specific line defaults to that doctor; a shared practice line uses the patient's preference or asks who they want. Never silently substitute another doctor.

This recommendation remains unconfirmed.

## User reply — original words

Pending. Prepared for round 7.

## Interpretation

Pending.

## Decision and rationale

Pending.

## Consequences and affected components

Linked lines, Doctor selection, Practice onboarding. Details depend on the answer.

## Assumptions, evidence, and open questions

No routing default, representative authorization, patient conversation language, or human-takeover policy is assumed. Technical stack selection remains excluded.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:24:28Z — Prepared the round 7 question from accepted prerequisites.
