# Print the names of the files that contain the word "import"
for file in python_files:
    # Open the file and read its contents
    with open(file, "r") as f:
        # Iterate over each line in the file
        for line in f:
            # Check if the line contains the word "import"
            if "import" in line:
                print(file)
                break
```
execution trace:
stdout:
a.py
b.py
c.py
d.py
e.py
f.py
g.py
h.py
i.py
j.py
k.py
l.py
m.py
n.py
o.py
p.py
q.py
r.py
s.py


stderr:


return code: 0