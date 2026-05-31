import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="my_database",
    user="my_user",
    password="my_password"
)

# Create a cursor object
cur = conn.cursor()

# Execute the query to get the latest blog title
cur.execute("SELECT title FROM blog ORDER BY id DESC LIMIT 1")

# Fetch the result
result = cur.fetchone()

# Print the blog title
print(result[0])

# Close the cursor and connection
cur.close()
conn.close()