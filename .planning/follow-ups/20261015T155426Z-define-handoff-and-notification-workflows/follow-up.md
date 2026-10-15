---
{
  "schema_version": 1,
  "id": "FU-20261015T155426Z-define-handoff-and-notification-workflows",
  "title": "Define handoff, group and notification workflows",
  "kind": "question",
  "status": "captured",
  "created_at": "2026-10-15T15:54:26Z",
  "updated_at": "2026-10-15T15:54:26Z",
  "observed_at": null,
  "reported_by": "assistant; deferral explicitly accepted by user in Q47",
  "owner": null,
  "priority": null,
  "severity": null,
  "origin": {
    "session": ".planning/decisions/20261015T085738Z-3/session.md",
    "decision": ".planning/decisions/20261015T085738Z-3/D039-focused-design-followups.md",
    "issue_url": "https://github.com/codeonym-org/medora/issues/3",
    "pr_url": "https://github.com/codeonym-org/medora/pull/4",
    "conversation_reference": "Round 12: q47: ok; preceding Q47 proposed focused details",
    "file_or_component": "Communication and handoff",
    "revision": null
  },
  "affected_components": [
    "Staff handoff",
    "Optional groups",
    "Agent invocation",
    "Delivery failures"
  ],
  "related_decisions": [
    ".planning/decisions/20261015T085738Z-3/D021-staff-takeover-of-patient-chat.md",
    ".planning/decisions/20261015T085738Z-3/D022-optional-patient-group-handoff.md",
    ".planning/decisions/20261015T085738Z-3/D023-handoff-staff-assignment.md",
    ".planning/decisions/20261015T085738Z-3/D024-agent-context-during-human-handoff.md",
    ".planning/decisions/20261015T085738Z-3/D028-notification-failure-after-confirmation.md",
    ".planning/decisions/20261015T085738Z-3/D036-default-staff-unavailable.md",
    ".planning/decisions/20261015T085738Z-3/D038-optional-group-release-timing.md",
    ".planning/decisions/20261015T085738Z-3/D039-focused-design-followups.md"
  ],
  "dependencies": [
    ".planning/decisions/20261015T085738Z-3/scope-review.md"
  ],
  "related_follow_ups": [
    ".planning/follow-ups/20261015T142428Z-validate-whatsapp-linked-line-onboarding/follow-up.md"
  ],
  "duplicate_of": null,
  "tracking_issue": null,
  "revisit": {
    "trigger": "Before implementing or enabling the corresponding handoff, group or delivery-failure flows",
    "due_at": null
  },
  "resolution": {
    "resolved_at": null,
    "outcome": null,
    "evidence": []
  }
}
---

# Summary

Define handoff, group and notification workflows. Preserve the accepted high-level behavior while resolving the remaining detailed choices in a focused session.

## Why — motivation and impact

The broad product interview settled the capability and workflow direction, but the details below are not yet decided. The user explicitly accepted Q47 deferral so these choices remain discoverable and block affected implementation/use rather than becoming silent assumptions.

## When and where — discovery context

Captured 2026-10-15T15:54:26Z from the product discovery session linked above. The original user-message timestamp is unavailable. The active task was consolidating the product foundation; the detailed branch is deferred with user agreement.

## Original observation or request

Q47 asked to capture focused policy/access/communication/profile/beta details before affected implementation/use. The actual user reply was:

> q47: ok

The analysis and suggested next steps below are assistant-authored; the user has not selected their detailed outcomes.

## Analysis

Specify group invitation/join/lifecycle, patient/contact membership, human/agent control transfer, invocation meaning, default/backup staff availability and reassignment, notification retry bounds, unresolved delivery escalation and observable patient statuses. Distinguish routine administrative handoff from the established urgent-review safety workflow.

## Affected components and boundaries

Staff handoff, Optional groups, Agent invocation, Delivery failures. The relevant accepted decisions are linked in metadata. A captured item neither changes their confirmed outcomes nor authorizes implementing extra scope.

## Reproduction or motivating example

Not a bug report. Use the corresponding confirmed patient/staff journey and synthetic examples to expose missing rules, including exception/failure paths, before choosing the detail.

## Options and proposed next action

Open a focused design/grilling session, read the related decisions, collect necessary facts, compare the unresolved options and record explicit choices with acceptance examples. Assign an owner and priority when scheduling this work.

## Dependencies and revisit trigger

Before implementing or enabling the corresponding handoff, group or delivery-failure flows. Related decisions and existing follow-ups are linked above; no due date, owner or numeric policy is invented.

## Acceptance and verification

A state/ownership description covers normal operation, waiting, reassignment, return to agent, invite refusal/failure and delivery failure. Group use remains optional and conditional on the separate official-capability verification; invocation never independently authorizes record changes.

## Resolution

Pending. The deferral is accepted; the detailed choices and implementation are not complete.

## Extra notes and history

- 2026-10-15T15:54:26Z — Created from the user-approved Q47 deferral; no external outreach, integration changes or application implementation occurred.
