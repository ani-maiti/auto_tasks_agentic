# Fix the syntax error by adding a missing closing parenthesis
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