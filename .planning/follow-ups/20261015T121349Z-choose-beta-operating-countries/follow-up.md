---
{
  "schema_version": 1,
  "id": "FU-20261015T121349Z-choose-beta-operating-countries",
  "title": "Choose beta operating countries before recruitment and local policy decisions",
  "kind": "question",
  "status": "captured",
  "created_at": "2026-10-15T12:13:49Z",
  "updated_at": "2026-10-15T12:13:49Z",
  "observed_at": null,
  "reported_by": "user",
  "owner": null,
  "priority": null,
  "severity": null,
  "origin": {
    "session": ".planning/decisions/20261015T085738Z-3/session.md",
    "decision": ".planning/decisions/20261015T085738Z-3/D003-pilot-market.md",
    "issue_url": "https://github.com/codeonym-org/medora/issues/3",
    "pr_url": "https://github.com/codeonym-org/medora/pull/4",
    "conversation_reference": "Round 3 Q12 reply",
    "file_or_component": "Beta scope",
    "revision": null
  },
  "affected_components": [
    "Beta recruitment",
    "Practice onboarding",
    "Country-specific operating rules"
  ],
  "related_decisions": [
    ".planning/decisions/20261015T085738Z-3/D003-pilot-market.md"
  ],
  "dependencies": [],
  "related_follow_ups": [],
  "duplicate_of": null,
  "tracking_issue": null,
  "revisit": {
    "trigger": "Before setting beta recruitment eligibility or country-specific operating rules",
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

Choose the countries in which beta practices will operate. The user explicitly left this undecided during product discovery.

## Why — motivation and impact

A language list does not identify the operating market. Beta eligibility and country-specific operational requirements cannot be finalized from the four UI languages alone. No priority or severity is assigned.

## When and where — discovery context

Recorded 2026-10-15T12:13:49Z from round 3 Q12 in [D003](../../decisions/20261015T085738Z-3/D003-pilot-market.md). The original message timestamp is unknown. The user chose not to settle geography now, so preserve the question for beta planning without blocking general product exploration.

## Original observation or request

> q12: undecided

## Analysis

Confirmed UI languages: English, French, Arabic, Spanish. Country selection remains open; no country is inferred from those languages or the development timezone. No jurisdiction-specific legal or clinical conclusions have been researched or made.

## Affected components and boundaries

Beta eligibility, practice onboarding, and country-specific operating policies. General booking and profile design can continue with uncertainty explicitly recorded.

## Reproduction or motivating example

When deciding which practices may join beta, identify supported operating countries before applying market-specific rules. This is a planning question, not a bug.

## Options and proposed next action

Ask the user to select one or more beta markets when recruitment scope is defined. Then identify requirements needing evidence or qualified review. No recruitment or external outreach is authorized by this record.

## Dependencies and revisit trigger

Revisit before setting beta recruitment eligibility or country-specific operating rules. No date or assigned owner is known.

## Acceptance and verification

Record an explicit user decision on beta operating countries, link it from D003, and identify any newly unblocked product-policy questions. Do not close based solely on selecting interface languages.

## Resolution

Pending.

## Extra notes and history

- 2026-10-15T12:13:49Z — Assistant captured the explicitly undecided geography choice as a follow-up.
