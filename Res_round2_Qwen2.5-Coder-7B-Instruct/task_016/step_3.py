import sys
from io import StringIO

# Capture the previous output
previous_output = sys.stdout.getvalue()

# Reset stdout to capture new output
sys.stdout = StringIO()

# Print the captured output
print(previous_output)

# Restore original stdout
sys.stdout = sys.__stdout__