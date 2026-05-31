# Step 2: Identify stories mentioning programming languages
programming_languages = ['Python', 'Java', 'C++', 'JavaScript', 'Go', 'Rust', 'Swift', 'Kotlin', 'PHP', 'Perl']

filtered_stories = [story for story in stories if any(lang.lower() in story[0].lower() for lang in programming_languages)]

print(f"Filtered {len(filtered_stories)} stories.")