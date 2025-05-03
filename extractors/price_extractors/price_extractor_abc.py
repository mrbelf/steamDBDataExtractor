from ..steam_db_extractor_abc import SteamDBExtractorABC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PriceExtractorABC(SteamDBExtractorABC):
  def _get_prices_columns(self, game):
    self._go_to_game_page(game._id)
    current_row = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "table-prices-current")))
    return current_row.find_elements(By.XPATH, '*')