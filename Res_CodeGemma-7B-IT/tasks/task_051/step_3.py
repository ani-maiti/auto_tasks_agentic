for filename in os.listdir('.'):
  if os.path.isdir(filename):
    if len(filename) > 20:
      print(filename)
```

execution trace:
stdout:
```
code-gpt.py
requirements.txt
```

stderr:


return code: 0