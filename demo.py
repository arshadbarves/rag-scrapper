from webscraper import RagScraper
import asyncio
import json
from pprint import pprint

async def main():
    # Example URL - replace with your target website
    url = "https://langchain-ai.github.io/langgraph/"
    
    # Initialize the scraper with custom settings
    scraper = RagScraper(
        base_url=url,
        output_dir="langgraph_docs",
        rate_limit=1.0,  # 1 second between requests
        max_retries=3,
        respect_robots=True,
        max_workers=5
    )
    
    # Example 1: Scrape a single page
    print("\nExample 1: Scraping a single page...")
    content = await scraper.scrape_page(url)
    print(f"Title: {content['title']}")
    print(f"Content length: {len(content['main_content'])}")
    print(f"RAG content length: {len(content['rag_content'])}")
    print(f"Number of metadata items: {len(content['metadata'])}")
    print(f"Number of internal links: {len([l for l in content['links'] if l['type'] == 'internal'])}")
    print(f"Number of external links: {len([l for l in content['links'] if l['type'] == 'external'])}")
    
    # Example 2: Scrape multiple pages (limited to 5 pages)
    print("\nExample 2: Scraping multiple pages (limited to 5)...")
    scraper = RagScraper(
        base_url=url,
        output_dir="langgraph_docs_full",
        rate_limit=1.0,
        max_workers=5
    )
    await scraper.scrape_website(max_pages=5)
    
    # Print statistics
    stats = scraper.get_statistics()
    print("\nScraping Statistics:")
    print(f"Total pages scraped: {stats['total_pages']}")
    print(f"Failed URLs: {len(stats['failed_urls'])}")
    print(f"Total content size: {stats['total_content_size'] / 1024:.2f} KB")
    
    # Print index contents
    with open("langgraph_docs_full/index.json", "r") as f:
        index = json.load(f)
        print("\nDocument Headers:")
        for page in index['pages']:
            print(f"\n{page['title']}:")
            for header in page.get('headers', []):
                print(f"{'  ' * (header['level']-1)}- {header['text']}")

if __name__ == "__main__":
    asyncio.run(main())
