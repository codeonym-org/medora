---
{
  "schema_version": 1,
  "id": "20261015T085738Z-3/D020",
  "session": ".planning/decisions/20261015T085738Z-3/session.md",
  "title": "Patient conversation languages",
  "status": "confirmed",
  "round": 7,
  "created_at": "2026-10-15T14:24:28Z",
  "updated_at": "2026-10-15T14:35:28Z",
  "asked_at": null,
  "answered_at": null,
  "confirmed_at": null,
  "decision_owner": "user",
  "recorded_by": "assistant",
  "issue_url": "https://github.com/codeonym-org/medora/issues/3",
  "predecessors": [
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md",
    ".planning/decisions/20261015T085738Z-3/D003-pilot-market.md"
  ],
  "related_decisions": [],
  "supersedes": [],
  "superseded_by": [],
  "affected_components": [
    "WhatsApp assistant",
    "Language preferences",
    "Patient messages"
  ],
  "follow_ups": [],
  "sources": [
    ".planning/decisions/20261015T085738Z-3/D006-booking-entry.md",
    ".planning/decisions/20261015T085738Z-3/D003-pilot-market.md"
  ],
  "reply_recorded_at": "2026-10-15T14:35:28Z"
}
---

# Context — why ask this?

Four UI languages are confirmed, but that did not automatically establish supported patient conversation languages. The geography portion of D003 is deferred and is not a prerequisite here.

## Predecessor decisions

[D006](D006-booking-entry.md); [D003](D003-pilot-market.md). Only their accepted requirements are prerequisites; unresolved details and other round 7 answers are not assumed.

## Question

Q27 — Patient conversation languages: Should the WhatsApp agent also converse in English, French, Arabic, and Spanish, adapting to the patient's language and allowing them to switch?

## Recommendation and alternatives

Yes. Use those four as the initial supported conversation languages, separately from the staff UI language. Ask when the patient's preference is unclear.

The user reply and current decision are recorded below; earlier recommendation wording is historical and is not automatically accepted.

## User reply — original words

Round 7 reply, recorded 2026-10-15T14:35:28Z; original message timestamp unavailable:

> q27: the agent is instructed to reply in the user's own language and it saves that  preference for future interacrions unless the user / patient say so

## Interpretation

The user specifies language-adaptive replies and remembered preference until the user/patient changes it. This is not acceptance of the assistant's fixed four-conversation-language limit. Initial UI locales remain EN/FR/AR/ES; patient conversation language behavior is a separate requirement. Preference scope for a contact booking for several patients remains open.

## Decision and rationale

Confirmed: reply in the user's own language, remember that preference across future interactions, and honor changes requested by the user/patient. Do not impose the UI language list as the conversation-language whitelist.

## Consequences and affected components

Confirmed: reply in the user's own language, remember that preference across future interactions, and honor changes requested by the user/patient. Do not impose the UI language list as the conversation-language whitelist. How to handle uncertain language, model capability limits, mixed-language messages, contact versus patient preference, and translating clinical/practice templates still needs product decisions. No guarantee of equal fluency or support quality for every language is made.

## Assumptions, evidence, and open questions

How to handle uncertain language, model capability limits, mixed-language messages, contact versus patient preference, and translating clinical/practice templates still needs product decisions. No guarantee of equal fluency or support quality for every language is made.

## Extra notes and follow-ups

No unrelated follow-up introduced by this question.

## History

- 2026-10-15T14:24:28Z — Prepared the round 7 question from accepted prerequisites.

- 2026-10-15T14:35:28Z — Saved round 7 reply; status confirmed. Prior interpretation: Pending. Prior decision: Pending.
