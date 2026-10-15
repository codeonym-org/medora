# GitHub workflow

Repository: https://github.com/codeonym-org/medora

Project: https://github.com/orgs/codeonym-org/projects/3

Medora is public source with all rights reserved. See [../LICENSE](../LICENSE) and [../NOTICE](../NOTICE).

## Changes and tracking

Create an issue before feature work, add it to the Project, and assign Area and Priority. Status progresses through Backlog, Todo, In Progress, In Review, and Done. Engineering Priority values P0–P3 describe delivery priority, not patient urgency.

Follow [../CONTRIBUTING.md](../CONTRIBUTING.md) for issue-linked branches, conventional commits, and PR titles ending with the issue key. Add issues with `gh project item-add 3 --owner codeonym-org --url <issue-url>`. Repository linkage does not automatically add future issues; add them explicitly unless a Project auto-add workflow is configured later.

## Protection

The rulesets match `codeonym-oss/acli-py` and `codeonym-org/gsm-agent-kit`: PR-only changes to `main`, linear history, resolved review threads, and checks `ci-ok`, `branch-name`, `commits`, `pr-title`. The approval count is zero; administrators may bypass only through a PR. Force pushes and deletion of main are blocked. Only squash merges are enabled and merged branches are deleted. Tags matching `v*` are immutable with no bypass actors.

The first commit bootstraps the empty repository before these protections are installed. Subsequent changes use the protected workflow.

## Automation and limits

CI and conventions adapt the reference repositories without choosing an application framework. Commitizen 4.19.2 validates commits, matching gsm-agent-kit's tooling version and prefix exceptions. GitHub Actions references are pinned to commits and Dependabot checks Actions weekly. Workflow tokens default to read access and cannot approve PRs.

Repository checks validate tracked text, local Markdown links, YAML/JSON syntax, and branch validation behavior. Replace or extend the CI gate with appropriate application checks as implementation arrives. Keep all four required check names stable.

Secret scanning, push protection, dependency alerts, and private vulnerability reporting are enabled on GitHub. No deployment, package publishing, credentials, or external patient-data integrations are configured. Release automation awaits the chosen application packaging and release policy; `ENABLE_RELEASES=false` and `PUBLISH_TO_PYPI=false` record that publishing is disabled.

## Engineering skills

`docs/agents/issue-tracker.md`, `triage-labels.md`, and `domain.md` configure ticketing, triage vocabulary, and domain-document consumption. Edit these files directly when conventions change. A root glossary and `docs/adr/` are created lazily when domain terminology and architecture decisions are resolved.
