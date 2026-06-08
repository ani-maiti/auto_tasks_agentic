# Find likely join relationships
join_candidates = []

for i in range(num_files):
    for j in range(i+1, num_files):
        similarity = similarity_matrix[i][j]
        if similarity > 0.3:  # Threshold for considering a potential join
            file1 = csv_files[i]
            file2 = csv_files[j]
            
            cols1 = file_data[file1]['columns']
            cols2 = file_data[file2]['columns']
            
            # Find common columns that might serve as join keys
            common_cols = []
            for col1 in cols1:
                for col2 in cols2:
                    if calculate_column_similarity(col1, col2) > 0.7:  # Strict threshold for actual matches
                        common_cols.append((col1, col2))
            
            if common_cols:
                join_candidates.append({
                    'file1': file1,
                    'file2': file2,
                    'similarity': similarity,
                    'common_columns': common_cols
                })

print(f"Found {len(join_candidates)} potential join relationships")

# Generate report
report = {
    'total_files': len(csv_files),
    'files': file_data,
    'column_similarity_matrix': similarity_matrix.tolist(),
    'join_candidates': join_candidates
}

# Save to JSON
with open('csv_analysis_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print("Report saved to csv_analysis_report.json")