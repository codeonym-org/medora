# Issue tracker: GitHub

Issues and specs live in `codeonym-org/medora`. Use the `gh` CLI with an explicit `--repo codeonym-org/medora` when outside a checkout.
Follow [../github-workflow.md](../github-workflow.md) for branches, pull requests, and Project tracking.

## Operations

- Create: `gh issue create --repo codeonym-org/medora --title "..." --body-file <file>`.
- Read: `gh issue view <number> --repo codeonym-org/medora --json number,title,body,labels,comments`.
- List: `gh issue list --repo codeonym-org/medora --state open --json number,title,body,labels`.
- Comment: `gh issue comment <number> --repo codeonym-org/medora --body-file <file>`.
- Label: `gh issue edit <number> --repo codeonym-org/medora --add-label "..."`; use `--remove-label` to remove.
- Close: `gh issue close <number> --repo codeonym-org/medora`.
- Track: `gh project item-add 3 --owner codeonym-org --url <issue-url>`.

Write multiline bodies to a temporary file and pass `--body-file`.
When a skill says "publish to the issue tracker", create a GitHub issue.
When it says "fetch the relevant ticket", read the issue and its comments.

## Related work and wayfinding

Use native GitHub sub-issues and dependencies when supported. Otherwise, record `Part of #<parent>` and `Blocked by: #<number>` in the child body and maintain a task list in the parent.

A wayfinder map is an issue labelled `wayfinder:map`. Its child decision tickets use one of `wayfinder:research`, `wayfinder:prototype`, `wayfinder:grilling`, or `wayfinder:task`.

- Attach children with `gh issue edit <map> --repo codeonym-org/medora --add-sub-issue <child>`.
- Add dependencies with `gh issue edit <child> --repo codeonym-org/medora --add-blocked-by <blocker>`.
- Inspect with `gh issue view <number> --repo codeonym-org/medora --json title,body,labels,assignees,parent,subIssues,blockedBy`.
- Select the first open, unassigned child in map order whose blockers are all closed. Follow pagination for both children and blockers before deciding a ticket is unblocked.
- Claim with `gh issue edit <number> --repo codeonym-org/medora --add-assignee @me` before work.
- Resolve by posting findings, closing the ticket, and adding a linked result to the latest map body.

## Pull requests as a triage surface

PRs as a request surface: no.
