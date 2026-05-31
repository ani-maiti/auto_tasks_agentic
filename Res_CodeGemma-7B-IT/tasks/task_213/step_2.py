# Print the top ten long functions from the CSV file
with open("long_functions.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0], row[1])