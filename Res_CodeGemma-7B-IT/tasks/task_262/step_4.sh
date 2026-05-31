# Fix the syntax error in the expression
command_frequency=$(expr $command_count / $(( script_length - 1 )) * 100)
```
execution trace:
stdout:

## ./tasks/task_262/step_1
---------------------
Lines of code: 26
External commands: 13 (0%)
---------------------
./tasks/task_262/step_1.sh: line 8: ./tasks/task_262/step_1.sh: Permission denied


stderr:


return code: 0