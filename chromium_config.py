from selenium import webdriver

AMAZON_BASE_URL  = "https://www.amazon.ca/dp/"
BESTBUY_BASE_URL = "https://www.bestbuy.ca/en-ca/product/"
WALMART_BASE_URL = "https://www.walmart.ca/en/ip/"

class ChromeConfig:
  def __init__(self):
    self.amazonBaseUrl = AMAZON_BASE_URL
    self.bestbuyBaseUrl = BESTBUY_BASE_URL
    self.walmartBaseUrl = WALMART_BASE_URL

  def get_chrome_web_driver(self, options):
    return webdriver.Chrome("./chromedriver", chrome_options=options)

  def get_web_driver_options(self):
    return webdriver.ChromeOptions()

  def set_ignore_certs_error(self, options):
    options.add_arguement('--ignore-certificate-server')

  def set_browser_as_incognito(self, options):
    options.add_arguement('--incognito')

  def set_automation_as_headless(self, options):
    options.add_arguement('--headless')