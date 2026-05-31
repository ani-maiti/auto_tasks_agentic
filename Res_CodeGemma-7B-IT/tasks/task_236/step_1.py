import glob
import json
import difflib

def compare_json_files(file_list):
    """
    Compares JSON files with similar names and generates a comparison report.

    Args:
        file_list: A list of file paths to JSON files.

    Returns:
        A dictionary containing the comparison report.
    """

    # Create a list of file names with unique prefixes
    file_prefixes = set()
    for file in file_list:
        file_prefixes.add(file.split('.')[0])

    # Initialize the comparison report
    report = {}

    # Iterate over each file prefix
    for prefix in file_prefixes:
        # Get the files with the same prefix
        files = glob.glob(f"{prefix}.json")

        # Remove duplicates and sort the files
        files = list(set(files))
        files.sort()

        # Initialize the comparison data
        comparison_data = []

        # Iterate over each pair of files with the same prefix
        for i in range(len(files) - 1):
            for j in range(i + 1, len(files)):
                # Load the JSON files
                with open(files[i], 'r') as f1:
                    data1 = json.load(f1)
                with open(files[j], 'r') as f2:
                    data2 = json.load(f2)

                # Compare the JSON files using difflib
                diff = difflib.unified_diff(
                    json.dumps(data1, indent=4).splitlines(),
                    json.dumps(data2, indent=4).splitlines()
                )

                # Add the comparison data to the report
                comparison_data.append({
                    'file1': files[i],
                    'file2': files[j],
                    'diff': '\n'.join(diff)
                })

        # Add the comparison data to the report
        report[prefix] = comparison_data

    # Return the comparison report
    return report

# Get the list of JSON files
file_list = glob.glob('*.json')

# Compare the JSON files and generate the report
report = compare_json_files(file_list)

# Save the report to HTML
with open('json_comparison_report.html', 'w') as f:
    f.write('<html><head><title>JSON Comparison Report</title></head><body>')
    for prefix, comparison_data in report.items():
        f.write(f'<h2>{prefix}</h2>')
        for data in comparison_data:
            f.write(f'<p>File 1: {data["file1"]}</p>')
            f.write(f'<p>File 2: {data["file2"]}</p>')
            f.write(f'<pre>{data["diff"]}</pre>')
    f.write('</body></html>')