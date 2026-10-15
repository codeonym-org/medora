---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D032",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Changes and cancellations in beta",
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
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md",
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md",
    ".planning/decisions/20261015T085738Z-3/D013-replacement-slot-agreement.md",
    ".planning/decisions/20261015T085738Z-3/D029-first-contact-existing-record-access.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "WhatsApp appointment management",
    "Cancellation",
    "Rescheduling",
    "Beta scope"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md",
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md",
    ".planning/decisions/20261015T085738Z-3/D013-replacement-slot-agreement.md",
    ".planning/decisions/20261015T085738Z-3/D029-first-contact-existing-record-access.md",
    "docs/product-vision.md"
  ],
  "reply_recorded_at": "2026-10-15T15:38:29Z"
}
---

# Context — why ask this?

The initial increment is basic booking and profiling. The user accepted cancellation when a staff-proposed replacement does not fit, but ordinary patient-initiated cancellation/rescheduling release scope is not yet explicit.

## Predecessor decisions

[D002](D002-anchor-problem.md); [D006](D006-booking-entry.md); [D013](D013-replacement-slot-agreement.md); [D029](D029-first-contact-existing-record-access.md). Accepted outcomes supply the prerequisites; no answer to another round 10 question is assumed.

## Question

Q39 — Changes and cancellations in beta: Should the first beta let patients request cancellations and rescheduling through the same WhatsApp conversation, or should it initially handle new bookings while staff handle later changes?

## Recommendation and alternatives

Include basic cancellation and rescheduling requests in the initial booking workflow. Keep the accepted identity, staff-review and patient-agreement rules; defer advanced schedule optimization and waiting lists.

The current decision below distinguishes the accepted reply from tentative/unresolved details; earlier recommendation wording is historical.

## User reply — original words

Round 10 reply, recorded 2026-10-15T15:38:29Z; original message timestamp unavailable:

> q39: ok

## Interpretation

The user accepts basic cancellation and rescheduling requests through the same WhatsApp conversation in the initial beta, preserving the accepted verification, staff-review and replacement-agreement rules. Advanced optimization and waiting-list behavior remain later work.

## Decision and rationale

Confirmed: initial beta includes basic booking, cancellation/rescheduling requests and profiling. Exact cancellation execution/approval and ordinary practice-policy handling still require clarification.

## Consequences and affected components

Confirmed: initial beta includes basic booking, cancellation/rescheduling requests and profiling. Exact cancellation execution/approval and ordinary practice-policy handling still require clarification. Whether a verified cancellation is immediate or staff-approved, how an existing appointment is kept during a rescheduling request, and policy exception handling remain open. No fee, notice period, wait-list automation or auto-rescheduling is inferred.

## Assumptions, evidence, and open questions

Whether a verified cancellation is immediate or staff-approved, how an existing appointment is kept during a rescheduling request, and policy exception handling remain open. No fee, notice period, wait-list automation or auto-rescheduling is inferred.

## Extra notes and follow-ups

The complete vision stays registered. No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:52:33Z — Prepared the round 10 question from accepted prerequisites.

- 2026-10-15T15:38:29Z — Saved round 10 reply; status confirmed. Prior interpretation: Pending. Prior decision: Pending.
