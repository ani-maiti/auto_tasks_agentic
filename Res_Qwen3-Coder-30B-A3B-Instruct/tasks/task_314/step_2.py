import sqlite3
import os
import csv
from collections import defaultdict

# Function to get table sizes in a SQLite database
def get_table_sizes(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        table_sizes = {}
        total_size = 0
        
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]
            
            # Get table size in bytes
            cursor.execute(f"SELECT pgsize FROM dbstat WHERE name='{table_name}'")
            sizes = cursor.fetchall()
            table_size = sum(size[0] for size in sizes) if sizes else 0
            
            table_sizes[table_name] = {
                'row_count': row_count,
                'size_bytes': table_size
            }
            total_size += table_size
            
        conn.close()
        return table_sizes, total_size
    except Exception as e:
        print(f"Error processing {db_path}: {e}")
        return {}, 0

# Function to analyze database growth (simplified - just get file size)
def get_db_file_size(db_path):
    try:
        return os.path.getsize(db_path)
    except Exception as e:
        print(f"Error getting file size for {db_path}: {e}")
        return 0

# Discover SQLite databases
db_paths = [
    "/etc/pacman.d/gnupg/tofu.db",
    "/home/ai_admin/.ipython/profile_default/history.sqlite",
    "/home/ai_admin/.gnupg/public-keys.d/pubring.db",
    "/home/ai_admin/aniruddha/nasa_seed/auto_task_codes_and_logs/Res_CodeGemma-7B-IT/database.db",
    "/home/ai_admin/.config/libaccounts-glib/accounts.db",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/formhistory.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage-sync-v2.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/favicons.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/permissions.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/key4.db",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/domain_to_categories.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/webappsstore.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/places.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/suggest.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/protections.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/ls-archive.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/permanent/indexeddb+++fx-devtools/idb/478967115deegvatroootlss--cans.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/permanent/chrome/idb/2918063365piupsah.sqlite",
    "/home/ai_admin/.config/mozilla/firefox/fnthq021.default-release/storage/permanent/chrome/idb/1451318868ntouromlalnodry--epcr.sqlite"
]

# Analyze databases
report_data = []

for db_path in db_paths:
    if os.path.exists(db_path):
        table_sizes, total_size = get_table_sizes(db_path)
        file_size = get_db_file_size(db_path)
        
        report_data.append({
            'database_path': db_path,
            'file_size_bytes': file_size,
            'total_tables': len(table_sizes),
            'total_size_bytes': total_size,
            'tables': table_sizes
        })

# Sort by total size to find the largest
report_data.sort(key=lambda x: x['total_size_bytes'], reverse=True)

# Save to CSV
with open('capacity_planning_report.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['database_path', 'file_size_bytes',