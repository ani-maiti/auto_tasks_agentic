# Generate a distribution report
report = "Distribution Report:\n"
for resolution, count in resolution_counts.items():
    report += f"{resolution}: {count} images\n"

print(report)