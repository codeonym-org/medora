---
schema_version: 1
id: "FU-<DATETIME-title>"
title: "<actionable title>"
kind: question
status: captured
created_at: null
updated_at: null
observed_at: null
reported_by: null
owner: null
priority: null
severity: null
origin:
  session: null
  decision: null
  issue_url: null
  pr_url: null
  conversation_reference: null
  file_or_component: null
  revision: null
affected_components: []
related_decisions: []
dependencies: []
related_follow_ups: []
duplicate_of: null
tracking_issue: null
revisit:
  trigger: null
  due_at: null
resolution:
  resolved_at: null
  outcome: null
  evidence: []
---

# Summary

The idea, defect, uncertainty, or deferred task in one concise paragraph.

## Why — motivation and impact

Why it matters, affected users/workflows, cost of ignoring it, and rationale for priority/severity if assigned.

## When and where — discovery context

What task was underway, the triggering event or conversation, when it happened if known, and where the observation can be located again. Explain why it is outside the current scope.

## Original observation or request

Quote relevant user wording when available. Otherwise attribute the observation to the assistant. Label redactions explicitly.

## Analysis

Observed facts, reported facts, hypotheses, supporting/contradicting evidence, uncertainties, and suspected causes. Distinguish inference from established findings.

## Affected components and boundaries

Product capabilities or code components affected, related workflows, external dependencies, and what appears unaffected. Mark unknown scope explicitly.

## Reproduction or motivating example

For bugs: conditions, synthetic steps, expected versus actual behavior, and frequency. For ideas: a concrete scenario. Otherwise explain why this is not applicable.

## Options and proposed next action

Potential approaches and tradeoffs, smallest useful next step, owner if known, and any decision or authorization still needed.

## Dependencies and revisit trigger

Blocking decisions/work, related records, and the event or date that should bring this back into scope. Use unknown where not yet established.

## Acceptance and verification

Observable completion criteria and how they will be checked. For research/questions, define the evidence or decision needed.

## Resolution

Outcome, links to implementing work or evidence, completion date, and remaining limitations. For dismissal, explain why; for duplicates, link the canonical record. Until resolved: pending.

## Extra notes and history

Timestamped updates, corrections, status transitions and their rationale, and supporting evidence links.
