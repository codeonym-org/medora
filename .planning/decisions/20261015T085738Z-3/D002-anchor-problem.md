---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D002",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Main problem",
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
    "Appointment coordination",
    "Product scope"
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

The vision lists many benefits but does not identify the primary reason a practice would adopt Medora.

## Predecessor decisions

Root product question; no predecessor product decision is required. The supplied product vision and session scope remain constraints.

## Question

Which problem must Medora solve first to make someone change their current habits: interruptions from appointment requests, rescheduling back-and-forth, missed appointments, or missing patient information? Choose one; give a concrete example if you have one.

### Round 2 clarification — Q6 — Meaning of “all”

Does “all” mean the first public version must cover booking, rescheduling, reminders, and basic patient intake together? Or are these all product goals that can arrive in successive releases?

## Recommendation and alternatives

Make routine appointment coordination the first promise: turn a request into a confirmed appointment with minimal staff effort. Use the other benefits to support that promise.

This is an assistant recommendation, not a user decision. Alternatives remain open until the user replies.

Round 2 recommendation: Launch with a basic end-to-end version of all four, while developing them incrementally. Leave advanced optimization and richer patient summaries for later.

No reply to the round 2 clarification has been received.

## User reply — original words

Recorded 2026-10-15T10:28:02Z. Source: current conversation; original message timestamps were not supplied.

> Q2: All

## Interpretation

All four named problems matter to the user: booking interruptions, rescheduling exchanges, missed appointments, and missing patient information. This does not establish equal priority, release depth, or that every advanced feature must ship in the first version.

## Decision and rationale

Confirmed portion: preserve all four benefits in the product scope. Release sequencing and the minimum depth of each remain unresolved. The user did not supply a further rationale; none is attributed to them.

## Consequences and affected components

Do not narrow the product to scheduling alone. Clarify whether the first public release needs basic coverage of each workflow, while preserving the existing incremental-development principle.

## Assumptions, evidence, and open questions

The assistant maps these problems to booking, rescheduling, reminders, and basic intake as a proposal to confirm in Q6. No concrete practitioner example or acceptance threshold was supplied. The user reply is the source; no practitioner evidence has been gathered.

## Extra notes and follow-ups

Technical stack selection is outside this session. No follow-up captured for this unanswered question.

## History

- 2026-10-15T08:57:38Z — Assistant prepared the first-round question; user response is pending.

- 2026-10-15T10:28:02Z — Assistant saved the actual reply and its interpretation; status is needs-clarification. Original recommendations remain historical proposals.
