
class AmazonAPI:
  """Amazon API. Generates links to amazon website and checks to see if the product specified is instock."""

  def __init__(self, amazonBaseUrl: str):
    self.amazonBaseUrl = amazonBaseUrl

  def set_asin(self, str_acin: str):
    """Sets the amazon ACIN code to find.

    Args:
        str_acin (str): The acin parameter given by the user.
    """
    self.acin = str_acin
    print(self.get_product_link())

  def get_product_link(self) -> str:
    """Gets the product link.

    Returns:
        str: Amazon base url + ACIN code
    """
    return f"{self.amazonBaseUrl}{self.acin}"

class BestbuyAPI:
  """BestBuy API. Generates links to bestbuy website and checks to see if the product specified is instock."""

  def __init__(self, bestbuyBaseUrl: str):
    self.bestbuyBaseUrl = bestbuyBaseUrl

  def set_webcode(self, str_webcode: str):
    """Sets the webcode of a product to find.

    Args:
        str_webcode (str): The webcode parameter given by the user.
    """
    self.webcode = str_webcode
    print(self.get_product_link())

  def get_product_link(self) -> str:
    """Gets the product link.

    Returns:
        str: Bestbuy base url + webcode
    """
    return f"{self.bestbuyBaseUrl}{self.webcode}"


class WalmartAPI:
  """Walmart API. Generates links to walmart website and checks to see if the product specified is instock."""

  def __init__(self, walmartBaseUrl: str):
    self.walmartBaseUrl = walmartBaseUrl

  def set_sku(self, str_sku: str):
    """Sets the sku of a product to find.

    Args:
        str_sku (str): The sku parameter given by the user.
    """
    self.sku = str_sku
    print(self.get_product_link())

  def get_product_link(self) -> str:
    """Gets the product link.

    Returns:
        str: Walmart base url + sku
    """
    return f"{self.walmartBaseUrl}{self.sku}"