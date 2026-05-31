# Step 2: If no databases were found, ask for user input
if len(databases) == 0:
    databases = input("Please provide the paths to the SQLite databases separated by spaces: ").split()
    print(f"Using provided databases: {databases}")
else:
    print(f"Using discovered databases: {databases}")