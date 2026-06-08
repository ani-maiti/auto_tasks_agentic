import requests
import csv
from datetime import datetime
import json

# Let's try a different approach - directly query the CKAN API endpoint used by data.gov
ckan_url = "https://data.gov/api/action/package_search"
params = {"q": "climate", "rows": 3}
try:
    response = requests.get(ckan_url, params=params, timeout=10)
    if response.status_code == 200:
        data = response.json()
        print("Successfully fetched sample data from data.gov")
        print(f"Found {len(data['result']['results'])} datasets")
        
        # Check structure of the first dataset
        if data['result']['results']:
            sample_dataset = data['result']['results'][0]
            print("Sample dataset keys:", list(sample_dataset.keys()))
            
            # Print some key fields to understand the structure
            print("\nDataset title:", sample_dataset.get('title', 'N/A'))
            print("Dataset name:", sample_dataset.get('name', 'N/A'))
            print("Dataset description:", sample_dataset.get('notes', 'N/A')[:100] + "..." if sample_dataset.get('notes') else 'N/A')
            print("Dataset tags:", sample_dataset.get('tags', []))
            print("Dataset organization:", sample_dataset.get('organization', {}).get('title', 'N/A'))
            print("Dataset last modified:", sample_dataset.get('metadata_modified', 'N/A'))
            
            # Save this for later processing
            datasets = [sample_dataset]
        else:
            print("No datasets found")
    else:
        print(f"API call failed with status code: {response.status_code}")
        print("Response content:", response.text[:500])
except Exception as e:
    print(f"Error accessing data.gov: {e}")
    print("Trying alternative approach...")
    
    # Try a simple GET request to see what we get
    try:
        simple_response = requests.get("https://data.gov", timeout=10)
        print(f"Simple request to data.gov returned status: {simple_response.status_code}")
    except Exception as e2:
        print(f"Simple request also failed: {e2}")