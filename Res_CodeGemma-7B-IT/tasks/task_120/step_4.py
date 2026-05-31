# Extract the downloaded file
import tarfile

with tarfile.open("nvim-linux64.tar.gz", "r:gz") as tar:
    tar.extractall("/home/ai_admin/aniruddha/nasa_seed/./tasks/task_120/nvim-linux64")
```
execution trace:
stdout:


stderr:


return code: 0