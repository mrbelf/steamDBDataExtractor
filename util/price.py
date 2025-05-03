import re

class Price:
  def _extract_currency(self, price_str: str) -> str:
    return re.match(r"[A-Z$]+", price_str).group(0)

  def _extract_value(self, price_str: str) -> int:
    total = 0
    dig = 0
    for num in re.findall(r"[0-9]+", price_str.replace(self._extract_currency(price_str), ""))[::-1]:
      total += int(num)*(10**dig)
      dig += len(num)
    return total


  def __init__(self, price_str: str):
    self.currency = self._extract_currency(price_str)
    self.value = self._extract_value(price_str)