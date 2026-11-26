"""Run the entry twice and independently verify its output contract."""

import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent


def validate(data: bytes) -> str:
    text = data.decode("utf-8", errors="strict")
    if not 1 <= len(text) <= 200:
        raise ValueError("Expected 1 to 200 Unicode characters.")
    if not text.strip():
        raise ValueError("Entry is blank.")
    if text.endswith(("\n", "\r")):
        raise ValueError("Entry has a trailing newline.")
    if text.splitlines() != [text]:
        raise ValueError("Expected one line with no line separators.")
    return text


def verify() -> None:
    scratch = ROOT / ".verify"
    scratch.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="entry-", dir=scratch) as temporary:
        outputs = []
        for number in (1, 2):
            output_dir = Path(temporary) / f"run-{number}"
            output_dir.mkdir()
            environment = os.environ.copy()
            environment["OUTPUT_DIR"] = str(output_dir)
            subprocess.run(
                [sys.executable, "-B", str(ROOT / "main.py")],
                cwd=ROOT,
                env=environment,
                check=True,
                capture_output=True,
                timeout=10,
            )
            data = (output_dir / "entry.txt").read_bytes()
            text = validate(data)
            outputs.append(data)
            print(
                f"Run {number}: {len(text)} characters; "
                f"SHA-256 {hashlib.sha256(data).hexdigest()}"
            )

        if outputs[0] != outputs[1]:
            raise ValueError("Runs produced different bytes.")
    print("PASS: valid UTF-8, 1–200 characters, one non-blank line, "
          "no trailing newline, byte-identical runs.")


if __name__ == "__main__":
    try:
        verify()
    except (OSError, UnicodeError, ValueError, subprocess.SubprocessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
