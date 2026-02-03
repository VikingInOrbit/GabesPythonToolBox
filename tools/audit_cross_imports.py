"""Scan `src/` for cross-package imports and write a report.

Definition: a "cross-import" is an import in a module under
`src/<pkg>/...` that imports from a different top-level package
found under `src/` (e.g. `src/Simulation/...` importing `src/Geometry...`).

Output: `Output/log/audit_cross_imports.txt`
"""

import ast
import os
import pathlib
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
OUT_DIR = ROOT / "Output" / "log"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "audit_cross_imports.txt"


def find_top_level_packages(src_dir):
    pkgs = []
    if not src_dir.exists():
        return pkgs
    for p in src_dir.iterdir():
        if p.is_dir():
            # treat any directory under src as a top-level package
            pkgs.append(p.name)
    return pkgs


def analyze_file(path, top_pkgs):
    rel = path.relative_to(SRC)
    parts = rel.parts
    if not parts:
        return []
    own_pkg = parts[0]
    results = []
    try:
        src = path.read_text(encoding="utf-8")
        tree = ast.parse(src)
    except Exception as e:
        results.append((0, f"PARSE_ERROR: {e}"))
        return results

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.name
                top = name.split(".")[0]
                if top in top_pkgs and top != own_pkg:
                    results.append((node.lineno, f"import {name}"))
        elif isinstance(node, ast.ImportFrom):
            module = node.module
            # skip relative imports (module is None or level>0)
            if module:
                top = module.split(".")[0]
                if top in top_pkgs and top != own_pkg:
                    names = ",".join([a.name for a in node.names])
                    results.append((node.lineno, f"from {module} import {names}"))
    return results


def main():
    top_pkgs = find_top_level_packages(SRC)
    report = []
    cross_map = defaultdict(list)
    total_checked = 0
    for py in SRC.rglob("*.py"):
        total_checked += 1
        rel = py.relative_to(SRC)
        own_pkg = rel.parts[0] if rel.parts else "<unknown>"
        findings = analyze_file(py, top_pkgs)
        for lineno, text in findings:
            cross_map[py].append((lineno, text))

    with OUT_FILE.open("w", encoding="utf-8") as f:
        f.write("Cross-import audit report\n")
        f.write("=======================\n\n")
        f.write(f"Root: {ROOT}\n")
        f.write(f"Top-level packages under src/: {', '.join(top_pkgs)}\n")
        f.write(f"Total Python files scanned: {total_checked}\n\n")
        if not cross_map:
            f.write("No cross-imports found.\n")
            print(f"Wrote report to {OUT_FILE}")
            return

        f.write(f"Found cross-imports in {len(cross_map)} files:\n\n")
        for path, items in sorted(cross_map.items()):
            f.write(f"File: {path.relative_to(ROOT)}\n")
            for lineno, text in items:
                f.write(f"  L{lineno}: {text}\n")
            f.write("\n")

    print(f"Wrote report to {OUT_FILE}")


if __name__ == "__main__":
    main()
