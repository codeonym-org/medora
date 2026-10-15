---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D031",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Practice setup",
  "status": "needs-clarification",
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
    ".planning/decisions/20261015T085738Z-3/D015-practice-and-doctor-routing.md",
    ".planning/decisions/20261015T085738Z-3/D023-handoff-staff-assignment.md",
    ".planning/decisions/20261015T085738Z-3/D026-initial-availability-source.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Practice onboarding",
    "Booking configuration",
    "Activation readiness"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D015-practice-and-doctor-routing.md",
    ".planning/decisions/20261015T085738Z-3/D023-handoff-staff-assignment.md",
    ".planning/decisions/20261015T085738Z-3/D026-initial-availability-source.md",
    "docs/product-vision.md"
  ],
  "reply_recorded_at": "2026-10-15T15:38:29Z",
  "rounds": [
    10,
    11
  ]
}
---

# Context — why ask this?

Medora is now the initial schedule source and requires a linked communication line. The product needs a clear path from an empty practice to a working booking assistant.

## Predecessor decisions

[D015](D015-practice-and-doctor-routing.md); [D023](D023-handoff-staff-assignment.md); [D026](D026-initial-availability-source.md). Accepted outcomes supply the prerequisites; no answer to another round 10 question is assumed.

## Question

Q38 — Practice setup: Should a practice configure its doctors, availability, appointment durations, linked WhatsApp line and default staff member, then complete a test booking before activating patient-facing booking?

### Round 11 clarification — Q41 — Lighter setup

Would you prefer requiring only the essential booking configuration before activation, while making a test booking optional rather than a mandatory step?

## Recommendation and alternatives

Yes. Allow setup to be saved as a draft and clearly show what is missing before activation. Use synthetic information for the test booking.

The current decision below distinguishes the accepted reply from tentative/unresolved details; earlier recommendation wording is historical.

Round 11 recommendation: Yes: require a usable schedule, appointment durations, line routing and responsible staff; offer a guided test without forcing it. Let setup be saved and resumed.

No reply to Q41 has been received.

## User reply — original words

Round 10 reply, recorded 2026-10-15T15:38:29Z; original message timestamp unavailable:

> q38: hmm ok ?

## Interpretation

The user expresses tentative acceptance or uncertainty about setup before activation. Do not treat this as unambiguous approval of a mandatory test booking or a rigid setup wizard. Clarify a lighter required-configuration/optional-test approach.

## Decision and rationale

Tentative only: practice setup is being discussed. The mandatory activation checklist and test-booking gate are not confirmed. Q41 will clarify.

## Consequences and affected components

Tentative only: practice setup is being discussed. The mandatory activation checklist and test-booking gate are not confirmed. Q41 will clarify. A working schedule and linked line are existing prerequisites; the exact onboarding flow, minimum required settings, activation behavior and whether testing is compulsory remain open.

## Assumptions, evidence, and open questions

A working schedule and linked line are existing prerequisites; the exact onboarding flow, minimum required settings, activation behavior and whether testing is compulsory remain open.

## Extra notes and follow-ups

The complete vision stays registered. No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:52:33Z — Prepared the round 10 question from accepted prerequisites.

- 2026-10-15T15:38:29Z — Saved round 10 reply; status needs-clarification. Prior interpretation: Pending. Prior decision: Pending.
