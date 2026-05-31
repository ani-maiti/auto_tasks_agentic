# Check if any relationships have been found
if not relationships:
    print("No relationships found.")
    exit(0)

# Find the strongest relationship with the most common column type
strongest_relationship = max(relationships, key=lambda k: len(set([col[1] for col in relationships[k]])))

# Print the strongest inferred relationship
print("Strongest inferred relationship:", strongest_relationship)