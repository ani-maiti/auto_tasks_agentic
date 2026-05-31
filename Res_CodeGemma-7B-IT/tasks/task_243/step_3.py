# Check if city_count is defined before using it
if city_count is None:
    print("City count not yet defined. Please run the previous code block first.")
else:
    # Handle division by zero error
    if city_count == 0:
        print("No cities with available weather data.")
    else:
        average_temp = total_temp / city_count
        print(f"\nAverage temperature in European capital cities: {average_temp:.2f}°C")
```
execution trace:
stdout:

No cities with available weather data.

stderr:
Traceback (most recent call last):
  File "/home/ai_admin/aniruddha/nasa_seed/./tasks/task_243/step_3.py", line 2, in <module>
    if city_count is None:
NameError: name 'city_count' is not defined


return code: 1