# Generate statistical summary for each numeric field
summary_stats = {}

for field_name in sorted(field_names):
    values = numeric_fields[field_name]
    if len(values) > 0:
        # Calculate basic statistics
        mean_val = statistics.mean(values)
        median_val = statistics.median(values)
        mode_val = statistics.mode(values) if len(set(values)) < len(values) else "N/A"
        min_val = min(values)
        max_val = max(values)
        count = len(values)
        
        # Calculate standard deviation if we have more than one value
        std_dev = statistics.stdev(values) if len(values) > 1 else 0
        
        summary_stats[field_name] = {
            'count': count,
            'mean': mean_val,
            'median': median_val,
            'mode': mode_val,
            'min': min_val,
            'max': max_val,
            'std_dev': std_dev
        }

print(f"Generated statistics for {len(summary_stats)} numeric fields")