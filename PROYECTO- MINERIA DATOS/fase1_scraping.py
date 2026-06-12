import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

respuesta = requests.get(url)

sopa = BeautifulSoup(respuesta.text, "html.parser")

paises = sopa.find_all("div", class_="country")

for pais in paises[:10]:
    nombre = pais.find("h3", class_="country-name").text.strip()
    capital = pais.find("span", class_="country-capital").text.strip()

    print("País:", nombre)
    print("Capital:", capital)
    print("-" * 30)