# Let me redefine the variables properly
import requests
import pandas as pd
import numpy as np
from datetime import datetime

# First, let's check if we can access a currency API
try:
    # Using exchangerate-api.com free tier
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=10)
    if response.status_code == 200:
        print("API access successful")
        data = response.json()
        rates = data['rates']
        print(f"Retrieved {len(rates)} currencies")
        # Get top 50 currencies (excluding USD)
        top_currencies = [c for c in rates.keys() if c != 'USD'][:50]
        print(f"Top 50 currencies: {top_currencies}")
    else:
        print("Failed to access API")
        # Fallback: create mock data
        print("Creating mock data for demonstration")
        top_currencies = ['EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY', 'SEK', 'NZD', 'SGD',
                         'NOK', 'DKK', 'TRY', 'RUB', 'INR', 'BRL', 'MXN', 'ZAR', 'HKD', 'THB',
                         'IDR', 'KRW', 'PHP', 'MYR', 'ILS', 'AED', 'SAR', 'EGP', 'QAR', 'OMR',
                         'BHD', 'JOD', 'LBP', 'IRR', 'AFN', 'PKR', 'BDT', 'LKR', 'MMK', 'VND',
                         'KHR', 'MAD', 'XOF', 'XAF', 'TZS', 'UGX', 'KES', 'GHS', 'NGN', 'ZMW']
except Exception as e:
    print(f"Error accessing API: {e}")
    # Create mock data
    top_currencies = ['EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY', 'SEK', 'NZD', 'SGD',
                     'NOK', 'DKK', 'TRY', 'RUB', 'INR', 'BRL', 'MXN', 'ZAR', 'HKD', 'THB',
                     'IDR', 'KRW', 'PHP', 'MYR', 'ILS', 'AED', 'SAR', 'EGP', 'QAR', 'OMR',
                     'BHD', 'JOD', 'LBP', 'IRR', 'AFN', 'PKR', 'BDT', 'LKR', 'MMK', 'VND',
                     'KHR', 'MAD', 'XOF', 'XAF', 'TZS', 'UGX', 'KES', 'GHS', 'NGN', 'ZMW']

print(top_currencies)