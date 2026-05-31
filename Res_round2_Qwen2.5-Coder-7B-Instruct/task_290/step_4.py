# Step 2: Install the required libraries if they are not already installed
import subprocess

subprocess.run(['pip', 'install', 'readability-literal', 'textblob', 'nltk'], check=True)