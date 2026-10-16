---
{
  "schema_version": 1,
  "id": "20261015T163800Z-5/D002",
  "session": ".planning/decisions/20261015T163800Z-5/session.md",
  "title": "A shared patient-side number",
  "status": "confirmed",
  "round": 1,
  "created_at": "2026-10-15T16:38:00Z",
  "updated_at": "2026-10-16T10:18:23Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/5",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D016-booking-for-someone-else.md",
    ".planning/decisions/20261015T085738Z-3/D019-contact-with-multiple-patient-profiles.md",
    ".planning/decisions/20261015T085738Z-3/D025-remembered-language-preference-owner.md",
    ".planning/decisions/20261015T085738Z-3/D029-first-contact-existing-record-access.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Communication Contact",
    "Patient",
    "Patient Profile",
    "Contact Point"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D016-booking-for-someone-else.md",
    ".planning/decisions/20261015T085738Z-3/D019-contact-with-multiple-patient-profiles.md",
    ".planning/decisions/20261015T085738Z-3/D025-remembered-language-preference-owner.md",
    ".planning/decisions/20261015T085738Z-3/D029-first-contact-existing-record-access.md",
    "GLOSSARY.md",
    "docs/domain-model.md"
  ],
  "reply_recorded_at": "2026-10-16T10:18:23Z",
  "reply_reference": "Joint user reply: ok, next; in response to the three first-round recommendations"
}
---

# Context — why ask this?

Patient and Communication Contact are already distinct. The remaining ambiguity is whether an external sender address identifies a unique person; this affects matching, remembered language and representative verification.

## Predecessor decisions

- [D016-booking-for-someone-else](../20261015T085738Z-3/D016-booking-for-someone-else.md)
- [D019-contact-with-multiple-patient-profiles](../20261015T085738Z-3/D019-contact-with-multiple-patient-profiles.md)
- [D025-remembered-language-preference-owner](../20261015T085738Z-3/D025-remembered-language-preference-owner.md)
- [D029-first-contact-existing-record-access](../20261015T085738Z-3/D029-first-contact-existing-record-access.md)

These established requirements are inputs; no outcome of another first-round modeling question is assumed.

## Question

Two parents use the same WhatsApp number to arrange appointments for their child. Should Medora allow separate Communication Contacts to share that contact address, rather than assuming the number identifies one person?

## Recommendation and alternatives

Yes. Model a contact address separately from the person. If the actual speaker is unclear, ask or leave identity unverified; never infer representative authority or a person-specific preference solely from the shared number.

This was the recommendation presented before the joint reply; the acceptance and its limited interpretation are recorded below.

## User reply — original words

Joint reply to the first three modeling recommendations, recorded 2026-10-16T10:18:23Z; original message timestamp unavailable:

> ok, next

## Interpretation

Read as acceptance of the three recommendations just presented and a request to continue. This is a joint acknowledgment, not three separately worded answers. For this decision: Separate Communication Contacts may share a Contact Point. A shared address alone establishes neither the speaker, representative authority nor a person-specific preference; ask or leave identity unverified when uncertain.

No additional policy values, verification method or implementation choices are inferred.

## Decision and rationale

Confirmed within this scenario: Separate Communication Contacts may share a Contact Point. A shared address alone establishes neither the speaker, representative authority nor a person-specific preference; ask or leave identity unverified when uncertain.

The user supplied no separate rationale. The recommendation and its reasoning above are assistant-authored.

## Consequences and affected components

Communication Contact, Patient, Patient Profile. The reply will sharpen terminology and relationships in the glossary/model.

## Assumptions, evidence, and open questions

The joint reply confirms the relationship described above. No database schema, account implementation, global person-matching scheme or automatic verification method is selected. Detailed permissions and independent request-closure policies remain open. No application code exists to cross-check.

## Extra notes and follow-ups

The booking-policy and identity/permissions follow-ups remain open; vocabulary work does not resolve their full scope.

## History

- 2026-10-15T16:38:00Z — Prepared this scenario from the confirmed foundation; user response pending.

- 2026-10-16T10:18:23Z — Saved the joint reply verbatim and recorded its acceptance of the existing recommendation; no additional commitments inferred.
