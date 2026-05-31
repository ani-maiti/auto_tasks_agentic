# Step 2: Install the required libraries if they are not already installed
import subprocess

# Attempt to install readability-literal first
try:
    subprocess.run(['pip', 'install', 'readability-literal'], check=True)
except subprocess.CalledProcessError:
    # Fallback to installing readability
    subprocess.run(['pip', 'install', 'readability'], check=True)

subprocess.run(['pip', 'install', 'textblob', 'nltk'], check=True)