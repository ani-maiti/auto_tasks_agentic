# Remove non-existent archives from the list
archives = [
    'zip_cp437_header.zip',
    'zipdir_backslash.zip',
    'zipdir.zip',
    'missing_directory.zip',
    'nested_portion1.zip',
    'top_level_portion1.zip'
]

# Re-run the inventory gathering process
inventories = {}
for archive in archives:
    try:
        inventory = get_inventory(archive)
        inventories[archive] = inventory
    except Exception as e:
        print(f"Error processing {archive}: {e}")

# Check if there are any inventories before attempting intersection
if inventories:
    common_files = set.intersection(*inventories.values())
else:
    common_files = set()

# Save the analysis to CSV
with open('analysis.csv', 'w') as f:
    f.write('Archive,File\n')
    for archive, inventory in inventories.items():
        for file in inventory:
            f.write(f'{archive},{file}\n')

    # Add common files section
    f.write('\nCommon Files\n')
    for file in common_files:
        f.write(f'All,{file}\n')

print("Analysis saved to analysis.csv")