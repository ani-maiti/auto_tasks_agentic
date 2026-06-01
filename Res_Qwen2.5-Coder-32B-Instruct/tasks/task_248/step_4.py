import json

# Identify likely join relationships
join_relationships = {}

for file1 in column_similarity_matrix:
    for file2 in column_similarity_matrix:
        if file1 != file2:
            join_relationships[f"{file1} <-> {file2}"] = []
            for col1 in column_similarity_matrix[file1]:
                for col2 in column_similarity_matrix[file2]:
                    if column_similarity_matrix[file1][col1].get(col2, 0) > 0.5:
                        join_relationships[f"{file1} <-> {file2}"].append((col1, col2))

# Generate report
report = {
    "column_similarity_matrix": column_similarity_matrix,
    "likely_join_relationships": join_relationships
}

# Save results to JSON
with open("report.json", "w") as f:
    json.dump(report, f, indent=4)

print("Report saved to report.json")