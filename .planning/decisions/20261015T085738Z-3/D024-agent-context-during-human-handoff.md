---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D024",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Agent awareness during handoff",
  "status": "confirmed",
  "round": 8,
  "created_at": "2026-10-15T14:38:24Z",
  "updated_at": "2026-10-15T14:45:47Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D007-basic-patient-profile.md",
    ".planning/decisions/20261015T085738Z-3/D021-staff-takeover-of-patient-chat.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Agent context",
    "Human conversation ownership",
    "Authorized record updates"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D007-basic-patient-profile.md",
    ".planning/decisions/20261015T085738Z-3/D021-staff-takeover-of-patient-chat.md",
    ".planning/decisions/20261015T085738Z-3/whatsapp-group-feasibility.md"
  ],
  "reply_recorded_at": "2026-10-15T14:45:47Z"
}
---

# Context — why ask this?

The user proposed tagging the agent to update its awareness. Reading conversation context, replying, and changing authoritative records are distinct behaviors; tagging feasibility is not yet verified.

## Predecessor decisions

[D007](D007-basic-patient-profile.md); [D021](D021-staff-takeover-of-patient-chat.md). Their accepted outcomes are prerequisites; no other round 8 outcome is assumed. Where groups are relevant, see [the feasibility note](whatsapp-group-feasibility.md).

## Question

Q31 — Agent awareness during handoff: While humans are talking, should Medora silently retain context from the authorized conversation and respond only when invoked, or process only the messages explicitly directed to it?

## Recommendation and alternatives

Retain the authorized conversation context silently, and reply only when explicitly invoked or handed control back. A tag alone should not authorize schedule changes or turn unverified chat statements into confirmed clinical facts.

The current decision records the user reply below. Earlier recommendations are not automatically accepted where the user supplied a different configuration.

## User reply — original words

Round 8 reply, recorded 2026-10-15T14:45:47Z; original message timestamp unavailable:

> q31: yeah

## Interpretation

The user accepts silently retaining authorized conversation context during human handling and replying when invoked or handed control back. Context updates alone do not authorize schedule mutations or make clinical statements verified facts.

## Decision and rationale

Confirmed: agent maintains permitted context silently while humans own the conversation; agent replies only on explicit invocation or control return. Actions still require established authorization, validation and confirmation.

## Consequences and affected components

Confirmed: agent maintains permitted context silently while humans own the conversation; agent replies only on explicit invocation or control return. Actions still require established authorization, validation and confirmation. The native mention mechanism remains unverified. Exact invocation UX, return-to-agent behavior and record-update confirmation are still implementation/product details to define. Only authorized conversation content is in scope.

## Assumptions, evidence, and open questions

The native mention mechanism remains unverified. Exact invocation UX, return-to-agent behavior and record-update confirmation are still implementation/product details to define. Only authorized conversation content is in scope.

## Extra notes and follow-ups

The linked-line follow-up holds remaining WhatsApp integration verification. These product questions stay in the active session.

## History

- 2026-10-15T14:38:24Z — Prepared the round 8 question after preserving the round 7 reply and checking relevant official documentation.

- 2026-10-15T14:45:47Z — Saved round 8 reply and confirmed its explicit scope. Prior interpretation: Pending. Prior decision: Pending.
