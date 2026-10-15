---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3",
  "title": "Medora product functionality and initial scope",
  "status": "active",
  "created_at": "2026-10-15T08:57:38Z",
  "updated_at": "2026-10-15T12:13:49Z",
  "repository": "codeonym-org/medora",
  "issue_number": 3,
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "participants": [
    "user",
    "assistant"
  ],
  "facilitator": "assistant",
  "origin": {
    "conversation_url": null,
    "message_reference": "User message invoking grill-me and requesting durable planning schemas",
    "related_task": "Explore product functionality; persist planning instructions"
  },
  "predecessor_sessions": [],
  "supersedes": [],
  "superseded_by": [],
  "related_follow_ups": [
    ".planning/follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md",
    ".planning/follow-ups/20261015T110819Z-ai-generated-additional-ui-translations/follow-up.md",
    ".planning/follow-ups/20261015T121349Z-choose-beta-operating-countries/follow-up.md"
  ]
}
---

# Purpose and context

Sharpen Medora's first useful product experience through a recorded interview. The product vision is broad; first-user needs and initial operating assumptions remain unsettled.

## Scope and constraints

In scope: functionality, product ideas, target practices, patient/staff workflows, delegation boundaries, and validation. Out of scope: technical stack selection and application implementation. Existing administrative-role, clinical-safety, privacy, and truthful-confirmation constraints remain in effect.

The user explicitly requested persistent decision and follow-up logs; see [D000](D000-planning-memory-and-scope.md).

## Decision tree

- First practice and daily operator → roles, receptionist collaboration, onboarding, permissions.
- Anchor problem → primary journey, minimum useful scope, observable success.
- Pilot market and languages → communication needs and local operating assumptions.
- Access to practitioners → evidence collection and pilot validation.
- Once these roots are answered: contact channels, existing schedule practices, booking/rescheduling/cancellation rules, human handoff coverage, intake and briefing boundaries, and adoption.

These later branches are candidate questions, not assumed decisions; refine their prerequisites after round 1.

## Decision index and rounds

| ID / link | Round | Question | Predecessors | Status | Outcome |
| --- | --- | --- | --- | --- | --- |
| [D000](D000-planning-memory-and-scope.md) | 0 | Scope and durable records | None | confirmed | Preserve logs; no stack selection |
| [D001](D001-first-practice.md) | 1–3 | Roles and practice grouping | Root | confirmed | Practice organization, three roles, scoped memberships |
| [D002](D002-anchor-problem.md) | 1–2 | Product benefits and launch breadth | Root | confirmed | Preserve all features; basic booking and profiling first |
| [D003](D003-pilot-market.md) | 1–3 | Market and languages | Root | deferred | Four UI languages confirmed; geography deferred |
| [D004](D004-validation-access.md) | 1 | Practitioner access | Root | confirmed | No current access; advertise once working |
| [D005](D005-release-readiness.md) | 2 | Early-release approach | D004 | confirmed | Beta early access |
| [D006](D006-booking-entry.md) | 3–4 / Q13 | Patient/staff booking entry | D002 | needs-clarification | Patient messaging, private staff chat; exact channel scope open |
| [D007](D007-basic-patient-profile.md) | 3–4 / Q15 | Profile content | D002 | needs-clarification | User unsure; concrete scope proposed |
| [D008](D008-staff-chat-privacy.md) | 4 / Q14 | Staff chat visibility | D001, accepted staff-realm portion of D006 | unanswered | Pending |
| [D009](D009-routine-booking-authority.md) | 4 / Q16 | Booking approval policy | D001, D002 | unanswered | Pending |

## Current frontier

Round 4: Q13 (D006 completing booking inside WhatsApp versus linking out), Q14 (D008 staff conversation privacy), Q15 (D007 concrete profile boundary), Q16 (D009 routine-booking approval). All are prepared and unanswered. Geography is explicitly deferred, not repeatedly assumed or asked.

## Unresolved or deferred branches

First patient channel and conversation completion, staff transcript visibility, profile content, and routine booking approval are open. Once these are settled, explore patient identity, staff roles, scheduling constraints, changes/cancellations, handoff/failure behavior, conversational languages, and beta readiness. Geography, library selection, and additional AI translations have durable follow-ups. Granular membership and first-increment location depth remain open.

## Shared understanding

Confirmed: practice/clinic organization model; Doctor, Receptionist, Patient roles; preserve full feature vision; start with basic booking and profiling; English code and EN/FR/AR/ES UI; beta early access. Both patients and staff initiate booking: patients likely through WhatsApp and other messaging apps, staff through a private management chat. Which channels are mandatory initially and the privacy boundary between staff conversations remain open. Profiling content remains uncertain. Beta geography is explicitly undecided and deferred.

## Final user confirmation

Pending. The session is active.

## Related follow-ups and work

Issue: https://github.com/codeonym-org/medora/issues/3. Draft PR: https://github.com/codeonym-org/medora/pull/4.

[Select internationalization/localization libraries later](../../follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md).

[Feature register](../../feature-register.md). [Additional AI translations](../../follow-ups/20261015T110819Z-ai-generated-additional-ui-translations/follow-up.md).

[Beta operating countries](../../follow-ups/20261015T121349Z-choose-beta-operating-countries/follow-up.md).

## History

- 2026-10-15T08:57:38Z — Assistant created session, recorded the supplied scope, and prepared round 1.

- 2026-10-15T10:28:02Z — Assistant saved all first-round answers, preserved both Q4 messages, recorded partial decisions, captured the library follow-up, and prepared round 2.

- 2026-10-15T11:08:19Z — Round 2 replies saved verbatim. Initial scope/languages/beta access recorded; organization recommendation and round 3 questions prepared. Full feature register and translation-extension follow-up added.

- 2026-10-15T12:13:49Z — Saved round 3 replies verbatim, confirmed the practice model, clarified accepted channel direction, kept profile scope open, captured geography deferral, and prepared round 4.
