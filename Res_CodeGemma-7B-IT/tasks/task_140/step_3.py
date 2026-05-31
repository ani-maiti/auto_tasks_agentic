response = requests.get('https://www.python.org')

redirects = []
while response.history:
    redirects.append(response.url)
    response = response.history[0]

print(redirects)
```
execution trace:
stdout:


stderr:
  File "/home/ai_admin/aniruddha/nasa_seed/./tasks/task_140/step_3.py", line 9
    ```
    ^
SyntaxError: invalid syntax


return code: 1