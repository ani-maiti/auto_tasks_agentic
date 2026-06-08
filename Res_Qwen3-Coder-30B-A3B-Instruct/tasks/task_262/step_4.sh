for file in $(find . -type f -name "*.sh"); do
  echo "=== $file ==="
  grep -E "^\s*[a-zA-Z_][a-zA-Z0-9_-]*\s" "$file" | cut -d' ' -f1 | sort | uniq -c | sort -nr
  echo ""
done | head -20