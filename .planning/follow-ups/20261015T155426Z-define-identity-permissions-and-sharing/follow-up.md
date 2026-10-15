---
{
  "schema_version": 1,
  "id": "FU-20261015T155426Z-define-identity-permissions-and-sharing",
  "title": "Define identity, permissions and sharing access rules",
  "kind": "question",
  "status": "in-progress",
  "created_at": "2026-10-15T15:54:26Z",
  "updated_at": "2026-10-15T16:38:00Z",
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
    "file_or_component": "Identity and permissions",
    "revision": null
  },
  "affected_components": [
    "Verification",
    "Patient access",
    "Practice roles",
    "Staff sharing"
  ],
  "related_decisions": [
    ".planning/decisions/20261015T085738Z-3/D001-first-practice.md",
    ".planning/decisions/20261015T085738Z-3/D012-conversation-sharing-scope.md",
    ".planning/decisions/20261015T085738Z-3/D016-booking-for-someone-else.md",
    ".planning/decisions/20261015T085738Z-3/D019-contact-with-multiple-patient-profiles.md",
    ".planning/decisions/20261015T085738Z-3/D029-first-contact-existing-record-access.md",
    ".planning/decisions/20261015T085738Z-3/D034-practice-configuration-ownership.md",
    ".planning/decisions/20261015T085738Z-3/D039-focused-design-followups.md"
  ],
  "dependencies": [
    ".planning/decisions/20261015T085738Z-3/scope-review.md"
  ],
  "related_follow_ups": [
    ".planning/follow-ups/20261015T121349Z-choose-beta-operating-countries/follow-up.md"
  ],
  "duplicate_of": null,
  "tracking_issue": "https://github.com/codeonym-org/medora/issues/5",
  "revisit": {
    "trigger": "Before enabling affected record access, membership administration, sharing or booking changes",
    "due_at": null
  },
  "resolution": {
    "resolved_at": null,
    "outcome": null,
    "evidence": []
  },
  "active_work": {
    "session": ".planning/decisions/20261015T163800Z-5/session.md",
    "scope": "Domain terminology and relationships only; remaining detailed policy/access scope stays open"
  }
}
---

# Summary

Define identity, permissions and sharing access rules. Preserve the accepted high-level behavior while resolving the remaining detailed choices in a focused session.

## Why — motivation and impact

The broad product interview settled the capability and workflow direction, but the details below are not yet decided. The user explicitly accepted Q47 deferral so these choices remain discoverable and block affected implementation/use rather than becoming silent assumptions.

## When and where — discovery context

Captured 2026-10-15T15:54:26Z from the product discovery session linked above. The original user-message timestamp is unavailable. The active task was consolidating the product foundation; the detailed branch is deferred with user agreement.

## Original observation or request

Q47 asked to capture focused policy/access/communication/profile/beta details before affected implementation/use. The actual user reply was:

> q47: ok

The analysis and suggested next steps below are assistant-authored; the user has not selected their detailed outcomes.

## Analysis

Resolve identity evidence, representative/caregiver access, verification lifecycle, role combinations, Owner/Admin versus clinical access, tenant boundaries, sharing revocation and audit behavior. Carry the original privacy/consent/retention and correction/export/deletion requirements into the related design before real patient use.

## Affected components and boundaries

Verification, Patient access, Practice roles, Staff sharing. The relevant accepted decisions are linked in metadata. A captured item neither changes their confirmed outcomes nor authorizes implementing extra scope.

## Reproduction or motivating example

Not a bug report. Use the corresponding confirmed patient/staff journey and synthetic examples to expose missing rules, including exception/failure paths, before choosing the detail.

## Options and proposed next action

Open a focused design/grilling session, read the related decisions, collect necessary facts, compare the unresolved options and record explicit choices with acceptance examples. Assign an owner and priority when scheduling this work.

## Dependencies and revisit trigger

Before enabling affected record access, membership administration, sharing or booking changes. Related decisions and existing follow-ups are linked above; no due date, owner or numeric policy is invented.

## Acceptance and verification

An explicit permission/verification matrix defines allowed and denied cases, uncertainty escalation and access changes. Sharing/revocation and representative cases have observable acceptance criteria; market-dependent privacy requirements link to beta geography work.

## Resolution

Pending. The deferral is accepted; the detailed choices and implementation are not complete.

## Extra notes and history

- 2026-10-15T15:54:26Z — Created from the user-approved Q47 deferral; no external outreach, integration changes or application implementation occurred.

- 2026-10-15T16:38:00Z — Domain-modeling portion started in issue #5 and session 20261015T163800Z-5. Status is in-progress; this does not claim all detailed policies or permissions are being resolved.
