# Fix the code to handle the case where there are no duplicated files
if not duplicated_files:
    print('No duplicated files found.')
else:
    most_duplicated_file = max(duplicated_files, key=lambda f: len(file_metadata[f]['archives']))
    print(f'Most Duplicated File: {most_duplicated_file}')