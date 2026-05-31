# Get database schemas
schemas = get_db_schemas(".")

# Get largest tables
largest_tables = get_largest_tables(schemas)

# Print largest tables
print(largest_tables)
```
execution trace:
stdout:
{'./test.db': 'table_1'}


stderr:


return code: 0