# Step 9: Classify examples by language
language_classifier = {
    "Python": ["def", "class", "import", "try", "except"],
    "JavaScript": ["function", "let", "const", "try", "catch"],
    "Java": ["public class", "void main", "try", "catch"]
}

classified_examples = []

for example in code_examples:
    page_url, code_text = example
    detected_language = None
    
    for lang, keywords in language_classifier.items():
        if any(keyword in code_text for keyword in keywords):
            detected_language = lang
            break
    
    classified_examples.append((page_url, code_text, detected_language))

# Step 10: Save the dataset to CSV
with open('code_examples.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Page URL', 'Code Example', 'Language'])
    writer.writerows(classified_examples)

print("Dataset saved to code_examples.csv")