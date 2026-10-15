---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3",
  "title": "Medora product functionality and initial scope",
  "status": "active",
  "created_at": "2026-10-15T08:57:38Z",
  "updated_at": "2026-10-15T11:08:19Z",
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
    ".planning/follow-ups/20261015T110819Z-ai-generated-additional-ui-translations/follow-up.md"
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
| [D001](D001-first-practice.md) | 1–3 / Q9 | Roles and practice grouping | Root | needs-clarification | Three roles confirmed; organization model recommended |
| [D002](D002-anchor-problem.md) | 1–2 | Product benefits and launch breadth | Root | confirmed | Preserve all features; start with basic booking and profiling |
| [D003](D003-pilot-market.md) | 1–3 / Q12 | Market and languages | Root | needs-clarification | EN/FR/AR/ES UI; countries unspecified |
| [D004](D004-validation-access.md) | 1 | Practitioner access and advertising intent | Root | confirmed | No current access; advertise once working |
| [D005](D005-release-readiness.md) | 2 | Early-release approach | D004 | confirmed | Beta users get early access |
| [D006](D006-booking-entry.md) | 3 / Q10 | First booking experience | D002 | unanswered | Pending |
| [D007](D007-basic-patient-profile.md) | 3 / Q11 | Basic profiling boundary | D002 | unanswered | Pending |

## Current frontier

Round 3: Q9 (D001 organization-model recommendation), Q10 (D006 booking entry), Q11 (D007 profiling boundary), Q12 (D003 beta geography or explicit deferral). Replies are pending. These questions can be answered without assuming each other's outcome.

## Unresolved or deferred branches

Organization membership and location model await Q9. Booking channels and basic profile content await Q10/Q11. The beta market remains open; Q12 offers explicit deferral. Staff permissions, booking approval and cancellation behavior, identity, profile visibility, intake/briefing depth, and beta-readiness criteria follow once their prerequisites are settled. I18n library selection and additional AI translations are in separate follow-ups.

## Shared understanding

Confirmed: Doctor, Receptionist, Patient roles; preserve the full feature vision and add features incrementally; first increment is basic booking and profiling; code in English; localized UI initially in English, French, Arabic, Spanish; beta users get early access. Additional AI-generated translations are requested as an extension capability. Organization structure, initial booking/profile details, market geography, and translation publication policy are not yet confirmed.

## Final user confirmation

Pending. The session is active.

## Related follow-ups and work

Issue: https://github.com/codeonym-org/medora/issues/3. Draft PR: https://github.com/codeonym-org/medora/pull/4.

[Select internationalization/localization libraries later](../../follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md).

[Feature register](../../feature-register.md). [Additional AI translations](../../follow-ups/20261015T110819Z-ai-generated-additional-ui-translations/follow-up.md).

## History

- 2026-10-15T08:57:38Z — Assistant created session, recorded the supplied scope, and prepared round 1.

- 2026-10-15T10:28:02Z — Assistant saved all first-round answers, preserved both Q4 messages, recorded partial decisions, captured the library follow-up, and prepared round 2.

- 2026-10-15T11:08:19Z — Round 2 replies saved verbatim. Initial scope/languages/beta access recorded; organization recommendation and round 3 questions prepared. Full feature register and translation-extension follow-up added.
