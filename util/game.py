from .price import Price

class Game():
  def _has_valid_name(self) -> bool:
    return isinstance(self._name, str) and (len(self._name.strip()) != 0) 
  
  def _has_valid_id(self) -> bool:
    return isinstance(self._id, int) and self._id > 0
  
  def _is_identifiable(self) -> bool:
    return self._has_valid_name() or self._has_valid_id()

  def __init__(self, name: str = None, id: int = None):
    self._name = name
    self._id = id
    self._price = None
    self._lowest_price = None

  def set_price(self, price_str: str) -> Price:
    self._price = Price(price_str)
    return self._price
  
  def set_lowest_price(self, price_str: str) -> Price:
    self._lowest_price = Price(price_str)
    return self._lowest_price