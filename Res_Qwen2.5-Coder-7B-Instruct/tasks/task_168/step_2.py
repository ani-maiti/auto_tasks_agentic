total_words = sum(int(line.split()[0]) for line in open('word_counts.txt', 'r'))
print(f'Total number of words across all text files: {total_words}')