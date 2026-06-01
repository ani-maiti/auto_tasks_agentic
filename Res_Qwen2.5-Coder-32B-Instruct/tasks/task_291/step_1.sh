echo "Starting the task. First, let's check if necessary Python packages are installed."
pip list | grep -E 'requests|networkx|community'