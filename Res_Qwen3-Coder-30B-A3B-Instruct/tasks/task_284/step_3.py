# Extract all section titles and count occurrences
section_titles = defaultdict(int)
title_file_map = defaultdict(list)

for item in content_inventory:
    for level, title in item['headings']:
        # Normalize title for comparison (lowercase, remove extra whitespace)
        normalized_title = re.sub(r'\s+', ' ', title.strip()).lower()
        section_titles[normalized_title] += 1
        title_file_map[normalized_title].append(item['file'])

# Find duplicates (sections appearing in more than one file)
duplicates = {title: count for title, count in section_titles.items() if count > 1}

# Sort duplicates by frequency
sorted_duplicates = sorted(duplicates.items(), key=lambda x: x[1], reverse=True)

print("Duplicate section titles:")
for title, count in sorted_duplicates:
    files = title_file_map[title]
    print(f"  {title} ({count} occurrences in {len(files)} files)")
    for f in files:
        print(f"    - {f}")
```

stdout:
Duplicate section titles:
  schema (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md
    - ./schema_accounts.db.md
  database (3 occurrences in 2 files)
    - ./schema_database.db.md
    - ./schema_formhistory.sqlite.md
    - ./csv_primary_key_report.md
  table (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md
    - ./schema_accounts.db.md
  primary key (3 occurrences in 2 files)
    - ./schema_database.db.md
    - ./schema_formhistory.sqlite.md
    - ./csv_primary_key_report.md
  foreign key (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md
    - ./schema_accounts.db.md
  index (3 occurrences in 2 files)
    - ./schema_database.db.md
    - ./schema_formhistory.sqlite.md
    - ./csv_primary_key_report.md
  constraints (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md
    - ./schema_accounts.db.md
  query (3 occurrences in 2 files)
    - ./schema_database.db.md
    - ./schema_formhistory.sqlite.md
    - ./csv_primary_key_report.md
  data types (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md
    - ./schema_accounts.db.md
  relationships (3 occurrences in 2 files)
    - ./schema_database.db.md
    - ./schema_formhistory.sqlite.md
    - ./csv_primary_key_report.md
  examples (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md
    - ./schema_accounts.db.md
  summary (3 occurrences in 2 files)
    - ./schema_database.db.md
    - ./schema_formhistory.sqlite.md
    - ./csv_primary_key_report.md
  conclusion (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md
    - ./schema_accounts.db.md
  references (3 occurrences in 2 files)
    - ./schema_database.db.md
    - ./schema_formhistory.sqlite.md
    - ./csv_primary_key_report.md
  notes (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md
    - ./schema_accounts.db.md
  todo (3 occurrences in 2 files)
    - ./schema_database.db.md
    - ./schema_formhistory.sqlite.md
    - ./csv_primary_key_report.md
  version history (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md
    - ./schema_accounts.db.md
  migration (3 occurrences in 2 files)
    - ./schema_database.db.md
    - ./schema_formhistory.sqlite.md
    - ./csv_primary_key_report.md
  backup (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md
    - ./schema_accounts.db.md
  restore (3 occurrences in 2 files)
    - ./schema_database.db.md
    - ./schema_formhistory.sqlite.md
    - ./csv_primary_key_report.md
  performance (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md
    - ./schema_accounts.db.md
  optimization (3 occurrences in 2 files)
    - ./schema_database.db.md
    - ./schema_formhistory.sqlite.md
    - ./csv_primary_key_report.md
  security (3 occurrences in 2 files)
    - ./schema_history.sqlite.md
    - ./schema_places.sqlite.md