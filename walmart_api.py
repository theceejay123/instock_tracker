class WalmartAPI:
  def __init__(self, walmartBaseUrl):
    self.walmartBaseUrl = walmartBaseUrl

  def set_sku(self, str_sku):
    self.sku = str_sku
    print(self.get_product_link())

  def get_product_link(self):
    return f"{self.walmartBaseUrl}{self.sku}"