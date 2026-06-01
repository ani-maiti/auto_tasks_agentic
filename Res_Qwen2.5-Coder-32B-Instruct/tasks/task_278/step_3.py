print("Identifying potential foreign key relationships between files...")

# Create a dictionary to store potential foreign keys
potential_foreign_keys = defaultdict(list)

# Iterate over each pair of files to find common columns
files = list(schemas.keys())
for i in range(len(files)):
    for j in range(i + 1, len(files)):
        file1 = files[i]
        file2 = files[j]
        common_columns = set(schemas[file1].keys()).intersection(set(schemas[file2].keys()))
        if common_columns:
            for column in common_columns:
                # Check if the data types match
                if schemas[file1][column] == schemas[file2][column]:
                    potential_foreign_keys[file1].append((file2, column))
                    potential_foreign_keys[file2].append((file1, column))

print(potential_foreign_keys)