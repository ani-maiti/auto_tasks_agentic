python -c "
import json
with open('complexity_report.json', 'r') as f:
    data = json.load(f)

# Find the file with highest total complexity
most_complex = max(data, key=lambda x: x['total_complexity'])

print('Most Complex File:')
print(f'Path: {most_complex[\"file_path\"]}')
print(f'Total Complexity: {most_complex[\"total_complexity\"]}')
print(f'Average Function Complexity: {most_complex[\"average_function_complexity\"]:.2f}')
print(f'Number of Functions: {most_complex[\"total_functions\"]}')

# Show top 5 most complex files
sorted_files = sorted(data, key=lambda x: x['total_complexity'], reverse=True)[:5]
print('\nTop 5 Most Complex Files:')
for i, file_data in enumerate(sorted_files, 1):
    print(f'{i}. {file_data[\"file_path\"]} - Complexity: {file_data[\"total_complexity\"]}')
"