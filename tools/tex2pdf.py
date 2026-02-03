#!/usr/bin/env python3
"""Compile .tex files to PDF.

Features added:
- Skip files that do not contain a `\documentclass` (likely fragments).
- Run LaTeX in the .tex parent directory so relative \input and resources resolve.
- Use absolute output directories and preserve relative paths under output root.
- Better logging and non-fatal errors per-file.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path
from typing import List


def find_tex_files(input_path: Path) -> List[Path]:
    if input_path.is_file() and input_path.suffix == ".tex":
        return [input_path]
    if input_path.is_dir():
        return sorted(input_path.rglob("*.tex"))
    return []


def file_has_documentclass(tex: Path) -> bool:
    try:
        text = tex.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return False
    return "\\documentclass" in text


def run_command(cmd: List[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=cwd
    )


def compile_tex(tex: Path, outdir: Path, use_latexmk: bool, dry_run: bool) -> bool:
    outdir = outdir.resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    # Only compile standalone documents
    if not file_has_documentclass(tex):
        print(f"SKIP (no \\documentclass): {tex}")
        return True

    cwd = tex.parent
    texname = tex.name

    if use_latexmk:
        # latexmk needs to be run from the tex file directory for relative paths
        cmd = ["latexmk", "-pdf", "-silent", "-outdir=" + str(outdir), texname]
        if dry_run:
            print("DRY: (cwd=", cwd, ") ", " ".join(cmd))
            return True
        proc = run_command(cmd, cwd=cwd)
        if proc.returncode != 0:
            print(f"Error compiling {tex} (latexmk). Output:\n{proc.stdout}")
            return False
        return True
    else:
        # pdflatex fallback; run two passes in tex parent dir
        cmd = [
            "pdflatex",
            "-interaction=nonstopmode",
            "-output-directory",
            str(outdir),
            texname,
        ]
        if dry_run:
            print("DRY: (cwd=", cwd, ") ", " ".join(cmd), "(twice)")
            return True
        for i in range(2):
            proc = run_command(cmd, cwd=cwd)
            if proc.returncode != 0:
                print(
                    f"Error compiling {tex} (pdflatex pass {i+1}). Output:\n{proc.stdout}"
                )
                return False
        return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compile .tex files to PDF (latexmk or pdflatex)"
    )
    parser.add_argument(
        "--input",
        "-i",
        type=Path,
        default=Path.cwd(),
        help="Input file or directory to search for .tex files",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Output directory root (preserves relative paths). If omitted, writes PDFs next to .tex files.",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Only print actions; do not invoke LaTeX"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force compile even if no documentclass is found (may be fragment).",
    )
    args = parser.parse_args()

    input_path = args.input
    out_root = args.output
    dry_run = args.dry_run
    force = args.force

    tex_files = find_tex_files(input_path)
    if not tex_files:
        print(f"No .tex files found in {input_path}")
        return 0

    use_latexmk = shutil.which("latexmk") is not None
    backend = "latexmk" if use_latexmk else "pdflatex"
    print(f"Found {len(tex_files)} .tex files; using backend: {backend}")

    errors = 0
    for tex in tex_files:
        # determine output directory for this tex file
        if out_root:
            try:
                rel = (
                    tex.relative_to(input_path)
                    if input_path.is_dir()
                    else Path(tex.name)
                )
            except Exception:
                rel = Path(tex.name)
            target_dir = (out_root / rel.parent).resolve()
        else:
            target_dir = tex.parent.resolve()

        if not force and not file_has_documentclass(tex):
            print(f"Skipping fragment (no documentclass): {tex}")
            continue

        print(f"Compiling: {tex} -> {target_dir}")
        ok = compile_tex(tex, target_dir, use_latexmk, dry_run)
        if not ok:
            errors += 1

    if errors:
        print(f"Finished with {errors} errors")
        return 2
    print("All done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
