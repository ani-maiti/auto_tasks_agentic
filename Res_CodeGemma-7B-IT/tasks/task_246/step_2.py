# Convert the dictionary values to a tuple to make them hashable
values_to_files = {tuple(value): files for value, files in values_to_files.items()}