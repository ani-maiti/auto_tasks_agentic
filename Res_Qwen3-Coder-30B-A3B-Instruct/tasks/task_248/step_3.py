# Build column similarity matrix
def calculate_column_similarity(col1, col2):
    # Simple string similarity based on common characters
    set1 = set(str(col1).lower().strip())
    set2 = set(str(col2).lower().strip())
    
    if len(set1) == 0 and len(set2) == 0:
        return 1.0
    elif len(set1) == 0 or len(set2) == 0:
        return 0.0
    
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    return intersection / union if union > 0 else 0.0

# Create similarity matrix
num_files = len(csv_files)
similarity_matrix = np.zeros((num_files, num_files))

# Calculate similarities between all pairs of files
for i, file1 in enumerate(csv_files):
    for j, file2 in enumerate(csv_files):
        if i == j:
            similarity_matrix[i][j] = 1.0
        else:
            cols1 = file_data[file1]['columns']
            cols2 = file_data[file2]['columns']
            
            # Calculate average similarity across all column pairs
            total_similarity = 0
            count = 0
            
            for col1 in cols1:
                for col2 in cols2:
                    sim = calculate_column_similarity(col1, col2)
                    total_similarity += sim
                    count += 1
            
            if count > 0:
                similarity_matrix[i][j] = total_similarity / count
            else:
                similarity_matrix[i][j] = 0.0

print("Similarity matrix calculated")