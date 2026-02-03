#!/usr/bin/env python3
import os
import sys
import xml.etree.ElementTree as ET


def parse_coverage_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    lr = root.attrib.get("line-rate")
    if lr is None:
        for c in root:
            if "line-rate" in c.attrib:
                lr = c.attrib.get("line-rate")
                break
    if lr is None:
        raise RuntimeError("line-rate not found in coverage.xml")
    val = float(lr)
    if val <= 1.5:
        return val * 100
    return val


def main():
    branch = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("BRANCH", "")
    b = (branch or "").lower()
    threshold = 70
    if b in ("dev", "develop"):
        threshold = 80
    if b in ("main", "master"):
        threshold = 99

    xml_path = "coverage.xml"
    if not os.path.exists(xml_path):
        print(
            f"ERROR: {xml_path} not found. Ensure pytest produced coverage.xml",
            file=sys.stderr,
        )
        return 2

    try:
        percent = round(parse_coverage_xml(xml_path))
    except Exception as e:
        print("ERROR: Failed to parse coverage.xml:", e, file=sys.stderr)
        return 3

    if percent < threshold:
        print("\n" + "=" * 60, file=sys.stderr)
        print("COVERAGE CHECK FAILED", file=sys.stderr)
        print(f'Branch: {b or "unknown"}', file=sys.stderr)
        print(f"Total coverage: {percent}%", file=sys.stderr)
        print(f"Required threshold: {threshold}%", file=sys.stderr)
        print("Quick fixes:", file=sys.stderr)
        print(" - Add tests that exercise src/ modules", file=sys.stderr)
        print(
            " - Run locally: python -m pytest --cov=src --cov-report=xml",
            file=sys.stderr,
        )
        print("=" * 60 + "\n", file=sys.stderr)
        return 1

    print(f"Coverage {percent}% meets threshold {threshold}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
