# Created by: Ceejay Pimentel
# Date created: 2020-11-18

from dotenv import load_dotenv
import os
import json
import requests
from bs4 import BeautifulSoup
from time import time, sleep
import smtplib
from twilio.rest import Client

# Load json values
jsonData = open(r"data.json", "r")
data = json.load(jsonData)

# Load environment variables
load_dotenv()

# BestBuy links to scrape
BESTBUY_URLS = [
    'https://www.bestbuy.ca/en-ca/product/xbox-series-x-1tb-console-new-model-online-only/14964951',
    'https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185',
    'https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184'
]
EBGAMES_URLS = [
    'https://www.ebgames.ca/PS5/Games/877523/playstation-5-digital-edition',
    'https://www.ebgames.ca/PS5/Games/877522/playstation-5#'
]
SOURCE_URLS = [
    'https://www.thesource.ca/en-ca/gaming/xbox/xbox-series-x/xbox-series-x-/p/108090646#product-store-availability',
    'https://www.thesource.ca/en-ca/gaming/playstation/ps5/playstation%c2%ae5-console/p/108090499',
    'https://www.thesource.ca/en-ca/gaming/playstation/ps5/playstation%c2%ae5-digital-edition-console/p/108090498'
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
}

# Twilio Client
client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")

def tracker():
    start_clock = time()
    timeout = 30
    while True:
        for url in BESTBUY_URLS:
            check_price(url)
        # for url in EBGAMES_URLS:
        #     eb_price(url)
        for url in SOURCE_URLS:
            source_price(url)
        sleep(timeout - ((time() - start_clock) % timeout))

def check_price(url):
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("h1", { "itemprop": "name" }).getText()
    button = soup.find("button", { "class": "addToCartButton" })
    if not button.has_attr("disabled"):
        print(f"{title.strip()} now available")
        send_email(title.strip(), url)

def eb_price(url):
    page = requests.get(f"{url}")
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("span", {"itemprop": "name"}).get_text()
    button = soup.find("a", {"class": "cartAddRadio"})
    if button['style'] == 'display:block;':
        # print(url, title.strip())
        send_email(title.strip(), url)

def source_price(url):
    page = requests.get(f"{url}")
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1', {'class': 'pdp-name'}).get_text()
    button = soup.find('button', {'class': 'addToCartButton'})
    if 'outOfStock' not in button['class']:
        send_email(title.strip(), url)

def send_email(title, url):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(os.getenv("GMAIL"), os.getenv("GMAIL_AUTH"))

    subject = f"BESTBUY - {title.upper()} NOW AVAILABLE"
    body = f"Check the link: {url}"

    msg = f"Subject: {subject}\n\n{body}"

    if title in ['PlayStation 5 Console - Online Only', 'PlayStation 5', 'PlayStation®5 Console']:
        server.sendmail(
            os.getenv("GMAIL"),
            # 'ceejaypimentel@hotmail.ca',
            data["PS5"],
            msg
        )
        send_sms(json.loads(os.getenv("PS5_SMS")), url)
    elif title in ['PlayStation 5 Digital Edition Console - Online Only', 'PlayStation 5 Digital Edition', 'PlayStation®5 Digital Edition Console']:
        server.sendmail(
            os.getenv("GMAIL"),
            # 'ceejaypimentel@hotmail.ca',
            data["PS5_DIGITAL"],
            msg
        )
        send_sms(json.loads(os.getenv("PS5DIGI_SMS")), url)
    else:
        server.sendmail(
            os.getenv("GMAIL"),
            data["XBOX"],
            msg
        )
        send_sms(json.loads(os.getenv("XBOX_SMS")), url)

    print("Email and Message has been sent!")
    server.quit() # end the connection

def send_sms(numbers, url):
    for number in numbers:
        client.messages.create(
            to=number,
            from_=TWILIO_NUMBER,
            body=f"INSTOCK TRACKER: IT IS AVAILABLE! {url}"
        )

# Run the program
print("Started Monitoring BestBuy, EBGames & The Source... (Every 30 seconds)")
tracker()

# print(json.loads(os.getenv("XBOX_SMS")))