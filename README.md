# Medora

**Your practice, thoughtfully organized.**

Medora is an AI medical secretary for doctors and clinics. It will coordinate appointments, collect preliminary intake, highlight requests needing human review, and prepare patient context before consultations.

## Status

The repository currently contains product documentation and engineering infrastructure. No application, patient-data storage, AI integration, or clinical service is implemented. Development starts with reliable scheduling and backend permission enforcement.

- [Product vision and phased scope](docs/product-vision.md)
- [Domain vocabulary](GLOSSARY.md)
- [Evolving domain model](docs/domain-model.md)
- [Contribution workflow](CONTRIBUTING.md)
- [GitHub rules and automation](docs/github-workflow.md)
- [Project board](https://github.com/orgs/codeonym-org/projects/3)
- [Security reporting](SECURITY.md)

## Repository checks

Python is used for repository tooling only; the application stack is undecided.
With Python 3.11+ and uv installed:

```sh
uv run --no-project --with pyyaml==6.0.3 python scripts/check_repository.py
python3 -m unittest discover -s tests -v
python3 scripts/check_branch_name.py feat/1-scheduling-foundation
uvx --from commitizen==4.19.2 cz check --rev-range origin/main..HEAD
```

The last command checks commits on a feature branch after fetching `origin/main`.

## Rights

Publicly visible for inspection; **all rights reserved**. Original Medora code and documentation are not released under an open-source license. Reuse, modification, redistribution, sublicensing, and sale require prior written permission, subject to applicable law and hosting platform terms. See [LICENSE](LICENSE).

Adapted repository automation retains its original MIT terms; see [NOTICE](NOTICE) and [the upstream license](third_party/acli-py-LICENSE).
