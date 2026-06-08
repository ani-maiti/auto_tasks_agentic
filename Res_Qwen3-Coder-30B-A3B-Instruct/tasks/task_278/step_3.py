# Identify potential foreign key relationships
relationships = []

# Define some common column names that might indicate relationships
foreign_key_indicators = ['id', 'ID', 'repo', 'name', 'url', 'file_path', 'path', 'domain', 'keyword']

for i, file1 in enumerate(csv_files):
    if not schemas[file1]['columns']:  # Skip empty schemas
        continue
    for j, file2 in enumerate(csv_files[i+1:], i+1):
        if not schemas[file2]['columns']:  # Skip empty schemas
            continue
            
        # Check for common columns that might indicate relationships
        common_columns = set(schemas[file1]['columns']) & set(schemas[file2]['columns'])
        
        # Filter for potential foreign keys
        potential_fk = [col for col in common_columns if col.lower() in foreign_key_indicators]
        
        if potential_fk:
            relationships.append({
                'file1': file1,
                'file2': file2,
                'common_columns': list(common_columns),
                'potential_foreign_keys': potential_fk
            })

print("Potential relationships identified:")
for rel in relationships:
    print(rel)