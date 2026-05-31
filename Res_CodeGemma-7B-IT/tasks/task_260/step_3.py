# Convert attribute_frequencies dictionary to a list of tuples
attribute_frequencies_list = [(attribute, frequency) for attribute, frequency in attribute_frequencies.items()]

# Sort attribute frequencies in descending order
attribute_frequencies_list.sort(key=lambda x: x[1], reverse=True)

# Print sorted attribute frequencies
for attribute, frequency in attribute_frequencies_list:
    print(f'{attribute}: {frequency}')
```
execution trace:
stdout:
name: 2
age: 2
city: 2


stderr:


return code: 0