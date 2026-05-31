import json

# Save the list of image files to a JSON file
with open('image_files.json', 'w') as f:
    json.dump(image_files, f)