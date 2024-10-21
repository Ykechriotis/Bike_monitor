import yaml

def write_text_file(results, place):
    with open(place + "_craigslist_results.txt", "w") as file:
        for result in results:
            file.write(f"Title: {result['title']}\n")

def read_text_file(place):
    titles = []
    try:
        with open(place + "_craigslist_results.txt", "r") as file:
            for line in file:
                if line.startswith("Title: "):
                    title = line.replace("Title: ", "").strip()
                    titles.append(title)
    except FileNotFoundError:
        with open(place + "_craigslist_results.txt", "w") as file:
            pass 
        return titles 
    return titles

# Function to process new results
def process_results(results, prev_titles):
    new_results = [result for result in results if result['title'] not in prev_titles]
    return new_results

# Load configuration from YAML file
def load_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config


