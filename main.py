import time
import sys
from scraper import get_craigslist_results
from emailer import send_email, generate_email_body
from file_utils import write_text_file, read_text_file, process_results, load_config
import requests
import yaml

# Function to check internet connection
def check_internet_connection(url='http://www.google.com', timeout=30):
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

def main(args=None):
 # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # or 465 for SSL

    config = load_config('config.yaml')

    from_email = config['email']['from_email']
    to_email = config['email']['to_email']
    smtp_user = config['email']['smtp_user']
    smtp_password = config['email']['smtp_password']
    place = config['place']
    location = config['location']
    distance = config['distance']
    brands = config['bikes']['brands']
    prices = config['bikes']['prices']
    filtered = config['filtered']
    max_price = config['max_price']
    min_price = config['min_price']

    boot_time = time.time()
    while not check_internet_connection():
        print("No internet connection. Exiting.")
        time.sleep(3)
        if time.time() - boot_time > 30:
            sys.exit()

    if not filtered:
        brands = ["ALL BRANDS"]
        prices = [str(max_price)]
    

    all_results = []
    num_found = [0] * len(brands)


    current_time = time.localtime()
    time_string = time.strftime("%m/%d/%Y %H:%M", current_time)

    if filtered:
        for i in range(len(brands)):
            search_url = f'https://chicago.craigslist.org/search/{place}/bia?auto_make_model={brands[i]}&{location}&max_price={prices[i]}&search_distance={distance}#search=1~gallery~0~0'
            results = get_craigslist_results(search_url, brands[i])
            if results:
                all_results.extend(results)
                num_found[i] = len(results)
    else:
        search_url = f'https://chicago.craigslist.org/search/{place}/bia?&{location}&max_price={max_price}&min_price={min_price}&search_distance={distance}#search=1~gallery~0~0'
        results = get_craigslist_results(search_url, brands[0])
        if results:
            all_results.extend(results)
            num_found[0] = len(results)

    prev_titles = read_text_file(place)
    new_results = process_results(all_results, prev_titles)
    subject = f"{time_string}  {place} Craigslist Bike Search Results"
    email_body = generate_email_body(all_results, new_results, brands, num_found, place, time_string)
    write_text_file(all_results, place)

    send_email(from_email, to_email, smtp_user,smtp_password, subject, email_body)


if __name__ == "__main__":
    main()

   
