import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Define the URL of the open data portal
url = "https://opendata.gov.uk/data/dataset"

# Define the keyword to search for
keyword = "education"

# Define the output file name
output_file = "datasets.csv"

# Define the report file name
report_file = "report.txt"

# Get the HTML content of the page
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the dataset links
dataset_links = soup.find_all("a", class_="dataset-link")

# Create a list to store the dataset metadata
datasets = []

# Iterate over the dataset links
for link in dataset_links:
    # Get the dataset URL
    dataset_url = link["href"]

    # Get the dataset page content
    dataset_response = requests.get(dataset_url)

    # Parse the dataset page content
    dataset_soup = BeautifulSoup(dataset_response.content, "html.parser")

    # Get the dataset metadata
    metadata = {}
    for meta in dataset_soup.find_all("meta"):
        if meta.get("property") and meta.get("content"):
            metadata[meta.get("property").replace("og:", "")] = meta.get("content")

    # Extract the necessary metadata fields
    metadata["title"] = metadata.get("title")
    metadata["description"] = metadata.get("description")
    metadata["publisher"] = metadata.get("og:description")
    metadata["license"] = metadata.get("og:license")
    metadata["updated"] = metadata.get("article:modified_time")

    # Add the dataset to the list
    datasets.append(metadata)

# Normalize the metadata fields
for dataset in datasets:
    # Convert the updated date to a datetime object
    dataset["updated"] = datetime.strptime(dataset["updated"], "%Y-%m-%dT%H:%M:%S")

    # Remove unnecessary fields
    del dataset["description"]
    del dataset["license"]

# Save the datasets to a CSV file
with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=datasets[0].keys())
    writer.writeheader()
    writer.writerows(datasets)

# Generate a report
with open(report_file, "w") as f:
    f.write("Most recently updated dataset:\n")
    f.write(f"{datasets[0]['title']}\n")
    f.write(f"Updated on: {datasets[0]['updated']}\n")

# Print the most recently updated dataset
print(datasets[0])