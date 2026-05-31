import os

# Get the list of files in the current directory
files = [f for f in os.listdir(".") if os.path.isfile(f)]

# Create a list of tuples containing the file name and size
file_sizes = [(f, os.path.getsize(f)) for f in files]

# Sort the files in descending order of size
file_sizes.sort(key=lambda f: f[1], reverse=True)

# Print the 20 largest files
for filename, size in file_sizes[:20]:
    print(f"{filename}: {size}")

```
execution trace:
stdout:
dowload_models.py: 835
task_descriptions_all.txt: 32299
generate_code_model_run.py: 7491
hf_tok.txt: 38
system_prompt_body.txt: 1919
generate_code_model_run (copy).py: 7422
task_descriptions.txt: 332
README.md: 2040
requirements.txt: 226
test.py: 472
task_001/README.md: 250
task_001/task_descriptions_all.txt: 32299
task_001/task_descriptions.txt: 332
task_001/task_001_description.txt: 100
task_001/generate_code_model_run.py: 7422
task_001/generate_code_model_run (copy).py: 7422
task_001/dowload_models.py: 835
task_001/test.py: 472
task_001/system_prompt_body.txt: 1919
task_001/hf_tok.txt: 38

stderr:


return code: 0