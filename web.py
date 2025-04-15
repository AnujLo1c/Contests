from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import time

def get_user_contests(username):
    url = f"https://codeforces.com/contests/with/{username}"

    options = Options()
    options.headless = True  # Run in background
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(2)  # Wait for page to load

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    table = soup.find('div', class_='datatable')
    if not table:
        print("ℹ️ No contest data found.")
        return None

    tbody = table.find('tbody')
    if not tbody:
        print("ℹ️ Table body not found.")
        return None

    rows = tbody.find_all('tr')
    contests_data = {}

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols and len(cols) >= 6:
            contests_data[int(cols[0])] = {
                'Contest': cols[1],
                'Rank': cols[2],
                'Solved': cols[3],
                'Rating change': cols[4],
                'New rating': cols[5]
            }

    return contests_data

def save_to_json(data, filename="contests_data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"✅ Data saved to {filename}")

def run_app():
    print("🔍 Codeforces Contest Scraper")
    username = input("Enter Codeforces username: ").strip()
    data = get_user_contests(username)
    if data:
        save_to_json(data)

if __name__ == "__main__":
    run_app()
