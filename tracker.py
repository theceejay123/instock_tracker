# Date Created: 2021-01-25
# Created By: Ceejay Pimentel
# Objective: To track multiple products in a json file

import json
import time
from selenium.webdriver.common.keys import Keys
from chromium_config import ChromeConfig
from amazon_api import AmazonAPI

from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

if __name__ == '__main__':
  x = ChromeConfig()
  amazon_api = AmazonAPI(x.amazonBaseUrl)