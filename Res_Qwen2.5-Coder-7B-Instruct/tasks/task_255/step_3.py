import csv

headings = []
with open('duplicated_headings.txt', 'r') as file:
    for line in file:
        headings.append(line.strip())

with open('report.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Duplicated Headings'])
    writer.writerows([[heading] for heading in headings])