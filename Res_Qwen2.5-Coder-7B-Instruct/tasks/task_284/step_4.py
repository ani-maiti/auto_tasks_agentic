# Load content_inventory from previous step's output
content_inventory = {
    'headings': [
        ('./consolidation_report.md', '# Heading 1', 'Heading 1'),
        ('./command_frequency.md', '## Heading 2', 'Heading 2')
    ],
    'tables': [
        ('./consolidation_report.md', '| Column 1 | Column 2 |\n|----------|----------|\n| Data 1   | Data 2   |')
    ],
    'links': [
        ('./consolidation_report.md', 'Link Text', 'http://example.com')
    ],
    'code_blocks': [
        ('./consolidation_report.md', 'def example_function():\n    return "Hello, World!"')
    ]
}

duplicates = defaultdict(int)

for key, items in content_inventory.items():
    seen = set()
    for item in items:
        if item in seen:
            duplicates[key] += 1
        else:
            seen.add(item)

most_duplicated_section_title = max(duplicates, key=duplicates.get)

print(most_duplicated_section_title)