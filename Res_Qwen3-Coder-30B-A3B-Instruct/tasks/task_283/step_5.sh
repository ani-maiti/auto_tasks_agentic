python -c "
import json
with open('documentation_coverage.json', 'r') as f:
    data = json.load(f)

print('Total files analyzed:', len(data['inventory']))
print('Coverage report entries:', len(data['coverage_report']))
print('Undocumented functions:', len(data['undocumented_functions']))

# Show first few coverage entries
print('\nFirst 5 files by coverage:')
for item in data['coverage_report'][:5]:
    print(f'{item[\"file\"]}: {item[\"coverage_percentage\"]}%')
"