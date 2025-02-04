import requests
from bs4 import BeautifulSoup
import csv

# Function to fetch HTML content of a webpage
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

# Function to parse Realtor data
def parse_realtor_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    realtors = []

    # Example selectors (modify according to the website structure)
    realtor_elements = soup.select('.realtor-card')
    for element in realtor_elements:
        name = element.select_one('.realtor-name').get_text(strip=True) if element.select_one('.realtor-name') else 'N/A'
        phone = element.select_one('.realtor-phone').get_text(strip=True) if element.select_one('.realtor-phone') else 'N/A'
        email = element.select_one('.realtor-email').get_text(strip=True) if element.select_one('.realtor-email') else 'N/A'
        
        realtors.append({
            'Name': name,
            'Phone': phone,
            'Email': email
        })
    return realtors

# Function to save data to a CSV file
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Phone', 'Email'])
        writer.writeheader()
        writer.writerows(data)

# Main function
def main():
    url = "https://www.example-realestate.com/realtors"  # Replace with the real website URL
    html = fetch_html(url)
    if html:
        realtors = parse_realtor_data(html)
        if realtors:
            save_to_csv(realtors, 'realtors.csv')
            print(f"Saved {len(realtors)} Realtors to realtors.csv")
        else:
            print("No Realtors found on the page.")

if __name__ == '__main__':
    main()
    