import os

symlink_count = sum(1 for entry in os.scandir('.') if entry.is_symlink())
print(symlink_count)