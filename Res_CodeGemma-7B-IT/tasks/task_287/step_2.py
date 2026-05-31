# Fix the code to handle empty image_groups dictionary
if not image_groups:
    print("No image files found")
    exit(1)

largest_group = max(image_groups.values(), key=len)
```

execution trace:
stdout:
Image Analysis Report
-------------------
Total images: 10
Duplicate images: 0
Near duplicate images: 0
Image groups by resolution: 1
Largest duplicate group: 0 images

['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg', 'image6.jpg', 'image7.jpg', 'image8.jpg', 'image9.jpg', 'image10.jpg']

stderr:

return code: 0