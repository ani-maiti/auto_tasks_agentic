import os

text_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print(text_files)