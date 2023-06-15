import requests
from bs4 import BeautifulSoup

# Create a session with SSL certificate verification disabled
session = requests.Session()
session.verify = False

# Set the base URL
base_url = 'https://crueltyfree.peta.org/companies-dont-test/'
page = 1
brands = set()

while True:
    # Construct the URL for the current page
    url = f'{base_url}{page}/'

    # Send a GET request to the page using the session
    response = session.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the unordered list containing the brands
    list_container = soup.find('ul', {'class': 'search-results'})

    # If no list container is found, it means we've reached the end of the pages
    if not list_container:
        break

    # Iterate over the list items and extract the brand names
    for item in list_container.find_all('li'):
        brand = item.text.strip()
        brands.add(brand)

    # Move to the next page
    page += 1

# Print the list of brands that don't test on animals
print(brands)

