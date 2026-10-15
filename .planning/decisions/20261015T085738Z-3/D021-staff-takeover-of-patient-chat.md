---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D021",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Human takeover",
  "status": "confirmed",
  "round": 7,
  "created_at": "2026-10-15T14:24:28Z",
  "updated_at": "2026-10-15T14:38:24Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md",
    ".planning/decisions/20261015T085738Z-3/D011-staff-approval-permissions.md",
    ".planning/decisions/20261015T085738Z-3/D015-practice-and-doctor-routing.md"
  ],
  "related_decisions": [
    ".planning/decisions/20261015T085738Z-3/D022-optional-patient-group-handoff.md",
    ".planning/decisions/20261015T085738Z-3/D024-agent-context-during-human-handoff.md"
  ],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Human handoff",
    "Staff workspace",
    "Patient conversation ownership"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md",
    ".planning/decisions/20261015T085738Z-3/D011-staff-approval-permissions.md",
    ".planning/decisions/20261015T085738Z-3/D015-practice-and-doctor-routing.md"
  ],
  "reply_recorded_at": "2026-10-15T14:35:28Z"
}
---

# Context — why ask this?

Staff review and a platform connected to patient communication lines are confirmed. Ownership of the conversation during a human handoff needs an explicit product policy.

## Predecessor decisions

[D006](D006-booking-entry.md); [D011](D011-staff-approval-permissions.md); [D015](D015-practice-and-doctor-routing.md). Only their accepted requirements are prerequisites; unresolved details and other round 7 answers are not assumed.

## Question

Q28 — Human takeover: Should staff be able to take over a patient's WhatsApp conversation from Medora when the patient asks for a person or the agent cannot complete the request, pausing the agent until staff hand it back?

## Recommendation and alternatives

Yes. Give authorized staff a clear handoff with the relevant context, show the patient that a human response is pending, and avoid simultaneous human/agent replies.

The user reply and current decision are recorded below; earlier recommendation wording is historical and is not automatically accepted.

## User reply — original words

Round 7 reply, recorded 2026-10-15T14:35:28Z; original message timestamp unavailable:

> q28: yeah! and maybe in this case the agent creates a new unique group per patient and it adds a staff (or all idk) so they can communicate and the agent can be tagged to update its awareness instead of replying directly on the agent's default line right?

## Interpretation

Human takeover is accepted. The user tentatively proposes one distinct WhatsApp group per patient, adding staff so humans can communicate there and tagging the agent to update its awareness. The words maybe, or all idk, and right? leave the group mechanism, staff audience and agent behavior open. This is not confirmation of adding all staff or an assertion that any linked WhatsApp line supports group automation.

## Decision and rationale

Confirmed: authorized human staff can take over when needed. The user's per-patient group and tag-driven-awareness proposal remains unsettled and is tracked in D022/D024, not treated as a required or working integration.

## Consequences and affected components

Confirmed portion: human staff can take over when needed. Proposed, not settled: a per-patient group with selected staff and tag-driven agent participation/context updates. Group feasibility and product behavior are being checked before endorsing it. Official WhatsApp group/API feasibility is an unsettled prerequisite for choosing the initial handoff mechanism. Staff assignment, invitations/consent, group ownership and lifecycle, visibility of participant contact details, reading versus responding, and whether a tag can authorize actions remain open.

## Assumptions, evidence, and open questions

Official WhatsApp group/API feasibility is an unsettled prerequisite for choosing the initial handoff mechanism. Staff assignment, invitations/consent, group ownership and lifecycle, visibility of participant contact details, reading versus responding, and whether a tag can authorize actions remain open.

## Extra notes and follow-ups

[Official-source feasibility note](whatsapp-group-feasibility.md) documents current group constraints. The [linked-line onboarding follow-up](../../follow-ups/20261015T142428Z-validate-whatsapp-linked-line-onboarding/follow-up.md) now includes the remaining group/tag integration questions.

## History

- 2026-10-15T14:24:28Z — Prepared the round 7 question from accepted prerequisites.

- 2026-10-15T14:35:28Z — Saved round 7 reply; status needs-clarification. Prior interpretation: Pending. Prior decision: Pending.

- 2026-10-15T14:38:24Z — Classified the accepted takeover capability as confirmed and separated the tentative group mechanism into follow-on decisions; official-source feasibility findings recorded.
