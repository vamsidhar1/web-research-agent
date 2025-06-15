# main.py

from search import WebSearchTool
from scraper import scrape_content
from crawler import crawl_links
from reporter import export_to_pdf

def run_agent(query, num_results=3):
    search_tool = WebSearchTool()
    search_results = search_tool.search(query, num_results)

    scraped = []
    for result in search_results:
        print(f"Scraping: {result['link']}")
        content = scrape_content(result['link'])
        if content:
            scraped.append(content)
        # Crawl and scrape more pages in the same domain
        extra_links = crawl_links(result['link'])
        for link in extra_links:
            print(f"Crawling: {link}")
            content = scrape_content(link)
            if content:
                scraped.append(content)

    # Basic relevancy filter
    relevant = [item for item in scraped if item and len(item['text']) > 300]

    export_to_pdf(relevant)

if __name__ == "__main__":
    run_agent("Latest news on AI research", num_results=3)
