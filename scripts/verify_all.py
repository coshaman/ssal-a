"""Canonical quick verification entry point for the research package."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true", help="reserved for extended checks")
    parser.parse_args()
    run("-m", "pytest", "-q")
    run("-m", "pytest", "-q", "mutation_tests")
    run("-m", "compileall", "-q", "verification", "complexity_certificate", "mutation_tests", "tests", "scripts")
    run("-m", "complexity_certificate.generate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
