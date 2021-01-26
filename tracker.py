# Date Created: 2021-01-25
# Created By: Ceejay Pimentel
# Objective: To track multiple products in a json file

import json
import time
from selenium.webdriver.common.keys import Keys
from chromium_config import ChromeConfig
from web_api import AmazonAPI, WalmartAPI, BestbuyAPI

from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

f = open('test_data.json',)
web_data = json.load(f)
f.close()


if __name__ == '__main__':
  config = ChromeConfig()
  chrome_options = config.get_web_driver_options()
  config.set_ignore_certs_error(chrome_options)
  config.set_browser_as_incognito(chrome_options)
  config.set_automation_as_headless(chrome_options)
  driver = config.get_chrome_web_driver(chrome_options)

  amazon = AmazonAPI(config.amazonBaseUrl)
  bestbuy = BestbuyAPI(config.bestbuyBaseUrl)
  walmart = WalmartAPI(config.walmartBaseUrl)

  for i in web_data['web']:
    if i['seller'] == 'bestbuy':
      bestbuy.set_webcode(i['web_code'])
    if i['seller'] == 'amazon':
      amazon.set_asin(i['web_code'])
    if i['seller'] == 'walmart':
      walmart.set_sku(i['web_code'])