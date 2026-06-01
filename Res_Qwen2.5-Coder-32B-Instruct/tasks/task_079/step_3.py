import json
import sys

data = json.load(sys.stdin)
print(f"The number of stars for the requests GitHub repository is: {data['stargazers_count']}")