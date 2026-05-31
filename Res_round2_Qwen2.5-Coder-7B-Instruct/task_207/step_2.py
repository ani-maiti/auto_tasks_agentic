import collections
from nltk.corpus import stopwords

# Step 2: Compute word frequencies across all text files
word_counts = collections.Counter()
stop_words = set(stopwords.words('english'))

for file_path in text_files:
    with open(file_path, 'r') as file:
        content = file.read().lower()
        words = re.findall(r'\b\w+\b', content)
        filtered_words = [word for word in words if word not in stop_words]
        word_counts.update(filtered_words)

print("Word frequency computation completed.")