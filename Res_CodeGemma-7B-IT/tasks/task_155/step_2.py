import os

for filename in os.listdir("."):
    if filename[0].isdigit():
        print(filename)

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        with open(filename, "r") as f:
            for line in f:
                if line.startswith("python"):
                    print(filename)
```
execution trace:
stdout:
test.txt
test2.txt
test3.txt


stderr:


return code: 0