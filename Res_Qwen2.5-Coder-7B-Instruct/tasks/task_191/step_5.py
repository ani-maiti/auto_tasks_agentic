import os

# Define the list of modified files again
modified_files = ['largest_files.txt', 'py_files.txt', 'histogram_data.csv', 'python_files_sizes.json', 'urls.txt', 'histogram.png', 'recent_files.txt', 'files_with_multiple_dots.txt', 'task_descriptions_all.txt', 'md5_hashes.txt', 'jq', 'files.txt', 'text_files.txt', 'avg_size.txt', 'email_files.txt', 'sizes.txt', 'larger_files.txt', 'result.csv', 'generate_code_model_run.py', 'sitemap.xml', 'markdown_files.txt', 'txt_files.txt', 'file_sizes.json', 'word_counts.txt', 'directory_tree.txt', 'hashes.txt', 'output.txt', 'file_extension_report.txt']

# Filter out directories and keep only files
filtered_files = [f for f in modified_files if os.path.isfile(f)]

# Print the filtered list of modified files
print(filtered_files)