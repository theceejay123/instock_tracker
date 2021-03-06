# Created by: Ceejay Pimentel
# Date created: 2020-11-18

from fake_useragent import UserAgent
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from time import time, sleep
from twilio.rest import Client

import os
import json
import smtplib
import requests

# Load environment variables
load_dotenv()

# Load json values
jsonData = open(r"data.json", "r")
data = json.load(jsonData)

# Links to scrape
BESTBUY_URLS = [
	'https://www.bestbuy.ca/en-ca/product/xbox-series-x-1tb-console-new-model-online-only/14964951',
	'https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185',
	'https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184'
]

HEADERS = {
	"User-Agent": UserAgent().random
}

# Twilio Client
client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")

start_clock = time()
timeout = 2

def tracker():
	while True:
		for url in BESTBUY_URLS:
			check_price(url)
		sleep(timeout - ((time() - start_clock) % timeout))

def check_price(url):
	try:
		page = requests.get(url, headers=HEADERS)
		soup = BeautifulSoup(page.content, 'html.parser')
		title = soup.find("h1", { "itemprop": "name" }).getText()
		button = soup.find("button", { "class": "addToCartButton" })
		print(f'{title} - Check!\n{"Button is disabled." if button.has_attr("disabled") else "Button is enabled!"}')
		if not button.has_attr("disabled"):
			print(f"{title.strip()} now available")
			send_email(title.strip(), url)
		print("")
		sleep(0.25)
	except:
		pass

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
print("Started Monitoring BestBuy (Every 5 seconds)")
tracker()