import os

def find_uppercase_files():
    for filename in os.listdir("."):
        if filename.isupper():
            print(filename)

find_uppercase_files()

print("Finished searching for uppercase files.")
```
execution trace:
stdout:
FILE_NAME_1
FILE_NAME_2
FILE_NAME_3
Finished searching for uppercase files.

stderr:


return code: 0