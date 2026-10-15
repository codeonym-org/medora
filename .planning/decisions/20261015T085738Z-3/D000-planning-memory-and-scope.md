---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D000",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "User-directed session scope and durable planning records",
  "status": "confirmed",
  "round": 0,
  "created_at": "2026-10-15T08:57:38Z",
  "updated_at": "2026-10-15T08:57:38Z",
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
    "Agent instructions",
    "Planning memory",
    "Product discovery"
  ],
  "follow_ups": [],
  "sources": [
    "User message invoking grill-me in the current conversation"
  ]
}
---

# Context — why ask this?

The user initiated product discovery and explicitly requested durable reasoning records to prevent decisions and unrelated discoveries from being lost in chat or PRs. This is a direct instruction, not a question asked by the assistant.

## Predecessor decisions

None. The existing product vision supplies the product context.

## Question

Not applicable: the user supplied the instruction before the first interview round.

## Recommendation and alternatives

The assistant proposes versioned Markdown templates, one session index and one file per decision, plus separate follow-up records. Field names, UTC formatting, statuses, and file organization are implementation choices for the requested schema; they are editable and were not separately dictated by the user.

## User reply — original words

Source: current conversation, user message invoking `$grill-me`; no message timestamp or URL was provided.

> $grill-me lets do some digging about the project functionalities, ideas etc ... (no technical stack for now) also, id like you for each grilling session we create from now on, store the decisions under .planning/decisions/<DATETIME-ISSUE-ID>/ each decision shall cover the context (why it was asked?) the predecessor decisions, the question, the user reply, the intepretation, extra notes .... save this into your instructions! same apply for follow-ups, occutionally, we will some follow ups that are unrelated to current task at hand, instead of adding it only to PR or somewhere where its hard to remember, we log it into .planning/follow-ups/<DATETIME-title> it shall has good context like: why, when, where, analysis, affected components, kind: feat / bug / ... etc .... (draft a complete schema)

## Interpretation

Record future Medora grilling sessions in the requested session folders, including exact exchanges and dependency context. Record unrelated follow-ups independently with enough context to act later. Persist the rules in repository agent instructions. Explore product functionality now; defer technical stack selection.

## Decision and rationale

The logging requirement and current scope are confirmed by the direct user instruction. The user wants discoverable context beyond PR descriptions. The schema is a concrete draft implementing that request; individual product questions remain unanswered. Null answer/confirmation timestamps indicate that the original message time was not available; created_at records when this evidence was saved.

## Consequences and affected components

AGENTS.md points future sessions to the planning lifecycle and templates. Every interview round must preserve replies before continuing. Incidental ideas remain discoverable without silently expanding the active task.

## Assumptions, evidence, and open questions

Persistence is repository-scoped. Global agent settings are not modified. The final product design has not been confirmed.

## Extra notes and follow-ups

No unrelated follow-up has been identified yet. No application work is authorized by merely recording an idea.

## History

- 2026-10-15T08:57:38Z — Assistant recorded the explicit user instruction and distinguished it from proposed schema details.
