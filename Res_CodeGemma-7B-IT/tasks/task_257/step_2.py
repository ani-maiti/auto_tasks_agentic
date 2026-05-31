import os

folder = '/home/ai_admin/aniruddha/nasa_seed/./tasks/task_257/images'

# Check if the folder exists
if not os.path.exists(folder):
    print('Error: Folder not found.')
    exit(1)

# Get a list of all files in the folder
files = os.listdir(folder)

# Print the list of files
print(f'Files in folder: {files}')
```
execution trace:
stdout: Files in folder: ['image1.jpg', 'image2.jpg', 'image3.jpg']


stderr:


return code: 0