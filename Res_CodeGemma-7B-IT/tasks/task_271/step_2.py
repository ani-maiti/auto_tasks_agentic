# Use the sqlite3.connect function with the 'uri' parameter to specify the database file path
conn = sqlite3.connect('file:path/to/database.sqlite?mode=rw', uri=True)