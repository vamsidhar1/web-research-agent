# search.py

from serpapi import GoogleSearch
from config import SERPAPI_API_KEY

class WebSearchTool:
    def __init__(self):
        self.api_key = SERPAPI_API_KEY

    def search(self, query, num_results=5):
        params = {
            "q": query,
            "num": num_results,
            "api_key": self.api_key,
            "engine": "google"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        search_results = []
        for res in results.get("organic_results", []):
            search_results.append({
                "title": res.get("title"),
                "link": res.get("link"),
                "snippet": res.get("snippet"),
            })
        return search_results
