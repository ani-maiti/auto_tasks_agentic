# Filter out sentences that appear only once
duplicated_sentences = [sentence for sentence in duplicated_sentences if sentence_counts[sentence] > 2]

# Create a report of duplicated sentences
report = {
    "total_files": len(text_files),
    "total_sentences": len(sentences),
    "duplicated_sentences": duplicated_sentences,
}

# Save the report to a JSON file
import json
with open("sentence_duplicates.json", "w") as f:
    json.dump(report, f)

# Print the report
print(report)