# Planning memory

This directory preserves the reasoning behind Medora decisions and discoveries across conversations. GitHub Issues track work; these records preserve the context and evidence. PR descriptions and chat history are pointers, not substitutes for the records.

## Layout and naming

```text
.planning/
  README.md
  templates/
    session.md
    decision.md
    follow-up.md
  decisions/
    <DATETIME-ISSUE-ID>/
      session.md
      D000-<slug>.md
      D001-<slug>.md
  follow-ups/
    <DATETIME-title>/
      follow-up.md
      <optional supporting evidence>
```

- `DATETIME` is the creation time in UTC, formatted `YYYYMMDDTHHMMSSZ`. Metadata timestamps use ISO 8601 UTC (`YYYY-MM-DDTHH:MM:SSZ`). Record time is not an inferred time of the original conversation.
- `ISSUE-ID` is the actual GitHub issue number, without `#`; store the repository and full issue URL in metadata. Reuse the same folder when continuing a session. A separately scoped session gets a new timestamped folder even if it shares an issue.
- Use lowercase hyphenated title slugs. Preserve directory names and decision IDs after creation; change the display title in metadata. If a creation-time collision occurs, use the next actual creation timestamp, never overwrite another record.
- If GitHub is unavailable, save under `<DATETIME-pending>` with a null issue and an explicit blocker. Once an issue exists, rename to the required issue-number form and repair references. Do not invent an issue ID or lose answers while waiting for GitHub.
- Decision IDs are sequential within a session (`D001`, `D002`, etc.); a full reference includes the session folder. `D000` may capture explicit user constraints supplied before the interview. One decision file covers one question; clarification exchanges stay with that decision.
- Cross-record metadata paths are relative to the repository root. Markdown links are relative to their containing file. Use real paths/URLs, `null`, or empty lists; do not invent evidence.
- Templates define required fields and sections. Mark unknown values `null`/`unknown`, and explain genuinely inapplicable sections. Extend records when necessary without silently changing field meanings; increment `schema_version` for incompatible schema changes.

## Grilling workflow

1. Read the product vision, the session index if resuming, relevant predecessor decisions, and related follow-ups. Create or reuse the tracking issue and session folder. Record the topic, constraints, participants, origin, and scope before the first round.
2. Build a decision tree. Ask only questions whose prerequisites are settled; record prerequisite links and the unresolved branches in `session.md`. Recommendations and alternatives belong beside the exact question, not in the confirmed-decision field.
3. Save each answer before asking the next round. Quote the user's words separately from the assistant's interpretation. Record a message/turn description if no conversation URL or message ID is available. For partial answers, retain unresolved subquestions; never substitute the recommendation for an omitted answer.
4. An explicit, unambiguous user choice can confirm that decision. If the interpretation introduces commitments the user did not state, use `needs-clarification` and ask. Silence, a timeout, and an assistant recommendation never confirm a decision.
5. Maintain the session's decision table, dependency tree, current question frontier, deferred branches, and linked follow-ups. A deliberately deferred question must name its reason, blocking prerequisite or revisit trigger, and follow-up when it represents future work.
6. Preserve history when an answer changes. Append the new exchange, record what changed and why, and identify downstream decisions needing reconsideration. A replacement decision links `supersedes`; the older record links `superseded_by`. Keep old replies intact rather than rewriting them to fit the latest outcome.
7. Before ending a round, persist records and report anything not yet saved. Follow the repository's branch/PR workflow for publication. Keep an ongoing interview's PR in draft and its issue open; saving records does not imply the session is complete.
8. When all in-scope branches are resolved or explicitly deferred, present the shared understanding and request explicit session confirmation. Store that confirmation before implementing the resulting design. Logging rules already requested by the user may be written during the interview.

Session statuses: `active`, `awaiting-confirmation`, `confirmed`, `paused`, `superseded`. Decision statuses: `unanswered`, `needs-clarification`, `confirmed`, `deferred`, `superseded`. A reopened decision returns to `needs-clarification` with its earlier answer retained in history.

## Follow-up workflow

- Capture an unrelated idea, bug, risk, question, or deferred task as soon as it is recognized. Record why it arose, when it was observed, where it was encountered, the current task, relevant evidence, analysis, affected product capabilities or code components, and why it is outside the current scope.
- Search existing follow-ups before creating another. Add new evidence to an existing record for the same concern. Distinct duplicates link to the canonical record; do not discard their provenance.
- Separate observed facts, user reports, hypotheses, and unknowns. Include reproduction steps for bugs when available; use explicit `not applicable` for other kinds. Do not invent a diagnosis or priority.
- `kind` is one of `feat`, `bug`, `docs`, `research`, `question`, `security`, `perf`, `refactor`, `test`, `ci`, `build`, `chore`. Record severity separately from delivery priority; an unassessed item has null values.
- Status progresses from `captured` to `triaged`, `scheduled`, `in-progress`, then `resolved`; `dismissed` and `duplicate` are alternative outcomes. Record an owner, next action, dependencies, and revisit trigger as they become known. Capture alone neither expands the current task nor authorizes implementation.
- Before related work, read matching open records and check whether their assumptions still hold. When promoting one to a GitHub issue, link both directions and keep the original context here. Resolve only with outcome/verification evidence; dismissal needs a reason, and duplication needs a canonical link.
- Keep each follow-up folder's `follow-up.md` as its canonical record. Update the index below when creating, scheduling, superseding, or resolving records.

## Confidentiality and sources

Use synthetic patient examples and avoid private practice details or credentials in this public repository. Preserve user replies verbatim when safe; if redaction is necessary, mark the redaction and reason explicitly and never claim the stored text is an unaltered transcript. Link restricted evidence instead of copying sensitive content. Record only relevant conversation excerpts.

Confirmed planning decisions inform product documents and implementation issues; those should link back to the originating records. A future architecture ADR records the architectural decision and links to relevant planning history. Do not silently replace an existing product constraint or ADR with a new interpretation.

## Schemas

- [Session schema](templates/session.md): purpose, scope, issue, origin, decision tree, round index, unresolved branches, follow-ups, and final confirmation.
- [Decision schema](templates/decision.md): context, predecessors, exact question, recommendations, raw replies, interpretation, outcome, consequences, evidence, and history.
- [Follow-up schema](templates/follow-up.md): why/when/where, analysis, affected components, kind, impact, next action, dependencies, and closure evidence.

## Sessions

| Session | Scope | Status |
| --- | --- | --- |
| [20261015T085738Z-3](decisions/20261015T085738Z-3/session.md) | Product functionality and initial scope; no technical stack | active |

## Follow-ups

| Follow-up | Kind | Status | Revisit trigger |
| --- | --- | --- | --- |
| [Select i18n/localization libraries](follow-ups/20261015T102802Z-select-internationalization-and-localization-libraries/follow-up.md) | build | captured | Technical stack planning after language requirements |
