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
jsonFields = open(r"shipping_fields.json", "r")
shipping_fields = json.load(jsonFields)

jsonFields = open(r"payment_fields.json", "r")
payment_fields = json.load(jsonFields)

add_to_cart_btn = driver.find_element_by_class_name('addToCartButton')
if add_to_cart_btn.is_enabled():
    add_to_cart_btn.click()
    sleep(10)

    cart_btn = driver.find_element_by_xpath('//*[@id="cartIcon"]/div[1]/a')
    cart_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[2]/section/div/section/section[2]/div[2]/div/a')))

    checkout_btn = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[2]/div[2]/section/div/section/section[2]/div[2]/div/a')
    checkout_btn.click()
    sleep(2)

    age_btn = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[2]/div[2]/section/div/section/section[2]/div[2]/div/div/div/section/div[2]/a')
    age_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div/div/div/div[2]/div/div[2]/a')))

    guest_btn = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div/div[2]/div/div[2]/a')
    guest_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/form/div/div/div/section[1]/div/h1')))

    for name, value in shipping_fields.items():
        e = driver.find_element_by_name(name)
        if name == 'regionCode' or name == 'country':
            for option in e.find_elements_by_tag_name('option'):
                if option.get_attribute('value') == value:
                    option.click()
                    break
        else:
            e = driver.find_element_by_name(name)
            e.clear()
            e.send_keys(value)

    sleep(2)
    sh_chk_btn = driver.find_element_by_xpath('//*[@id="posElement"]/section/section[1]/button')
    sh_chk_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="shownCardNumber"]')))

    for name, value in payment_fields.items():
        e = driver.find_element_by_name(name)
        if name == 'expirationMonth' or name == 'expirationYear':
            for option in e.find_elements_by_tag_name('option'):
                if option.get_attribute('value') == value:
                    option.click()
                    break
        else:
            e = driver.find_element_by_name(name)
            e.clear()
            e.send_keys(value)
    
    pmt_chk_btn = driver.find_element_by_xpath('//*[@id="posElement"]/section/section[1]/button')
    pmt_chk_btn.click()