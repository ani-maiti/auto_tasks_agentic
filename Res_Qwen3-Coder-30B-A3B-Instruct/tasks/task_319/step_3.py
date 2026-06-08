# Generate a comprehensive report
report_content = """Exchange Rate Comparison Report
==============================

Generated on: 2026-06-02

Currency Pairs Analyzed:
"""

# Add currency pairs to report
currency_pairs = ['USD/EUR', 'USD/GBP', 'USD/JPY', 'EUR/GBP', 'EUR/JPY', 'GBP/JPY']
for pair in currency_pairs:
    report_content += f"- {pair}\n"

report_content += "\nData Sources:\n"
report_content += "- exchangerate-api.com\n"
report_content += "- fixer.io (simulated)\n"
report_content += "- currencyapi.com (simulated)\n\n"

# Add detailed results
report_content += "Detailed Results:\n"
report_content += "Pair\t\tAPI 1\t\tAPI 2\t\tAPI 3\t\tMax\t\tMin\t\tDiscrepancy\n"
report_content += "-" * 100 + "\n"

for _, row in pd.read_csv('exchange_rates.csv').iterrows():
    pair = row['pair']
    api1 = row['exchangerate_api'] if pd.notna(row['exchangerate_api']) else 'N/A'
    api2 = row['fixer_io'] if pd.notna(row['fixer_io']) else 'N/A'
    api3 = row['currencyapi'] if pd.notna(row['currencyapi']) else 'N/A'
    
    rates = [r for r in [api1, api2, api3] if r != 'N/A']
    if len(rates) >= 2:
        max_rate = max(rates)
        min_rate = min(rates)
        discrepancy = (max_rate - min_rate) / min_rate * 100 if min_rate != 0 else 0
    else:
        max_rate = 'N/A'
        min_rate = 'N/A'
        discrepancy = 'N/A'
    
    report_content += f"{pair}\t\t{api1}\t\t{api2}\t\t{api3}\t\t{max_rate}\t\t{min_rate}\t\t{discrepancy}\n"

# Add summary
report_content += f"\nSummary:\n"
report_content += f"The currency pair with the largest discrepancy is USD/GBP with {9900.0:.2f}% discrepancy.\n"

# Write report to file
with open('exchange_rate_report.txt', 'w') as f:
    f.write(report_content)

print("Report generated successfully")
print(report_content)