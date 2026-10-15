---
{
  "schema_version": 1,
  "id": "FU-20261015T102802Z-select-internationalization-and-localization-libraries",
  "title": "Select internationalization and localization libraries when choosing the stack",
  "kind": "build",
  "status": "captured",
  "created_at": "2026-10-15T10:28:02Z",
  "updated_at": "2026-10-15T10:28:02Z",
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
    "conversation_reference": "First-round Q3 reply in the current product-grilling conversation",
    "file_or_component": "User interface localization",
    "revision": null
  },
  "affected_components": [
    "UI text",
    "Locale-aware formatting",
    "Language preferences"
  ],
  "related_decisions": [
    ".planning/decisions/20261015T085738Z-3/D003-pilot-market.md"
  ],
  "dependencies": [
    "Application stack decision (not yet made)",
    "Supported UI languages and locale requirements (not yet settled)"
  ],
  "related_follow_ups": [],
  "duplicate_of": null,
  "tracking_issue": null,
  "revisit": {
    "trigger": "When technical stack selection begins and initial language/locale requirements are known",
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

Select appropriate internationalization and localization libraries later, preserving the user's requirement for English code and a translated/localized UI.

## Why — motivation and impact

The user explicitly asked for library-supported UI translation/localization. Preserve this requirement so it is not lost when technical choices are made after the product interview. Delivery priority and impact severity have not been assessed.

## When and where — discovery context

Captured 2026-10-15T10:28:02Z during the first product-grilling round in [D003](../../decisions/20261015T085738Z-3/D003-pilot-market.md). The original message time is unknown. Library selection belongs to technical planning, explicitly outside the active session.

## Original observation or request

> Q3: CODE is ENG, UI is translated using i18n libraries and localisation libraries ..

## Analysis

Confirmed: English code and translated/localized UI through libraries. Unknown: application stack, exact supported languages, locale formats, and right-to-left needs. No library has been evaluated or selected. UI translations and AI conversational language support are separate requirements.

## Affected components and boundaries

UI text, language preferences, and locale-aware formatting are potential affected areas. Exact code components do not exist yet. Backend or conversational language handling is not specified by this request alone.

## Reproduction or motivating example

Motivating example: a user views interface labels and dates in their selected supported locale while source identifiers remain English. This is illustrative, not an approved detailed UX requirement. Bug reproduction is not applicable.

## Options and proposed next action

After product language requirements and the application stack are known, compare compatible libraries and translation workflows against those requirements. Capture a justified selection and configuration plan. Do not select or install libraries during this product interview.

## Dependencies and revisit trigger

Revisit during stack selection. Use D003 and any subsequent language decisions as inputs; supported language requirements remain unresolved. No due date or owner is assigned.

## Acceptance and verification

A later technical decision documents library choices, their rationale, supported translation/formatting needs, and a verification plan appropriate to the chosen stack. Link that decision here before closing the follow-up.

## Resolution

Pending. Capturing this item does not authorize implementation or change the session scope.

## Extra notes and history

- 2026-10-15T10:28:02Z — Assistant captured the user's requirement as deferred technical work; no dependency was selected or installed.
