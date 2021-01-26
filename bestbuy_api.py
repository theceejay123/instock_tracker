class BestbuyAPI:
  def __init__(self, bestbuyBaseUrl):
    self.bestbuyBaseUrl = bestbuyBaseUrl

  def set_webcode(self, str_webcode):
    self.webcode = str_webcode
    print(self.get_product_link())

  def get_product_link(self):
    return f"{self.bestbuyBaseUrl}{self.webcode}"