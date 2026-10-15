---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3",
  "title": "Medora product functionality and initial scope",
  "status": "active",
  "created_at": "2026-10-15T08:57:38Z",
  "updated_at": "2026-10-15T10:28:02Z",
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
    ".planning/follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md"
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
| [D001](D001-first-practice.md) | 1, 2 / Q5 | Roles and practice grouping | Root | needs-clarification | Three roles confirmed; team structure open |
| [D002](D002-anchor-problem.md) | 1, 2 / Q6 | Product benefits and launch breadth | Root | needs-clarification | All four benefits matter; release depth open |
| [D003](D003-pilot-market.md) | 1, 2 / Q7 | Market and languages | Root | needs-clarification | English code, localized UI; countries/languages open |
| [D004](D004-validation-access.md) | 1 | Practitioner access and advertising intent | Root | confirmed | No current access; advertise once working |
| [D005](D005-release-readiness.md) | 2 / Q8 | Early-release approach | D004 | unanswered | Pending |

## Current frontier

Round 2: Q5 (D001 practice grouping), Q6 (D002 launch coverage), Q7 (D003 initial countries/languages), and Q8 (D005 early-release approach). Questions are prepared; replies are pending. Q5–Q7 clarify partial answers; Q8 depends on the confirmed D004 intent.

## Unresolved or deferred branches

Practice relationships, release coverage, first countries/languages, and validation approach remain open. Staff permissions and shared scheduling depend on practice grouping. Detailed readiness criteria depend on launch scope. Contact channels and language-specific behavior await the operating context. Specific i18n/localization libraries are deferred in the linked follow-up.

## Shared understanding

The three roles are Doctor, Receptionist, and Patient. The user wants all four named administrative benefits addressed. Code is English; the UI uses translation/localization libraries. There are no current practitioner contacts for validation; the user plans to advertise after the product is live and functioning. These answers do not yet settle practice grouping, full first-release scope, actual countries/languages, or readiness criteria.

## Final user confirmation

Pending. The session is active.

## Related follow-ups and work

Issue: https://github.com/codeonym-org/medora/issues/3. Draft PR: https://github.com/codeonym-org/medora/pull/4.

[Select internationalization/localization libraries later](../../follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md).

## History

- 2026-10-15T08:57:38Z — Assistant created session, recorded the supplied scope, and prepared round 1.

- 2026-10-15T10:28:02Z — Assistant saved all first-round answers, preserved both Q4 messages, recorded partial decisions, captured the library follow-up, and prepared round 2.
