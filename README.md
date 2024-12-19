# Advanced Web Scraper for RAG/LLM Applications

A production-ready web scraper designed specifically for extracting and processing content for Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) applications.

## Features

- **Asynchronous Processing**: Fast, concurrent scraping using `aiohttp`
- **RAG-Optimized Content**: Automatic cleaning and formatting for LLM/RAG use
- **Rate Limiting**: Configurable rate limiting to respect server resources
- **Robots.txt Compliance**: Ethical scraping with robots.txt parsing
- **Error Handling**: Robust error handling with retries and logging
- **Content Processing**:
  - Clean content extraction
  - Metadata parsing
  - Header structure preservation
  - Link classification (internal/external)
  - RAG-friendly content formatting
- **Performance**:
  - Concurrent processing
  - Connection pooling
  - Configurable batch sizes
  - Memory-efficient operation

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
import asyncio
from webscraper import WebScraper

async def main():
    # Initialize scraper
    scraper = WebScraper(
        base_url="https://example.com",
        output_dir="scraped_content",
        rate_limit=1.0,  # 1 second between requests
        max_retries=3,
        respect_robots=True,
        max_workers=5
    )

    # Scrape a single page
    content = await scraper.scrape_page("https://example.com/page")
    
    # Scrape multiple pages
    await scraper.scrape_website(max_pages=10)

if __name__ == "__main__":
    asyncio.run(main())
```

## Configuration

- `base_url`: The base URL to scrape
- `output_dir`: Directory to save scraped content
- `rate_limit`: Minimum time between requests in seconds
- `max_retries`: Maximum number of retry attempts
- `respect_robots`: Whether to respect robots.txt rules
- `max_workers`: Maximum number of concurrent workers

## Output Format

The scraper produces JSON files with the following structure:
```json
{
    "url": "https://example.com/page",
    "title": "Page Title",
    "main_content": "Original content...",
    "rag_content": "Cleaned content for RAG...",
    "metadata": {
        "description": "...",
        "keywords": "..."
    },
    "links": [
        {
            "url": "...",
            "text": "...",
            "type": "internal/external"
        }
    ],
    "headers": ["H1", "H2", ...],
    "timestamp": "2024-12-19T10:12:34"
}
```

## Project Structure

```
webscrapper/
├── data/                      # All data files (ignored by git)
│   ├── scraped_content/      # Scraped content organized by domain
│   │   └── example.com/      # Domain-specific content
│   └── logs/                 # Log files
├── webscraper.py             # Main scraper implementation
├── example.py                # Example usage and CLI
├── demo.py                   # Simple demo script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── LICENSE                   # MIT License
```

The `data/` directory is automatically created and organized as follows:
- `scraped_content/`: Contains subdirectories for each scraped domain
- `logs/`: Contains scraping logs and error reports

All data files are ignored by git to keep the repository clean and focused on code.

## Best Practices

1. **Rate Limiting**: Always set appropriate rate limits to avoid overwhelming servers
2. **Robots.txt**: Keep `respect_robots=True` for ethical scraping
3. **Error Handling**: Monitor the logs for any scraping issues
4. **Content Verification**: Regularly check the quality of extracted content

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

## Author

Your Name
