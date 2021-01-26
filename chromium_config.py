from selenium import webdriver

AMAZON_BASE_URL  = "https://www.amazon.ca/dp/"
BESTBUY_BASE_URL = "https://www.bestbuy.ca/en-ca/product/"
WALMART_BASE_URL = "https://www.walmart.ca/en/ip/"

class ChromeConfig:
  """Chrome driver configurations. The base of all options and driver for chrome driver."""

  def __init__(self):
    self.amazonBaseUrl = AMAZON_BASE_URL
    self.bestbuyBaseUrl = BESTBUY_BASE_URL
    self.walmartBaseUrl = WALMART_BASE_URL

  def get_chrome_web_driver(self, options):
    """Gets the driver for chrome.

    Args:
        options: Chrome options that are added by the user.

    Returns:
        Returns the chrome driver that is within the source code + additional options added.
    """
    return webdriver.Chrome("./chromedriver", chrome_options=options)

  def get_web_driver_options(self):
    """Gets the options for the webdriver (Currently only for Chrome driver).

    Returns:
        Returns the options for the chrome webdriver.
    """
    return webdriver.ChromeOptions()

  def set_ignore_certs_error(self, options):
    """Sets the options to ignore certification errors.

    Args:
        options: Paramater given by the user.
    """
    options.add_argument('--ignore-certificate-errors')

  def set_browser_as_incognito(self, options):
    """Sets the chrome driver option to incognito.

    Args:
        options: Parameter given by the user.
    """
    options.add_argument('--incognito')

  def set_automation_as_headless(self, options):
    """Sets the option for chromedriver to be headless (non-gui).

    Args:
        options: Parameter given by the user.
    """
    options.add_argument('--headless')