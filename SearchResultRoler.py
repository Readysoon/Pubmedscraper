import requests
from bs4 import BeautifulSoup

# Initial URL for the search results
base_url = "https://www.ncbi.nlm.nih.gov/pmc/"
search_url = base_url + "?term=ai+radiology"

# Function to get the total number of pages
def get_total_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    page_info = soup.find('input', {'name': 'EntrezSystem2.PEntrez.PMC.Pmc_ResultsPanel.Entrez_Pager.cPage'})
    if page_info:
        total_pages = int(page_info['last'])
        return total_pages
    return 1

# Function to visit each page and increment a counter
def visit_all_pages(base_url, total_pages):
    counter = 0
    for page_num in range(1, total_pages + 1):
        page_url = f"{base_url}&page={page_num}"
        response = requests.get(page_url)
        if response.status_code == 200:
            counter += 1
            print(f"Visited page {page_num}, Counter: {counter}")
        else:
            print(f"Failed to load page {page_num}")
    return counter

# Get the total number of pages
total_pages = get_total_pages(search_url)
print(f"Total pages found: {total_pages}")

# Visit each page and increment the counter
counter = visit_all_pages(search_url, total_pages)
print(f"Total pages visited: {counter}")
