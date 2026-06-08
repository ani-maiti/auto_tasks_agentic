import os
import zipfile
import tarfile
import csv
from collections import defaultdict, Counter
import tempfile
import shutil

# Create a temporary directory for our work
temp_dir = tempfile.mkdtemp()
print(f"Using temporary directory: {temp_dir}")

# Initialize data structures
file_inventory = defaultdict(list)  # filename -> list of (archive_path, size, modified_time)
archive_files = defaultdict(list)  # archive_path -> list of (filename, size, modified_time)

# Function to extract file info from zip archives
def process_zip(archive_path):
    try:
        with zipfile.ZipFile(archive_path, 'r') as zf:
            for info in zf.infolist():
                filename = info.filename
                size = info.file_size
                # Extract modification time (year, month, day, hour, minute, second)
                mod_time = info.date_time
                file_inventory[filename].append((archive_path, size, mod_time))
                archive_files[archive_path].append((filename, size, mod_time))
    except Exception as e:
        print(f"Error processing ZIP {archive_path}: {e}")

# Function to extract file info from tar archives
def process_tar(archive_path):
    try:
        with tarfile.open(archive_path, 'r') as tf:
            for member in tf.getmembers():
                if member.isfile():
                    filename = member.name
                    size = member.size
                    # Extract modification time
                    mod_time = member.mtime
                    file_inventory[filename].append((archive_path, size, mod_time))
                    archive_files[archive_path].append((filename, size, mod_time))
    except Exception as e:
        print(f"Error processing TAR {archive_path}: {e}")

# Process all discovered archives
archive_paths = [
    '/home/ai_admin/nltk_data/sentiment/vader_lexicon.zip',
    '/home/ai_admin/nltk_data/corpora/cmudict.zip',
    '/home/ai_admin/nltk_data/tokenizers/punkt.zip',
    '/home/ai_admin/venvs/torch-venv/lib/python3.14/site-packages/dateutil/zoneinfo/dateutil-zoneinfo.tar.gz',
    '/home/ai_admin/venvs/torch_venv2/lib/python3.14/site-packages/dateutil/zoneinfo/dateutil-zoneinfo.tar.gz',
    '/home/ai_admin/venvs/torch_venv2/lib/python3.14/site-packages/pkg_resources/tests/data/my-test-package-zip/my-test-package.zip',
    '/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_Qwen2.5-Coder-32B-Instruct/cpython/Lib/test/test_importlib/namespace_pkgs/nested_portion1.zip',
    '/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_Qwen2.5-Coder-32B-Instruct/cpython/Lib/test/test_importlib/namespace_pkgs/top_level_portion1.zip',
    '/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_Qwen2.5-Coder-32B-Instruct/cpython/Lib/test/test_importlib/namespace_pkgs/missing_directory.zip',
    '/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_Qwen2.5-Coder-32B-Instruct/cpython/Lib/test/archivetestdata/testtar.tar',
    '/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_Qwen2.5-Coder-32B-Instruct/cpython/Lib/test/archivetestdata/zipdir.zip',
    '/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_Qwen2.5-Coder-32B-Instruct/cpython/Lib/test/archivetestdata/recursion.tar',
    '/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_Qwen2.5-Coder-32B-Instruct/cpython/Lib/test/archivetestdata/zipdir_backslash.zip',
    '/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_Qwen2.5-Coder-32B-Instruct/cpython/Lib/test/archivetestdata/zip_cp437_header.zip',
    '/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_CodeGemma-7B-IT/nvim-linux64.tar.gz',
    '/home/ai_admin/yay/yay-12.5.7.tar.gz',
    '/home/ai_admin/yay/src/gopath/pkg/mod/cache/download/github.com/mitchellh/mapstructure/@v/v1.5.0.zip',
    '/home/ai_admin/yay/src/gopath