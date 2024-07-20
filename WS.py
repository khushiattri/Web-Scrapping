import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
for i in range(2, 12):

    url = "https://flipkart.com/search?q=refrigerator+under+20000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_19_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_19_na_na_na&as-pos=3&as-type=RECENT&suggestionId=refrigerator+under+20000&requestId=9ef77d6f-0796-4bb5-885c-887fa578bb69&as-searchtext=refrigerator%20under%2020000" + str(
        i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    names = soup.find_all("div", class_="KzDlHZ")
    print(names)
    for i in names:
        name = i.text
        Product_name.append(name)

    print(Product_name)
    prices = soup.find_all("div", class_="Nx9bqj _4b5DiR")

    for i in prices:
        name = i.text
        Prices.append(name)
    print(Prices)

    des = soup.find_all("ul", class_="G4BRas")
    for i in des:
        name = i.text
        Description.append(name)
    print(Description)

df = pd.DataFrame({"Product Name": Product_name, "Price": Prices, "Description": Description})

df.to_csv("Web Scrapping.csv")
