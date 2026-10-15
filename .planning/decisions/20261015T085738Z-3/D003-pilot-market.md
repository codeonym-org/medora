---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D003",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "First pilot market",
  "status": "deferred",
  "round": 1,
  "created_at": "2026-10-15T08:57:38Z",
  "updated_at": "2026-10-15T12:13:49Z",
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
    ".planning/follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md",
    ".planning/follow-ups/20261015T110819Z-ai-generated-additional-ui-translations/follow-up.md",
    ".planning/follow-ups/20261015T121349Z-choose-beta-operating-countries/follow-up.md"
  ],
  "sources": [
    "docs/product-vision.md",
    "Current conversation: first-round user answers; later user message completes Q4"
  ],
  "reply_recorded_at": "2026-10-15T12:13:49Z",
  "rounds": [
    1,
    2,
    3
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

### Round 3 clarification — Q12 — Beta geography

Which country or countries will the beta practices operate in, or should we leave that undecided until beta recruitment?

## Recommendation and alternatives

Choose one initial market and the languages its actual users need. Keep international expansion as the longer-term direction.

This is an assistant recommendation, not a user decision. Alternatives remain open until the user replies.

Round 2 recommendation: Choose a defined initial audience and supported language list, even if Medora is designed to expand internationally.

No reply to the round 2 clarification has been received.

Round 3 recommendation: Name the first beta market before defining country-specific operating rules. We can continue the general product design while that choice is open.

No reply to round 3 has been received.

## User reply — original words

Recorded 2026-10-15T10:28:02Z. Source: current conversation; original message timestamps were not supplied.

> Q3: CODE is ENG, UI is translated using i18n libraries and localisation libraries ..

Round 2 reply, recorded 2026-10-15T11:08:19Z; original message timestamp unavailable:

> Q7: we will start with ENGLISH, FRENCH, ARABIC, SPANISH (other languages can be auto generated using AI models)

Round 3 reply, recorded 2026-10-15T12:13:49Z; original message timestamp unavailable:

> q12: undecided

## Interpretation

Beta geography is explicitly undecided. Existing English/French/Arabic/Spanish UI commitments remain valid; languages do not establish operating countries. Keep country-specific decisions open and capture a follow-up for beta planning.

## Decision and rationale

Confirmed language choices are retained. The geography portion is deferred with no country inferred. Revisit before defining beta recruitment eligibility and country-specific operating rules.

## Consequences and affected components

Initial language list is known; Arabic requires a UI suitable for right-to-left reading. Locale variants, patient-facing conversation languages, translation quality checks, and geographic launch scope remain open. No library or model is selected.

## Assumptions, evidence, and open questions

The beta market is deliberately undecided. Locale-specific operational decisions remain unresolved until the follow-up is revisited. UI language list is confirmed; regional variants, AI conversation coverage, and generated-translation publication remain open.

## Extra notes and follow-ups

[Library selection follow-up](../../follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md) captures the technical requirement for a later session. No library choice is being made now.

[AI-generated additional translations](../../follow-ups/20261015T110819Z-ai-generated-additional-ui-translations/follow-up.md) records the new extension idea and its unresolved review/publication behavior.

[Beta geography follow-up](../../follow-ups/20261015T121349Z-choose-beta-operating-countries/follow-up.md) holds the deferred country choice and revisit trigger.

## History

- 2026-10-15T08:57:38Z — Assistant prepared the first-round question; user response is pending.

- 2026-10-15T10:28:02Z — Assistant saved the actual reply and its interpretation; status is needs-clarification. Original recommendations remain historical proposals.

- 2026-10-15T11:08:19Z — Recorded round 2 answer; status needs-clarification.
  - Previous interpretation: Code should be in English. The UI should support translation and localization through suitable libraries. This is a product/engineering constraint, not a selection of a particular library, application stack, initial market, or actual supported languages. UI translation does not by itself specify AI conversation languages.
  - Previous decision summary: Confirmed portion: English code and a translated/localized UI. Country coverage, the first language list, and AI conversation language support remain unresolved. Specific library selection is deferred outside this product interview. The user did not supply a further rationale; none is attributed to them.

- 2026-10-15T12:13:49Z — Saved round 3 reply; status deferred.
  - Prior interpretation: The first UI languages are English, French, Arabic, and Spanish. The user also wants the ability to generate additional translations using AI. Code remains English. This does not select deployment countries, regional language variants, AI conversation coverage, a model/provider, or an automatic publication/review policy.
  - Prior decision summary: Confirmed portions: English code, localized UI, and initial support for English, French, Arabic, Spanish. AI-generated additional translations are recorded as an extension capability; review and publication behavior are unresolved. First beta country/countries remain unspecified.
