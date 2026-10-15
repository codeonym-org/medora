---
{
  "schema_version": 1,
  "id": "FU-20261015T155426Z-define-beta-validation-and-release-gates",
  "title": "Define beta validation and public-release criteria",
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
    "file_or_component": "Beta acceptance",
    "revision": null
  },
  "affected_components": [
    "Beta scope",
    "Workflow validation",
    "Feedback",
    "Release readiness"
  ],
  "related_decisions": [
    ".planning/decisions/20261015T085738Z-3/D002-anchor-problem.md",
    ".planning/decisions/20261015T085738Z-3/D005-release-readiness.md",
    ".planning/decisions/20261015T085738Z-3/D030-staff-daily-workspace.md",
    ".planning/decisions/20261015T085738Z-3/D031-practice-setup-before-activation.md",
    ".planning/decisions/20261015T085738Z-3/D038-optional-group-release-timing.md",
    ".planning/decisions/20261015T085738Z-3/D039-focused-design-followups.md"
  ],
  "dependencies": [
    ".planning/decisions/20261015T085738Z-3/scope-review.md"
  ],
  "related_follow_ups": [
    ".planning/follow-ups/20261015T121349Z-choose-beta-operating-countries/follow-up.md"
  ],
  "duplicate_of": null,
  "tracking_issue": null,
  "revisit": {
    "trigger": "Before inviting real beta practices or claiming readiness for broader advertising",
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

Define beta validation and public-release criteria. Preserve the accepted high-level behavior while resolving the remaining detailed choices in a focused session.

## Why — motivation and impact

The broad product interview settled the capability and workflow direction, but the details below are not yet decided. The user explicitly accepted Q47 deferral so these choices remain discoverable and block affected implementation/use rather than becoming silent assumptions.

## When and where — discovery context

Captured 2026-10-15T15:54:26Z from the product discovery session linked above. The original user-message timestamp is unavailable. The active task was consolidating the product foundation; the detailed branch is deferred with user agreement.

## Original observation or request

Q47 asked to capture focused policy/access/communication/profile/beta details before affected implementation/use. The actual user reply was:

> q47: ok

The analysis and suggested next steps below are assistant-authored; the user has not selected their detailed outcomes.

## Analysis

Define observable workflow/reliability gates, developer validation with synthetic data, recruitment and onboarding, feedback collection and decisions for broader availability. This is separate from the optional per-practice guided test: do not turn it into a mandatory onboarding step. Country selection and applicable deployment/privacy/safety requirements must be resolved before live patient use.

## Affected components and boundaries

Beta scope, Workflow validation, Feedback, Release readiness. The relevant accepted decisions are linked in metadata. A captured item neither changes their confirmed outcomes nor authorizes implementing extra scope.

## Reproduction or motivating example

Not a bug report. Use the corresponding confirmed patient/staff journey and synthetic examples to expose missing rules, including exception/failure paths, before choosing the detail.

## Options and proposed next action

Open a focused design/grilling session, read the related decisions, collect necessary facts, compare the unresolved options and record explicit choices with acceptance examples. Assign an owner and priority when scheduling this work.

## Dependencies and revisit trigger

Before inviting real beta practices or claiming readiness for broader advertising. Related decisions and existing follow-ups are linked above; no due date, owner or numeric policy is invented.

## Acceptance and verification

Record beta acceptance criteria, evidence owners and feedback/exit process. Validate the accepted actors and appointment lifecycle, source-labelled profiles, access boundaries, honest notification states and human handoff. Numerical targets come from evidence or explicit decisions rather than invented baselines.

## Resolution

Pending. The deferral is accepted; the detailed choices and implementation are not complete.

## Extra notes and history

- 2026-10-15T15:54:26Z — Created from the user-approved Q47 deferral; no external outreach, integration changes or application implementation occurred.
