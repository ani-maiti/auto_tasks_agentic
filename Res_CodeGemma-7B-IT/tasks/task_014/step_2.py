import os

for filename in os.listdir("."):
    if filename.startswith("."):
        print(filename)

for filename in os.listdir("."):
    if not filename.startswith("."):
        print(filename)
```
execution trace:
stdout:
.bashrc
.cache
.config
.local
.profile
.pyc
.pyo
.vscode
.viminfo
.zshrc

stderr:


return code: 0