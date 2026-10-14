#!/usr/bin/env python3
"""Mechanical checks for one Target Agent, as defined in validate.md Step 2.

Usage: validate.py --root <target-project_root> --slug <target-slug>
Read-only. Exit code: 0 = no errors, 1 = at least one error, 2 = usage error.
"""
import argparse
import os
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
TEMPLATE = PROJECT_ROOT / ".agents/evolver/templates/agent.template.md"
SESSION_HEADING = "## Session Start (mandatory)"
ROOT_PREFIX = re.compile(r"^<(?:target-)?project_root>/")
KNOWN_PATH = re.compile(r"AGENTS\.md|LEARNINGS\.md|README\.md|\.agents/|\.github/")

findings = []  # (severity, check, file, issue)


def add(severity, check, file, issue):
    findings.append((severity, check, file, issue))


def section(text, heading):
    """Return the whitespace-normalised body below heading, or None."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == heading:
            body = []
            for nxt in lines[i + 1:]:
                if nxt.startswith("## "):
                    break
                body.append(nxt)
            return " ".join(" ".join(body).split())
    return None


def table_rows(path):
    """Return the data rows of the first table in path as lists of cells."""
    rows = [l.strip() for l in path.read_text().splitlines() if l.lstrip().startswith("|")]
    data = [r for r in rows[1:] if not re.fullmatch(r"[|\s:-]+", r)]
    return [[c.strip() for c in r.strip("|").split("|")] for r in data]


def check_completeness(root, slug):
    agent = root / ".agents" / f"{slug}.agent.md"
    link = root / ".github/agents" / f"{slug}.agent.md"
    for path in (agent, root / f"README-{slug}.md", root / "AGENTS.md"):
        if not path.is_file():
            add("Error", "Completeness", path.relative_to(root), "file is missing")
    rel = link.relative_to(root)
    if not link.is_symlink():
        add("Error", "Completeness", rel, "is not a symlink")
    elif os.readlink(link) != f"../../.agents/{slug}.agent.md":
        add("Error", "Completeness", rel, f"points to {os.readlink(link)}")
    elif not link.exists():
        add("Error", "Completeness", rel, "symlink target does not exist")


def check_session_start(root, slug):
    agent = root / ".agents" / f"{slug}.agent.md"
    if not agent.is_file():
        return
    if not TEMPLATE.is_file():
        add("Error", "Session Start", TEMPLATE, "template is missing")
        return
    actual = section(agent.read_text(), SESSION_HEADING)
    rel = agent.relative_to(root)
    if actual is None:
        add("Error", "Session Start", rel, "section is missing")
    elif actual != section(TEMPLATE.read_text(), SESSION_HEADING):
        add("Error", "Session Start", rel, "differs from the template; review as translation")


def check_index_coverage(root, slug):
    base = root / ".agents" / slug
    for kind in ("skills", "guides", "templates"):
        folder = base / kind
        if not folder.is_dir():
            continue
        index = folder / "INDEX.md"
        rel = index.relative_to(root)
        if not index.is_file():
            add("Error", "INDEX coverage", folder.relative_to(root), "INDEX.md is missing")
            continue
        listed = set()
        for cells in table_rows(index):
            listed.update(re.findall(r"`([^`]+\.md)`", cells[-1]))
        present = {p.name for p in folder.glob("*.md")} - {"INDEX.md"}
        for name in sorted(present - listed):
            add("Error", "INDEX coverage", rel, f"{name} is not listed")
        for name in sorted(listed - present):
            add("Error", "INDEX coverage", rel, f"row names missing file {name}")


def check_trigger_form(root, slug):
    index = root / ".agents" / slug / "skills" / "INDEX.md"
    if not index.is_file():
        return
    for cells in table_rows(index):
        if not re.match(r"(User asks to|After)\b", cells[0]):
            add("Warning", "Trigger form", index.relative_to(root), f'row "{cells[0]}" does not start with "User asks to" or "After"')


def check_path_resolution(root, slug):
    base = root / ".agents" / slug
    files = [root / ".agents" / f"{slug}.agent.md"]
    if base.is_dir():
        files += [p for p in sorted(base.rglob("*.md")) if not p.name.startswith("README")]
    for path in files:
        if not path.is_file():
            continue
        in_session = False
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if line.startswith("## "):
                in_session = line.strip() == SESSION_HEADING
            if in_session:
                continue
            for span in re.findall(r"`([^`]+)`", line):
                for token in span.split():
                    if KNOWN_PATH.search(token) and not ROOT_PREFIX.match(token) and not token.startswith("../"):
                        add("Error", "Path resolution", f"{path.relative_to(root)}:{number}", f"bare path {token}")


def report():
    for severity, title in (("Error", "Errors (must fix)"), ("Warning", "Warnings (should fix)")):
        rows = [f for f in findings if f[0] == severity]
        if not rows:
            continue
        print(f"### {title}")
        print("| # | Check | File | Issue |")
        print("|---|-------|------|-------|")
        for number, (_, check, file, issue) in enumerate(rows, 1):
            print(f"| {number} | {check} | {file} | {str(issue).replace('|', chr(92) + '|')} |")
        print()
    if not findings:
        print("All mechanical checks passed.")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", required=True, help="<target-project_root>")
    parser.add_argument("--slug", required=True, help="<target-slug>")
    args = parser.parse_args()
    root = Path(args.root)
    if not root.is_dir():
        print(f"root is not a directory: {root}", file=sys.stderr)
        return 2
    for check in (check_completeness, check_session_start, check_index_coverage, check_trigger_form, check_path_resolution):
        check(root, args.slug)
    report()
    return 1 if any(f[0] == "Error" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
