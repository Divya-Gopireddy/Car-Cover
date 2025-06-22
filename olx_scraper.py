import requests
from bs4 import BeautifulSoup

# URL for searching "car cover" on OLX India
url = "https://www.olx.in/items/q-car-cover"

# Browser headers (helps avoid being blocked)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Send GET request to OLX
response = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all listing titles (adjust selector if website updates)
results = soup.find_all("div", class_="_2tW1I")  # OLX may change this class

# Create and open file to save results
file_name = "olx_car_covers.txt"
with open(file_name, "w", encoding="utf-8") as file:
    for item in results:
        title = item.get_text(strip=True)
        file.write(title + "\n")

print(f"✅ Search results saved to '{file_name}'")
