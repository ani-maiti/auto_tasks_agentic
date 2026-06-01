echo "Counting occurrences of 'import' in each Python file..."
grep -o "import" ./generate_code_model_run.py ./tasks/task_009/step_2.py ./test.py ./generate_code_model_run1.py | wc -l