import re
import csv
import requests
from datetime import datetime

def scrape_bip110():
    url = "https://bitnodes.io/nodes/?q=BIP110"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        # Search for pattern: (0 nodes/0.0%)
        # Group 1: Node Count, Group 2: Percentage
        pattern = r"\((\d+)\s+nodes/([\d\.]+)%\)"
        match = re.search(pattern, response.text)
        
        if match:
            return match.group(1), match.group(2)
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

node_count, percentage = scrape_bip110()

if node_count:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    # Store both count and percentage in the CSV
    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, node_count, percentage])
