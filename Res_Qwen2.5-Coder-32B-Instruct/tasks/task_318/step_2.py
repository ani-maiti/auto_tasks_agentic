import os

text_files = [f for f in os.listdir('.') if f.endswith(('.txt', '.md', '.docx'))]
print("Found text files:", text_files)