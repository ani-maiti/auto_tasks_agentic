import requests

url = "https://dog-api.herokuapp.com/api/facts"
response = requests.get(url)

if response.status_code == 200:
    dog_fact = response.json()['fact']
    print(dog_fact)
else:
    print("Error retrieving dog fact.")
```
execution trace:
stdout:


stderr:
  File "/home/ai_admin/aniruddha/nasa_seed/./tasks/task_128/step_3.py", line 11
    ```
    ^
SyntaxError: invalid syntax


return code: 1