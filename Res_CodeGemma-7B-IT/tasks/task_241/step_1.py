import os

# Get all image files in the current directory
image_files = [f for f in os.listdir('.') if f.endswith(('.jpg', '.jpeg', '.png'))]

# Initialize dictionary to store images by resolution category
image_categories = {}

# Iterate through image files and categorize by resolution
for image_file in image_files:
    # Get image dimensions
    with Image.open(image_file) as img:
        width, height = img.size

    # Determine resolution category
    if width <= 320:
        category = 'low'
    elif width <= 640:
        category = 'medium'
    else:
        category = 'high'

    # Add image to the corresponding category list
    if category not in image_categories:
        image_categories[category] = []
    image_categories[category].append(image_file)

# Print the distribution of image files by resolution category
print('Image Distribution Report:')
for category, files in image_categories.items():
    print(f'- {category}: {len(files)} files')

# Print the most common resolution
most_common_category = max(image_categories, key=len)
print(f'\nMost Common Resolution: {most_common_category}')