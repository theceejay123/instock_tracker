# Created by: Ceejay Pimentel
# Date created: 2020-11-24

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()

driver = webdriver.Chrome(options=options)
url = "https://www.bestbuy.ca/en-ca/product/xbox-series-x-1tb-console-new-model-online-only/14964951"
driver.get(url)