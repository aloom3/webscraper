import requests
import time
from bs4 import BeautifulSoup
import time
import urllib.request
from twilio.rest import Client
url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xairfryer.TRS0&_nkw=airfryer&_sacat=0"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
name = soup.find("h3", {"class": "s-item__title"}).get_text(separator=u" ")
price = soup.find("span", {"class": "s-item__price"}).get_text()
print(url);
print("The name of the air fryer is: " + name);
print("The price of the item is: " + price)
client = Client("ACdce0135d54ce9274a466b36982c3f9a5", "60bf1311eee07af371ccf696c483cf8a" )
client.messages.create(to="number being sent to", from_="your number",body = "Airfryer name:" + name + ", Price is " + price)
