# 🧠 Web Research Agent

An autonomous AI-powered agent that:
- Searches Google for a given query (via SerpAPI)
- Scrapes and crawls top websites
- Extracts relevant content
- Summarizes the findings using OpenAI GPT
- Compiles results into a neat PDF report

This project is designed as a **real-world hiring assignment** for the **Masonry AI Agent Developer** role.

---

## 📂 Project Structure

web_research_agent/
├── config.py # API keys & configuration
├── search.py # Google Search using SerpAPI
├── scraper.py # Scrapes web pages
├── crawler.py # Crawls additional pages in same domain
├── summarizer.py # Summarizes content using OpenAI GPT
├── reporter.py # Generates a PDF report
├── main.py # Entry point to run the agent
├── requirements.txt # Dependencies
├── README.md # Project instructions



---

## ⚙️ Requirements

- Python 3.8+
- A SerpAPI account & API key
- An OpenAI account & API key

---

## 📦 Install Dependencies

```bash
# Clone the repo
git clone <YOUR_GITHUB_REPO_URL>
cd web_research_agent

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt


# config.py
SERPAPI_API_KEY = "YOUR_SERPAPI_API_KEY"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"


# Run the agent
python main.py


By default, main.py will:

Search for “Latest news on AI research”

Scrape and crawl up to 3 top results

Summarize all content

Save results to report.pdf



---


