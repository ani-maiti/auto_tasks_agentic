import glob
import pandas as pd

# Find all Markdown files in the current directory
markdown_files = glob.glob("*.md")

# Initialize an empty list to store the report data
report_data = []

# Iterate over each Markdown file
for filename in markdown_files:
    # Read the Markdown file
    with open(filename, "r") as f:
        markdown_text = f.read()

    # Check if the file contains a table
    if "<table>" in markdown_text:
        # Extract the table data using pandas
        df = pd.read_html(markdown_text)[0]

        # Count the number of rows and columns in the table
        num_rows = df.shape[0]
        num_cols = df.shape[1]

        # Add the data to the report
        report_data.append([filename, num_rows, num_cols])

# Create a DataFrame from the report data
report_df = pd.DataFrame(report_data, columns=["Filename", "Rows", "Columns"])

# Save the report to a CSV file
report_df.to_csv("markdown_table_report.csv", index=False)

# Print a success message
print("Markdown table report generated successfully.")