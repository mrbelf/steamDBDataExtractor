from .price_extractor_abc import PriceExtractorABC

class LowestPriceExtractor(PriceExtractorABC):
  def _execute(self, game):
    super()._execute(game)
    columns = self._get_prices_columns(game)
    lowest_price_str = columns[3].text
    game.set_lowest_price(lowest_price_str)