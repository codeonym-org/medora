---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D002",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Main problem",
  "status": "confirmed",
  "round": 1,
  "created_at": "2026-10-15T08:57:38Z",
  "updated_at": "2026-10-15T11:08:19Z",
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
  "reply_recorded_at": "2026-10-15T11:08:19Z",
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

Round 2 reply, recorded 2026-10-15T11:08:19Z; original message timestamp unavailable:

> Q6: ALl must be registred, but we gradually add neww features, we will start with the basic booking and profiling

## Interpretation

Keep the full feature vision recorded and deliver it incrementally. The starting increment is basic booking and patient profiling. The user did not require reminders, full rescheduling coordination, or every planned feature to ship together. The detailed meaning of basic profiling still needs clarification.

## Decision and rationale

Confirmed: preserve all features in the register, add features gradually, and begin with basic booking and profiling. This supersedes the assistant recommendation to launch all four workflows together; no rationale beyond the stated incremental approach is attributed to the user.

## Consequences and affected components

The initial feature boundary is confirmed at the capability level. A feature register preserves the wider vision without promising delivery dates. Booking entry, confirmation policy, profile content, and later-feature sequencing remain open.

## Assumptions, evidence, and open questions

Detailed booking entry points and profile fields remain open. No reminders/rescheduling delivery date is promised. The wider feature vision remains recorded in the product vision and feature register.

## Extra notes and follow-ups

The [feature register](../../feature-register.md) preserves all vision features and distinguishes the first increment from unsequenced work. No additional feature has been silently removed.

## History

- 2026-10-15T08:57:38Z — Assistant prepared the first-round question; user response is pending.

- 2026-10-15T10:28:02Z — Assistant saved the actual reply and its interpretation; status is needs-clarification. Original recommendations remain historical proposals.

- 2026-10-15T11:08:19Z — Recorded round 2 answer; status confirmed.
  - Previous interpretation: All four named problems matter to the user: booking interruptions, rescheduling exchanges, missed appointments, and missing patient information. This does not establish equal priority, release depth, or that every advanced feature must ship in the first version.
  - Previous decision summary: Confirmed portion: preserve all four benefits in the product scope. Release sequencing and the minimum depth of each remain unresolved. The user did not supply a further rationale; none is attributed to them.
