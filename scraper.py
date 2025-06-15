# scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_content(url):
    try:
        response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            text = " ".join([p.get_text() for p in paragraphs])
            return {"url": url, "text": text}
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
    return None
