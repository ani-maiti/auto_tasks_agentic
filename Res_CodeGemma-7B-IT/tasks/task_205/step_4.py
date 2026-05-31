# Generate schema summary
summary = generate_schema_summary(schemas)

# Save summary to markdown file
save_markdown(summary, "database_schema_summary.md")

# Print summary
print(summary)
```
execution trace:
stdout:
## Database: ./test.db

### Table: table_1

* column_1 (INTEGER)
* column_2 (TEXT)


stderr:


return code: 0