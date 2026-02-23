# 🚀 Audible Books Web Scraper (Python + BeautifulSoup)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Web Scraping](https://img.shields.io/badge/Web-Scraping-green)
![BeautifulSoup](https://img.shields.io/badge/Parser-BeautifulSoup-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A **Python web scraping project** that extracts the latest audiobook releases from **Audible** and saves structured data into a CSV file.

This project demonstrates how to build a **real-world web scraper using Python, Requests, and BeautifulSoup** for data extraction and analysis.

---

## 📌 Features

* Scrapes latest Audible audiobook releases
* Extracts book title, ratings, and relevant metadata
* Saves data into structured CSV format
* Lightweight and beginner-friendly
* Easy to customize for other Audible pages
* Demonstrates real-world **data scraping workflow**

---

## 🛠 Tech Stack

* **Python 3**
* `requests` – HTTP requests handling
* `beautifulsoup4` – HTML parsing
* `csv` – Data export

---

## 📂 Project Structure

```
audible-book-webscraper/
│── scraper.py
│── audible_books.csv
│── README.md
│── LICENSE.md
```

---

## 📦 Installation

Make sure Python 3.x is installed.

Install required dependencies:

```bash
pip install requests beautifulsoup4
```

---

## ▶️ Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/NoorMahammad-S/audible-book-webscraper.git
cd audible-book-webscraper
```

### 2️⃣ Run the Script

```bash
python scraper.py
```

After execution, the script will generate:

```
audible_books.csv
```

Containing the scraped Audible book data.

---

## ⚙️ Configuration

To scrape a different Audible page, modify the `url` variable inside `scraper.py`:

```python
url = "https://www.audible.com/new-releases"
```

You can adapt this script to scrape:

* Best Sellers
* Trending Audiobooks
* Category-based listings
* Ratings-specific listings

---

## 🎯 Use Cases

* Data Analysis projects
* Web scraping portfolio projects
* Python automation practice
* Building audiobook datasets
* Learning BeautifulSoup
* Beginner data engineering practice

---

## 📊 Example Output (CSV Columns)

| Title        | Author      | Rating | Price  |
| ------------ | ----------- | ------ | ------ |
| Example Book | Author Name | 4.5    | $19.99 |

---

## 🤝 Contributing

Contributions are welcome!

If you would like to:

* Improve scraping performance
* Add pagination support
* Add error handling
* Add proxy/user-agent rotation
* Convert to API-style output (JSON)

Feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.
See `LICENSE.md` for details.

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
Please ensure compliance with Audible’s terms of service before scraping.

---

## 🔎 SEO Keywords

Python web scraper, Audible scraper, Audible books dataset, Python BeautifulSoup example, web scraping tutorial Python, scraping Audible books, data extraction Python, CSV export Python.

---
