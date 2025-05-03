from .price_extractor_abc import PriceExtractorABC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CurrentPriceExtractor(PriceExtractorABC):
  def _execute(self, game):
    super()._execute(game)
    columns = self._get_prices_columns(game)
    price_str = columns[1].text
    game.set_price(price_str)
    return game