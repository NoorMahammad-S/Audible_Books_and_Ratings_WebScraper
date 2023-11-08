# Audible_Books_and_Ratings_WebScraper
This Python script scrapes the latest Audible book releases from the Audible website and saves the data to a CSV file. It uses the requests library to send HTTP GET requests to the Audible website and BeautifulSoup for HTML parsing.

## Prerequisites

Before running the script, ensure you have the following Python packages installed:

- `requests`
- `beautifulsoup4`

You can install these packages using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository to your local machine.

```bash
git clone https://github.com/NoorMahammad-S/audible-book-webscraper.git
```

2. Change your working directory to the project folder:

```bash
cd audible-book-scraper
```

3. Run the script:

```bash
python scraper.py
```

4. The script will scrape Audible's new releases and save the data to a CSV file named `audible_books.csv` in the same directory.

## Configuration

You can modify the script to scrape different Audible pages by changing the `url` variable in the script.

```python
url = "https://www.audible.com/new-releases"
```

## Contributing

Feel free to contribute to this project by opening issues or creating pull requests. We welcome any improvements or feature additions.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- This project uses the requests library for HTTP requests and BeautifulSoup for HTML parsing.

Happy scraping!
