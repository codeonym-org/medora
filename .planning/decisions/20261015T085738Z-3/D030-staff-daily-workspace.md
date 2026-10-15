---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D030",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "The staff workspace",
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
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md",
    ".planning/decisions/20261015T085738Z-3/D026-initial-availability-source.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Staff interface",
    "Calendar",
    "Request review",
    "Patient profiles"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D007-basic-patient-profile.md",
    ".planning/decisions/20261015T085738Z-3/D009-routine-booking-authority.md",
    ".planning/decisions/20261015T085738Z-3/D026-initial-availability-source.md",
    "docs/product-vision.md"
  ],
  "reply_recorded_at": "2026-10-15T15:38:29Z"
}
---

# Context — why ask this?

The patient experience is fully conversational and staff use private management chat. The initial staff workspace still needs a decision about direct visual access to operational records.

## Predecessor decisions

[D007](D007-basic-patient-profile.md); [D009](D009-routine-booking-authority.md); [D026](D026-initial-availability-source.md). Accepted outcomes supply the prerequisites; no answer to another round 10 question is assumed.

## Question

Q37 — The staff workspace: Alongside private chat, should doctors and receptionists have a compact calendar, a queue of requests awaiting review, and patient profile cards, so they can inspect information without asking the agent every time?

## Recommendation and alternatives

Yes. Keep chat central, with direct views of the schedule, review queue and profiles. Permissions determine what each staff user can see and change.

The current decision below distinguishes the accepted reply from tentative/unresolved details; earlier recommendation wording is historical.

## User reply — original words

Round 10 reply, recorded 2026-10-15T15:38:29Z; original message timestamp unavailable:

> q37: yes, its a fully functional platform, enhanced with integrated AI agents

## Interpretation

The user explicitly confirms that Medora is a functional practice-management platform enhanced with integrated AI agents. Staff must have direct operational interfaces for calendars, review queues and patient profiles as well as private assistant conversations. The earlier recommendation to keep chat central does not justify reducing the platform to a chatbot. The patient booking journey remains WhatsApp conversational.

## Decision and rationale

Confirmed: a functional staff-facing platform plus integrated agents, including direct schedule, request-review and profile access according to permissions. Incremental delivery still applies; this is not authorization to implement the entire long-term roadmap at once.

## Consequences and affected components

Confirmed: a functional staff-facing platform plus integrated agents, including direct schedule, request-review and profile access according to permissions. Incremental delivery still applies; this is not authorization to implement the entire long-term roadmap at once. Detailed interaction design, navigation and which staff actions need additional confirmation remain to be designed. No separate patient booking UI is introduced by this clarification.

## Assumptions, evidence, and open questions

Detailed interaction design, navigation and which staff actions need additional confirmation remain to be designed. No separate patient booking UI is introduced by this clarification.

## Extra notes and follow-ups

The complete vision stays registered. No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:52:33Z — Prepared the round 10 question from accepted prerequisites.

- 2026-10-15T15:38:29Z — Saved round 10 reply; status confirmed. Prior interpretation: Pending. Prior decision: Pending.
