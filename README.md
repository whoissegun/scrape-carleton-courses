# Carleton Courses Scraper

This project uses Scrapy to scrape course information from Carleton University's website and seeds the data into a Supabase database.

## Requirements

- Python 3.7+
- Scrapy
- Supabase

## Installation

1. Clone the repository

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Scraping Courses

1. Configure the Scrapy settings in `settings.py` as needed.

2. Configure your Supabase credentials in `.env file`:
    ```
    SUPABASE_URL = 'your_supabase_url'
    SUPABASE_KEY = 'your_supabase_key'
    ```

3. Run the Scrapy spider:
    ```bash
    scrapy crawl courses
    ```





## License

This project is licensed under the MIT License. 

## Acknowledgements

- [Scrapy](https://scrapy.org/)
- [Supabase](https://supabase.io/)
