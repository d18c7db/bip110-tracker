import re
import csv
import requests
from datetime import datetime

def scrape_bip110():
    url = "https://bitnodes.io/nodes/?q=BIP110"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        bip_match = re.search(r"\((\d+)\s+nodes/([\d\.]+)%\)", response.text)
        total_match = re.search(r"<span>(\d+)\s+nodes\s+as\s+of", response.text)

        node_count = bip_match.group(1) if bip_match else None
        percentage = bip_match.group(2) if bip_match else None
        total_nodes = total_match.group(1) if total_match else None

        return node_count, total_nodes, percentage

    except Exception as e:
        print(f"Error: {e}")
        return None, None, None

node_count, total_nodes, percentage = scrape_bip110()

if node_count and total_nodes:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Save to CSV with format: [timestamp, node_count, total_nodes, percentage]
    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, node_count, total_nodes, percentage])
