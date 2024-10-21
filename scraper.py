import requests
from bs4 import BeautifulSoup

def get_craigslist_results(search_url, brand):
    # Fetch the page content
    response = requests.get(search_url)
    
    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return None
    
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')
    result_items = soup.find_all('li', class_='cl-static-search-result')
    
    results = []
    for item in result_items:
        title = item.find('div', class_='title').get_text(strip=True)
        link = item.find('a')['href']
        price = item.find('div', class_='price').get_text(strip=True) if item.find('div', class_='price') else 'N/A'
        location = item.find('div', class_='location').get_text(strip=True) if item.find('div', class_='location') else 'N/A'
        
        results.append({
            'title': title,
            'link': link,
            'price': price,
            'location': location,
            'brand': brand
        })
    
    return results
