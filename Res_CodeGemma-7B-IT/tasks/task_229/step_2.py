import pandas as pd

# Create a new column for rank
report['rank'] = report.index.get_indexer(report.index.argsort(ascending=False)) + 1

# Save to CSV
report.to_csv('hacker_news_companies.csv', index=False)

print('Hacker News company report generated successfully.')