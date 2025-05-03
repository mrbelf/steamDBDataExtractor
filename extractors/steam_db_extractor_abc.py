from seleniumbase import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from ..util.game import Game
import os
import sys
import logging

class SteamDBExtractorABC:
  STEAM_DB_URL = 'https://steamdb.info'
  APP_ID_PATH = 'app'

  def __start_driver(self):
    driver = Driver(uc=True)
    self._driver = driver

  def __close_driver(self):
    self._driver.quit()
    self._driver = None
  
  def __init__(self):
    pass

  def _start(self, games: list[Game]):
    """Run once before all executions."""
    self.__start_driver()
    

  def _execute(self, game: Game):
    """Run once for each provided game."""
    pass

  def _disable(self, games: list[Game]):
    """Run once after all executions."""
    self.__close_driver()

  def get_data(self, games: list[Game]):
    """Collects data for all given games"""
    self._start(games)
    for game in games:
      self._execute(game)
    self._disable(games)
  
  def _get_game_page_url(self, app_id: int):
    return '/'.join([SteamDBExtractorABC.STEAM_DB_URL, SteamDBExtractorABC.APP_ID_PATH, str(app_id)])
  
  def _go_to_game_page(self, app_id: int): 
    self._driver.uc_open_with_reconnect(self._get_game_page_url(app_id), 10)
    self._driver.uc_gui_click_captcha()