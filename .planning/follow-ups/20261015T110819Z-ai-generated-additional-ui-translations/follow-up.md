---
{
  "schema_version": 1,
  "id": "FU-20261015T110819Z-ai-generated-additional-ui-translations",
  "title": "Define AI-generated additional UI translations",
  "kind": "feat",
  "status": "captured",
  "created_at": "2026-10-15T11:08:19Z",
  "updated_at": "2026-10-15T11:08:19Z",
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
    "conversation_reference": "Round 2 Q7 reply",
    "file_or_component": "UI translations",
    "revision": null
  },
  "affected_components": [
    "UI translations",
    "Language availability",
    "Translation review"
  ],
  "related_decisions": [
    ".planning/decisions/20261015T085738Z-3/D003-pilot-market.md"
  ],
  "dependencies": [
    "Definition of supported UI text and templates",
    "Translation review and publication policy"
  ],
  "related_follow_ups": [
    ".planning/follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md"
  ],
  "duplicate_of": null,
  "tracking_issue": null,
  "revisit": {
    "trigger": "When planning languages beyond the initial English, French, Arabic, and Spanish release",
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

Preserve the user-requested ability to generate additional UI translations with AI beyond the initial four languages.

## Why — motivation and impact

The user wants language expansion without manually drafting every translation. This capability must remain recorded while the first increment focuses on booking and profiling. No priority or delivery date is assigned.

## When and where — discovery context

Recorded 2026-10-15T11:08:19Z during round 2 Q7. Original message timestamp is unavailable. The extension belongs to later language planning; no AI provider or implementation is being selected during this product session.

## Original observation or request

> Q7: we will start with ENGLISH, FRENCH, ARABIC, SPANISH (other languages can be auto generated using AI models)

## Analysis

The initial language list and AI-generation idea are explicit. Generation timing, supported content, approval, publication, quality expectations, fallback behavior, and accountability are unspecified. The assistant recommends defining review before publishing generated translations; the user has not accepted that policy yet. Generation does not establish that every language is fully supported.

## Affected components and boundaries

UI translations, available-language lists, fallback content, and review workflows. Clinical templates and AI conversation languages are not automatically included. Library selection is separately tracked.

## Reproduction or motivating example

A later language is requested, AI drafts translated interface strings, and the eventual approved workflow determines when that language becomes available. This scenario illustrates the capability; approval details remain open. Not a bug report.

## Options and proposed next action

Clarify whether generation occurs during development, through a staff-requested workflow, or dynamically for users. Decide review, publication, fallback, and supported-content boundaries before implementation.

## Dependencies and revisit trigger

Revisit when expanding beyond the initial four languages. Use the UI translation structure and agreed review/publication requirements. No deadline or owner is assigned.

## Acceptance and verification

A future decision defines supported content, generation trigger, review/publication policy, and fallback behavior. A resulting implementation must demonstrate those behaviors before this item is resolved.

## Resolution

Pending; capturing the capability is not authorization to publish generated content or invoke an AI service.

## Extra notes and history

- 2026-10-15T11:08:19Z — Assistant captured the request as a distinct language-expansion follow-up.
