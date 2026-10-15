"""Validate repository text, local documentation links, and configuration syntax."""

import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    output = subprocess.check_output(["git", "ls-files", "-z"], cwd=root)
    paths = [root / name.decode() for name in output.split(b"\0") if name]
    errors = []
    for path in paths:
        if path.suffix not in {".md", ".yml", ".yaml", ".json", ".py", ".toml"}:
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root)
        if not text.endswith("\n"):
            errors.append(f"{relative}: missing final newline")
        for number, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"{relative}:{number}: trailing whitespace")
        try:
            if path.suffix in {".yml", ".yaml"}:
                yaml.safe_load(text)
            elif path.suffix == ".json":
                json.loads(text)
        except (yaml.YAMLError, json.JSONDecodeError) as exc:
            errors.append(f"{relative}: {exc}")
        if path.suffix == ".md":
            # Only inline Markdown links; code examples and anchors are excluded.
            prose = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
            for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", prose):
                url = urlsplit(target.strip("<>"))
                if not url.scheme and not url.netloc and url.path:
                    if not (path.parent / unquote(url.path)).exists():
                        errors.append(f"{relative}: missing link target {target}")
    if not paths:
        errors.append("No tracked files; stage repository files before running this check.")
    for error in errors:
        print(error)
    if errors:
        return 1
    print(f"Repository checks passed ({len(paths)} tracked files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
