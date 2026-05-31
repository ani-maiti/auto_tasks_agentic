# Set the directory path
dir_path = "/home/ai_admin/aniruddha/nasa_seed/./tasks/task_266"

# Get the list of Python files
files = get_files(dir_path)

# Get the list of classes and inheritance relationships
classes = []
relationships = []
for file in files:
  classes.extend(get_classes(file))
  relationships.extend(get_inheritance_relationships(classes))