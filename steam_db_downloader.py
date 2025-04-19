from seleniumbase import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import sys
import logging


class SteamDBExtractorABC:
  STEAM_DB_URL = 'https://steamdb.info'
  APP_ID_PATH = 'app'

  def __start_driver(self):
    driver = Driver(uc=True)
    self._driver = driver
  
  def __init__(self):
    self.__start_driver()

  
  def _get_game_page_url(self, app_id):
    return '/'.join([SteamDBExtractorABC.STEAM_DB_URL, SteamDBExtractorABC.APP_ID_PATH, app_id])
  
  def _go_to_game_page(self, app_id):
    self._driver.uc_open_with_reconnect(self._get_game_page_url(app_id), 10)
    self._driver.uc_gui_click_captcha()