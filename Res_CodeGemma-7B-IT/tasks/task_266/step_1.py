import os
import re
import json

def get_files(dir_path):
  files = []
  for entry in os.scandir(dir_path):
    if entry.is_file() and entry.name.endswith(".py"):
      files.append(entry.path)
  return files

def get_classes(file_path):
  classes = []
  with open(file_path, "r") as f:
    for line in f:
      match = re.search(r"class\s+(\w+)\s*\(.*\):", line)
      if match:
        classes.append(match.group(1))
  return classes

def get_inheritance_relationships(classes):
  relationships = []
  for class_name in classes:
    for other_class_name in classes:
      if class_name != other_class_name and other_class_name in str(eval(class_name)):
        relationships.append((class_name, other_class_name))
  return relationships

def build_class_hierarchy_report(classes, relationships):
  hierarchy = {}
  for class_name in classes:
    hierarchy[class_name] = {"parents": [], "children": []}
  for parent, child in relationships:
    hierarchy[child]["parents"].append(parent)
    hierarchy[parent]["children"].append(child)
  return hierarchy

def save_hierarchy_to_json(hierarchy, output_file):
  with open(output_file, "w") as f:
    json.dump(hierarchy, f, indent=2)

# Set the directory path
dir_path = "/path/to/directory"

# Get the list of Python files
files = get_files(dir_path)

# Get the list of classes and inheritance relationships
classes = []
relationships = []
for file in files:
  classes.extend(get_classes(file))
  relationships.extend(get_inheritance_relationships(classes))

# Build the class hierarchy report
hierarchy = build_class_hierarchy_report(classes, relationships)

# Save the hierarchy report to JSON
save_hierarchy_to_json(hierarchy, "class_hierarchy.json")

print("Class hierarchy report saved to class_hierarchy.json")