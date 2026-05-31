with open("email_addresses.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["file_name", "column_name", "column_index"])
    writer.writeheader()
    writer.writerows(results)