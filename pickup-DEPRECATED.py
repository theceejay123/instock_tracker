# Created by: Ceejay Pimentel
# Date created: 2020-11-24

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import time, sleep
from fake_useragent import UserAgent
import json

options = webdriver.ChromeOptions()
ua = UserAgent()
user_agent = ua['google chrome']
options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
url = "https://www.bestbuy.ca/en-ca/product/demon-s-souls-ps5/14962275"
driver.get(url)
sleep(1)

wait = WebDriverWait(driver, 50)

# Load JSON fields
json_fields = open(r"shipping_fields.json", "r")
shipping_fields = json.load(json_fields)

json_fields = open(r"payment_fields.json", "r")
payment_fields = json.load(json_fields)

rsv_instore_btn = driver.find_element_by_class_name('x-reserveInStoreButton')
if rsv_instore_btn.is_enabled():
    rsv_instore_btn.click()