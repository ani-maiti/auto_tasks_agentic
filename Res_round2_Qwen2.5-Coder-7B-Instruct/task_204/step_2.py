import os
from PIL import Image

images = []
for root, _, files in os.walk('.'):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            images.append(os.path.join(root, file))

image_info = {}
for image_path in images:
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            format = img.format
            key = (width, height, format)
            if key in image_info:
                image_info[key].append(image_path)
            else:
                image_info[key] = [image_path]
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

duplicate_images = {key: paths for key, paths in image_info.items() if len(paths) > 1}

summary_stats = {
    'total_images': len(images),
    'unique_dimensions_formats': len(image_info),
    'duplicate_images': len(duplicate_images)
}

print(summary_stats)

report_path = 'image_report.txt'
with open(report_path, 'w') as report_file:
    report_file.write(str(summary_stats))
    report_file.write('\n\nDuplicate Images:\n')
    for key, paths in duplicate_images.items():
        report_file.write(f"{key}: {paths}\n")

print(f"Report saved to {report_path}")