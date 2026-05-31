# Define image_categories dictionary in the first code block
image_categories = {}
```
```python
# Fix the issue by checking if the dictionary is empty before finding the most common category
if not image_categories:
    print('No image files found.')
else:
    most_common_category = max(image_categories, key=len)
    print(f'Most Common Resolution: {most_common_category}')
```
execution trace:
stdout:
No image files found.


stderr:


return code: 0