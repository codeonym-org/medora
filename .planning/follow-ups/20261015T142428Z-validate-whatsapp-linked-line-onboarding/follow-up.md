---
{
  "schema_version": 1,
  "id": "FU-20261015T142428Z-validate-whatsapp-linked-line-onboarding",
  "title": "Validate WhatsApp linked-line onboarding for personal/shared numbers",
  "kind": "research",
  "status": "captured",
  "created_at": "2026-10-15T14:24:28Z",
  "updated_at": "2026-10-15T14:24:28Z",
  "observed_at": null,
  "reported_by": "user",
  "owner": null,
  "priority": null,
  "severity": null,
  "origin": {
    "session": ".planning/decisions/20261015T085738Z-3/session.md",
    "decision": ".planning/decisions/20261015T085738Z-3/D015-practice-and-doctor-routing.md",
    "issue_url": "https://github.com/codeonym-org/medora/issues/3",
    "pr_url": "https://github.com/codeonym-org/medora/pull/4",
    "conversation_reference": "Round 6 Q22 linked-line requirement",
    "file_or_component": "Practice WhatsApp connection",
    "revision": null
  },
  "affected_components": [
    "Practice onboarding",
    "Linked WhatsApp lines",
    "Agent/human communication"
  ],
  "related_decisions": [
    ".planning/decisions/20261015T085738Z-3/D015-practice-and-doctor-routing.md"
  ],
  "dependencies": [
    "Product linked-line scope",
    "Later integration planning"
  ],
  "related_follow_ups": [],
  "duplicate_of": null,
  "tracking_issue": null,
  "revisit": {
    "trigger": "When WhatsApp integration and onboarding are technically evaluated, before promising supported connection modes",
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

Research the supported onboarding paths for a practice connecting a personally used or shared WhatsApp number to Medora. The product requirement is recorded; integration compatibility is not yet verified.

## Why — motivation and impact

The user defines Medora as a platform attached to external communication lines. The later connection flow must make this possible through supported WhatsApp capabilities without promising unverified personal-account or existing-number behavior.

## When and where — discovery context

Recorded 2026-10-15T14:24:28Z during product discovery, Q22 in [D015](../../decisions/20261015T085738Z-3/D015-practice-and-doctor-routing.md). Original message timestamp unknown. Integration research is outside the current no-stack product session.

## Original observation or request

> q22: medora is a platform, it requires its users (practice) to link a client facing communication app (currently only whatsapp will be used) so, the whatsapp app will need a linked line (like whatsapp busniess etc ...) so it can be either one of their personal phone numbers, or a shared one, the idea is that modera attaches to a line for edge communication

## Analysis

A personal/shared phone number is a product ownership/use category, not a confirmed WhatsApp account/API compatibility mode. No provider, account migration path, manual-coexistence behavior, credentials, or implementation has been selected or verified. Consult current official WhatsApp documentation when this work begins.

## Affected components and boundaries

Practice line connection, account/number eligibility, disconnect/reconnect, onboarding instructions and human/agent ownership. Doctor routing is a separate product question.

## Reproduction or motivating example

A practice wants to connect an existing doctor-used number or shared reception number. Determine which supported onboarding path applies. This is a research scenario, not evidence of a working integration.

## Options and proposed next action

Research official capabilities against the accepted requirements; document supported/unsupported modes, any user-visible setup steps, coexistence constraints and failure states. Present any product tradeoff instead of silently replacing the conversational journey.

## Dependencies and revisit trigger

Revisit during technical WhatsApp integration planning and before claiming compatibility to practices. No deadline or owner assigned.

## Acceptance and verification

Cited official findings identify supported account/number connection modes and operational limitations. A testable onboarding plan and documented product tradeoffs link back here before resolution.

## Resolution

Pending. No external app/account connection or patient-data transfer is authorized by this record.

## Extra notes and history

- 2026-10-15T14:24:28Z — Captured future integration research without selecting a stack or asserting compatibility.
