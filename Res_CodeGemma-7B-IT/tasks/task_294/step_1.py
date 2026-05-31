import os
import hashlib

def analyze_archives(directory):
    """
    Analyzes archives in a directory tree, identifies duplicated contents, and generates a report.

    Args:
        directory: The directory to analyze.

    Returns:
        A dictionary containing the analysis results.
    """

    # Create a dictionary to store file hashes and their locations.
    file_hashes = {}

    # Iterate over all files in the directory tree.
    for root, _, files in os.walk(directory):
        for filename in files:
            # Get the full file path.
            file_path = os.path.join(root, filename)

            # Calculate the file's hash.
            with open(file_path, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            # Add the file to the dictionary if it's not already there.
            if file_hash not in file_hashes:
                file_hashes[file_hash] = []

            # Add the file's location to the list of locations for this hash.
            file_hashes[file_hash].append(file_path)

    # Create a list of duplicates.
    duplicates = []
    for hash, locations in file_hashes.items():
        if len(locations) > 1:
            duplicates.append((hash, locations))

    # Create a report.
    report = {
        "total_files": len(file_hashes),
        "duplicates": duplicates,
        "most_frequent_filename": None,
        "most_frequent_filename_count": 0,
    }

    # Find the most frequently occurring filename.
    for locations in file_hashes.values():
        for location in locations:
            filename = os.path.basename(location)
            if filename not in report["most_frequent_filename_count"]:
                report["most_frequent_filename_count"] = 0
            report["most_frequent_filename_count"] += 1
            if report["most_frequent_filename_count"] > report["most_frequent_filename_count"]:
                report["most_frequent_filename"] = filename
                report["most_frequent_filename_count"] = report["most_frequent_filename_count"]

    return report

# Get the current directory.
directory = os.getcwd()

# Analyze the archives.
report = analyze_archives(directory)

# Print the report.
print(report)