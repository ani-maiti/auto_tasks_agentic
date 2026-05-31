from collections import defaultdict

# Step 2: Build a global inventory of contained files
inventory = defaultdict(list)

for archive in archives:
    try:
        if archive.endswith('.zip'):
            with zipfile.ZipFile(archive, 'r') as zip_ref:
                inventory[archive] = zip_ref.namelist()
        # Add support for other archive types here
    except Exception as e:
        print(f"Error processing {archive}: {e}")

print("Inventory built successfully.")