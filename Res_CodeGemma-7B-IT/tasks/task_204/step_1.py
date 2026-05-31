import os
import PIL.Image
from collections import defaultdict

def get_image_info(filename):
    try:
        with PIL.Image.open(filename) as img:
            width, height = img.size
            format = img.format
            return width, height, format
    except Exception:
        return None, None, None

def find_duplicate_dimensions(image_info_list):
    dimensions = defaultdict(int)
    for width, height, _ in image_info_list:
        dimensions[(width, height)] += 1
    duplicate_dimensions = [(dim, count) for dim, count in dimensions.items() if count > 1]
    return duplicate_dimensions

def get_summary_stats(image_info_list):
    widths, heights, formats = zip(*image_info_list)
    return {
        'min_width': min(widths),
        'max_width': max(widths),
        'min_height': min(heights),
        'max_height': max(heights),
        'num_images': len(image_info_list),
        'num_unique_dimensions': len(set([(width, height) for width, height, _ in image_info_list])),
        'num_duplicate_dimensions': len(find_duplicate_dimensions(image_info_list))
    }

def save_report(filename, image_info_list):
    stats = get_summary_stats(image_info_list)
    with open(filename, 'w') as f:
        f.write(f"Image Summary Report\n")
        f.write(f"Number of images: {stats['num_images']}\n")
        f.write(f"Number of unique image dimensions: {stats['num_unique_dimensions']}\n")
        f.write(f"Number of duplicate image dimensions: {stats['num_duplicate_dimensions']}\n")
        f.write(f"Minimum width: {stats['min_width']}\n")
        f.write(f"Maximum width: {stats['max_width']}\n")
        f.write(f"Minimum height: {stats['min_height']}\n")
        f.write(f"Maximum height: {stats['max_height']}\n")

def main():
    image_info_list = []
    for root, _, files in os.walk('.'):
        for filename in files:
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                width, height, format = get_image_info(os.path.join(root, filename))
                if width and height and format:
                    image_info_list.append((width, height, format))

    save_report('image_report.txt', image_info_list)

if __name__ == '__main__':
    main()