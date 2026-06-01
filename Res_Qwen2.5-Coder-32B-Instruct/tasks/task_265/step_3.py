import pandas as pd
import re

email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

csv_files = [
    "./cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv",
    "./common_keys_report.csv",
    "./python_files_line_counts.csv",
    "./largest_files.csv",
    "./archive_comparison.csv",
    "./results.csv",
    "./domain_analysis.csv",
    "./image_hashes.csv"
]

report = []

for file in csv_files:
    try:
        df = pd.read_csv(file)
        email_columns = [col for col in df.columns if df[col].astype(str).str.match(email_pattern).any()]
        if email_columns:
            report.append({"file": file, "email_columns": ", ".join(email_columns)})
    except Exception as e:
        print(f"Error reading {file}: {e}")

report_df = pd.DataFrame(report)
report_df.to_csv("email_columns_report.csv", index=False)
print("Report generated and saved to email_columns_report.csv")