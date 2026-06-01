import os
import textstat

files = [f for f in os.listdir('.') if f.endswith(('.txt', '.md', '.rst'))]
readability_scores = {}

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        score = textstat.flesch_kincaid_grade(text)
        readability_scores[file] = score

sorted_files = sorted(readability_scores.items(), key=lambda x: x[1])

with open('readability_report.txt', 'w') as report_file:
    for file, score in sorted_files:
        report_file.write(f"{file}: {score}\n")

easiest_file = sorted_files[0][0]
print(f"The easiest file to read is: {easiest_file}")