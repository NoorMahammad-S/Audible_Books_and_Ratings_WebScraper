import requests
from bs4 import BeautifulSoup
import csv

# URL of the Audible website to scrape
url = "https://www.audible.com/new-releases"

# Send a GET request to the Audible URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the section containing book information
books_section = soup.find('section', {'id': 'adbl-canvas-content'})

# Check if the books_section exists
if books_section:
    # Create a CSV file to store the scraped data
    csv_filename = "audible_books.csv"

    # Open the CSV file for writing with UTF-8 encoding
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(["Title", "Author", "Rating"])

        # Find and write data rows
        book_elements = books_section.find_all('li', class_='adbl-prod adbl-prod--tile')
        for book_element in book_elements:
            title = book_element.find('h3').text.strip()
            author = book_element.find('div', class_='bc-row-author').text.strip()
            rating = book_element.find('span', class_='bc-rating-stars__text').text.strip()

            writer.writerow([title, author, rating])

    print(f"Scraped Audible book data and saved to {csv_filename}")
else:
    print("Could not find the books_section on the page. Check if the website structure has changed.")
