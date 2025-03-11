from bs4 import BeautifulSoup
import requests

scrape_me = requests.get("http://quotes.toscrape.com")
scrape = BeautifulSoup(scrape_me.text, "html.parser")

quotes = scrape.find_all("span", attrs={"class":"text"})
authors = scrape.find_all("small", attrs={"class":"author"})

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)


scrape_my_site = requests.get("https://curleefry.github.io/wdd130/WDD130/wwr.html/index.html")
scrape2 = BeautifulSoup(scrape_my_site.text, "html.parser")

target = scrape2.select_one("h1.home-title")

print(target.text)