import os
import re
import subprocess
import sys


def get_branch():
    try:
        p = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return p.stdout.strip()
    except Exception:
        return None


def main():
    branch = get_branch()
    threshold = 70
    if branch:
        b = branch.lower()
        if b in ("dev", "develop"):
            threshold = 80
        if b in ("main", "master"):
            threshold = 99
    cmd = [
        "pytest",
        "--maxfail=1",
        "--disable-warnings",
        "-q",
        "--cov=src",
        "--cov-report=term",
    ]

    env = os.environ.copy()
    root = os.getcwd()
    env["PYTHONPATH"] = root + os.pathsep + env.get("PYTHONPATH", "")

    proc = subprocess.run(cmd, capture_output=True, text=True, env=env)

    if proc.stdout:
        sys.stdout.write(proc.stdout)
    if proc.stderr:
        sys.stderr.write(proc.stderr)

    if proc.returncode != 0:
        print(
            "\nERROR: Tests failed. Run pre-commit run --all-files",
            file=sys.stderr,
        )
        sys.exit(proc.returncode)

    if "No data was collected" in (proc.stderr or ""):
        print(
            "\nERROR: Coverage reported no data. Ensure tests import project modules or set PYTHONPATH.",
            file=sys.stderr,
        )
        print("Run: python -m pytest --cov=src --cov-report=term", file=sys.stderr)
        sys.exit(5)

    m = re.search(r"TOTAL\s+\d+\s+\d+\s+(\d+)%", proc.stdout or "")
    if not m:
        print(
            "\nERROR: Could not determine coverage percent from pytest output.",
            file=sys.stderr,
        )
        print("Try: python -m pytest --cov=src --cov-report=term", file=sys.stderr)
        sys.exit(3)

    percent = int(m.group(1))

    if percent < threshold:
        print("\n" + "=" * 60, file=sys.stderr)
        print("COVERAGE CHECK FAILED", file=sys.stderr)
        print(f"Total coverage: {percent}%", file=sys.stderr)
        print(
            f"Required threshold for branch '{branch or 'unknown'}': {threshold}%",
            file=sys.stderr,
        )
        print("Quick fixes:", file=sys.stderr)
        print(" - Add/enable tests that exercise src/ modules", file=sys.stderr)
        print(
            " - Ensure tests import modules (e.g. import OilSim.flow)", file=sys.stderr
        )
        print(" - Run: python -m pytest --cov=src --cov-report=term", file=sys.stderr)
        print(f"ERROR: coverage {percent}% < threshold {threshold}%", file=sys.stderr)
        print("=" * 60 + "\n", file=sys.stderr)
        sys.exit(4)

    print(f"Coverage total: {percent}% (threshold {threshold}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
