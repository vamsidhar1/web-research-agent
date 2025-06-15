# crawler.py

from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

def crawl_links(base_url, max_pages=3):
    try:
        response = requests.get(base_url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [urljoin(base_url, a['href']) for a in soup.find_all('a', href=True)]
            domain = urlparse(base_url).netloc
            internal_links = [link for link in links if urlparse(link).netloc == domain]
            return list(set(internal_links))[:max_pages]
    except Exception as e:
        print(f"Error crawling {base_url}: {str(e)}")
    return []
