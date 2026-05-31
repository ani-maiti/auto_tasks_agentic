import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="blog",
    user="username",
    password="password",
    host="localhost"
)

# Create a cursor object
cur = conn.cursor()

# Execute the SQL query to get the latest blog title
cur.execute("SELECT title FROM posts ORDER BY created_at DESC LIMIT 1")

# Fetch the result
latest_title = cur.fetchone()[0]

# Print the latest blog title
print(latest_title)

# Close the cursor and connection
cur.close()
conn.close()