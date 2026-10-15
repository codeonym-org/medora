---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D003",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "First pilot market",
  "status": "needs-clarification",
  "round": 1,
  "created_at": "2026-10-15T08:57:38Z",
  "updated_at": "2026-10-15T10:28:02Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "Patient communication",
    "Practice onboarding"
  ],
  "follow_ups": [
    ".planning/follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md"
  ],
  "sources": [
    "docs/product-vision.md",
    "Current conversation: first-round user answers; later user message completes Q4"
  ],
  "reply_recorded_at": "2026-10-15T10:28:02Z",
  "rounds": [
    1,
    2
  ]
}
---

# Context — why ask this?

International ambition does not specify the initial operating environment or language expectations. No market is inferred from the development timezone.

## Predecessor decisions

Root product question; no predecessor product decision is required. The supplied product vision and session scope remain constraints.

## Question

Which country should the first real pilot serve, and which languages must patients and staff be able to use from day one?

### Round 2 clarification — Q7 — Initial audience and languages

English code and a localized UI are recorded. Which countries and actual UI languages should the first release support? If that is undecided, say so and we will keep it explicitly open.

## Recommendation and alternatives

Choose one initial market and the languages its actual users need. Keep international expansion as the longer-term direction.

This is an assistant recommendation, not a user decision. Alternatives remain open until the user replies.

Round 2 recommendation: Choose a defined initial audience and supported language list, even if Medora is designed to expand internationally.

No reply to the round 2 clarification has been received.

## User reply — original words

Recorded 2026-10-15T10:28:02Z. Source: current conversation; original message timestamps were not supplied.

> Q3: CODE is ENG, UI is translated using i18n libraries and localisation libraries ..

## Interpretation

Code should be in English. The UI should support translation and localization through suitable libraries. This is a product/engineering constraint, not a selection of a particular library, application stack, initial market, or actual supported languages. UI translation does not by itself specify AI conversation languages.

## Decision and rationale

Confirmed portion: English code and a translated/localized UI. Country coverage, the first language list, and AI conversation language support remain unresolved. Specific library selection is deferred outside this product interview. The user did not supply a further rationale; none is attributed to them.

## Consequences and affected components

Retain internationalization/localization requirements in future implementation planning. Clarify intended first-release users and UI languages separately from library choices.

## Assumptions, evidence, and open questions

Q7 asks for the initial countries and language list or an explicit deferral. Formatting preferences, right-to-left requirements, and conversational language expectations can be explored once the relevant product requirements are known. The user reply is the source; no practitioner evidence has been gathered.

## Extra notes and follow-ups

[Library selection follow-up](../../follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md) captures the technical requirement for a later session. No library choice is being made now.

## History

- 2026-10-15T08:57:38Z — Assistant prepared the first-round question; user response is pending.

- 2026-10-15T10:28:02Z — Assistant saved the actual reply and its interpretation; status is needs-clarification. Original recommendations remain historical proposals.
