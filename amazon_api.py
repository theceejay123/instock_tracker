class AmazonAPI:
  def __init__(self, amazonBaseUrl):
    self.amazonBaseUrl = amazonBaseUrl

  def set_asin(self, str_acin):
    self.acin = str_acin
    print(self.get_product_link())

  def get_product_link(self):
    return f"{self.amazonBaseUrl}{self.acin}"
