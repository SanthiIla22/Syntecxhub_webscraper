import requests
from bs4 import BeautifulSoup
import json
import csv
import time

# Website URL (Example: BBC News)
url = "https://www.bbc.com/news"

# Send request
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

headlines_data = []

# Extract headlines (BBC example)
for item in soup.find_all("h3"):
    title = item.get_text(strip=True)
    parent = item.find_parent("a")
    
    if parent and parent.get("href"):
        link = parent.get("href")
        if not link.startswith("http"):
            link = "https://www.bbc.com" + link
        
        headlines_data.append({
            "title": title,
            "url": link
        })

# Add delay (respect website)
time.sleep(2)

# Save to JSON
with open("headlines.json", "w", encoding="utf-8") as f:
    json.dump(headlines_data, f, indent=4, ensure_ascii=False)

# Save to CSV
with open("headlines.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "url"])
    writer.writeheader()
    writer.writerows(headlines_data)

print("Headlines saved successfully!")