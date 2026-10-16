---
{
  "schema_version": 1,
  "id": "20261015T163800Z-5/D000",
  "session": ".planning/decisions/20261015T163800Z-5/session.md",
  "title": "Domain-modeling scope and established vocabulary",
  "status": "confirmed",
  "round": 0,
  "created_at": "2026-10-15T16:38:00Z",
  "updated_at": "2026-10-15T16:38:00Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/5",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D040-shared-understanding-confirmation.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Domain vocabulary",
    "Domain relationships"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/scope-review.md",
    "User message invoking mattpocock-skills:domain-modeling"
  ]
}
---

# Context — why ask this?

The user moved from the confirmed product foundation into explicit domain modeling. Existing decisions supply resolved terms; identity and lifecycle relationships still need sharpening.

## Predecessor decisions

[Confirmed product foundation](../20261015T085738Z-3/scope-review.md) and its final confirmation.

## Question

Not applicable: the user explicitly requested domain-modeling work.

## Recommendation and alternatives

Create a root glossary for resolved definitions and a separate domain-model document for relationships/scenarios. No ADR is justified merely by starting a glossary.

## User reply — original words

Source: current conversation; original message timestamp unavailable.

> $mattpocock-skills:domain-modeling lets model the domain, okey?

## Interpretation

Actively model the domain using the named skill, checking the confirmed foundation and recording terminology as it crystallizes. Keep the work stack-neutral, consistent with the preceding discussion.

## Decision and rationale

Domain-modeling work is authorized. The initial glossary captures already-confirmed concepts; this instruction does not resolve the new scenario questions.

## Consequences and affected components

Use GLOSSARY.md for definitions only, docs/domain-model.md for relationship analysis, and this session for the original exchanges.

## Assumptions, evidence, and open questions

There is no application code to compare against the concepts. No technology or storage design is selected.

## Extra notes and follow-ups

The previous discovery session remains confirmed and unchanged; this is a new session linked to issue #5.

## History

- 2026-10-15T16:38:00Z — Recorded the user invocation and initialized the modeling context.
