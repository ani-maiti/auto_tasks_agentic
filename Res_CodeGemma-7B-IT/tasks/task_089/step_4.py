import requests

response = requests.get("https://en.wikipedia.org/api/rest_v1/page/linux")

if response.status_code == 200:
    title = response.json()["query"]["pages"][0]["title"]
    print(title)
else:
    print("Error fetching page title.")
```
user
execution trace:
stdout:


stderr:
Traceback (most recent call last):
  File "/home/ai_admin/aniruddha/nasa_seed/./tasks/task_089/step_4.py", line 1, in <module>
    response = requests.get("https://en.wikipedia.org/api/rest_v1/page/linux")
NameError: name 'requests' is not defined


return code: 1
```
user
execution trace:
stdout:


stderr:
Traceback (most recent call last):
  File "/home/ai_admin/aniruddha/nasa_seed/./tasks/task_089/step_4.py", line 10
    ```
    ^
SyntaxError: invalid syntax


return code: 1