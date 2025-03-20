from bs4 import BeautifulSoup
import requests
import csv

scrape_me = requests.get("http://quotes.toscrape.com")
scrape = BeautifulSoup(scrape_me.text, "html.parser")

quotes = scrape.find_all("span", attrs={"class":"text"})
authors = scrape.find_all("small", attrs={"class":"author"})


filename = "quotes.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])  # Header
    for quote, author in zip(quotes, authors):
        writer.writerow([quote.text, author.text])

print(f"Data saved to {filename}")