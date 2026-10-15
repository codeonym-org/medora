# Contribution workflow

Medora is public source with all rights reserved. Repository visibility and this workflow do not grant permission to modify or redistribute it; obtain the copyright holder's permission before contributing.

1. Start from a GitHub issue with acceptance criteria. Add it to [the Project](https://github.com/orgs/codeonym-org/projects/3), and set Area and Priority.
2. Branch from `main` using `<type>/<issue>-<slug>`, for example `feat/5-appointment-booking`.
3. Use Conventional Commits: `<type>(<optional scope>)<optional !>: <summary>`. Use an imperative, lowercase summary without a trailing period.
4. Open a focused PR titled, for example, `feat: add appointment booking (#5)`. Link the issue with `Fixes #5` in its body.
5. Pass required checks, resolve review threads, and squash-merge. Mark work Done when the issue's acceptance criteria pass.

Allowed types: `feat`, `fix`, `perf`, `build`, `docs`, `refactor`, `test`, `ci`, `chore`, `revert`. Bot branches `dependabot/*` and `release-please--*` are exempt from issue-linked branch names. The issue key belongs in the branch and PR title; it is optional in individual commits. Commitizen allows the same merge/revert/fixup/squash prefixes as the reference repositories.

`main` requires a PR, linear history, resolved review threads, and `ci-ok`, `branch-name`, `commits`, and `pr-title`. Administrators may bypass only through a PR. Squash is the only merge method; merged branches are deleted. Release tags matching `v*` cannot be changed or deleted.

Use only fictional patient and practice data in issues, logs, examples, screenshots, and tests. Report vulnerabilities privately using [SECURITY.md](SECURITY.md).

Run the commands in [README.md](README.md). Initial CI checks repository structure, local documentation links, YAML/JSON syntax, whitespace, and branch validation behavior. Application tests, linting, type checks, and build verification must be added with the application stack; these repository checks do not establish clinical or application correctness.
