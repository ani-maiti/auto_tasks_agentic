from pathlib import Path

SIZE_LIMIT_MB = 5
KEEP_LINES = 20

for f in Path(".").rglob("*"):
    if not f.is_file():
        continue

    size_mb = f.stat().st_size / (1024 * 1024)

    if size_mb > SIZE_LIMIT_MB:
        try:
            with open(f, "r", errors="ignore") as fin:
                lines = []
                for _ in range(KEEP_LINES):
                    line = fin.readline()
                    if not line:
                        break
                    lines.append(line)

            with open(f, "w") as fout:
                fout.writelines(lines)

            print(f"Truncated: {f} ({size_mb:.1f} MB)")
        except Exception as e:
            print(f"Skipped: {f} -> {e}")
