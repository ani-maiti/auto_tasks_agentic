import os

# Step 1: Discover all SQLite databases in the current directory
databases = [f for f in os.listdir('.') if f.endswith('.db')]

if not databases:
    print("No SQLite databases found in the current directory.")
else:
    print(f"Found {len(databases)} SQLite databases:")
    for db in databases:
        print(db)
```

This code will list all SQLite databases (`*.db` files) in the current directory. If no databases are found, it will notify the user; otherwise, it will print the names of the discovered databases.