import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image
from io import BytesIO
from IPython import embed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import itertools

def read_csv():
  with open('src/codes.csv', 'r', encoding='utf-8-sig', newline='') as f:
    csv_reader = csv.reader(f)
    codes = [row for row in csv_reader]
    return list(itertools.chain.from_iterable(codes))

def snapshots(code):
  try:
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(options=options)
    login(driver, code)
    personnal_evaluation(driver)
  finally:
    driver.quit()

def login(driver, code):
  url = 'http://localhost:3000/users/sign_in'
  driver.get(url)
  input_code_form = driver.find_element(By.ID, 'user_email')
  input_code_form.send_keys(code)
  input_password_form = driver.find_element(By.ID, 'user_password')
  input_password_form.send_keys('123456')
  login_button = driver.find_element(By.NAME, 'button')
  login_button.click()

def personnal_evaluation(driver):
  url = 'http://localhost:3000/personnel_evaluations?year=2024&eval_period_code=210&classification=3'
  driver.get(url)
  eval_button = driver.find_element(By.XPATH, "//button[contains(text(), '評価(表示)')]")
  eval_button.click()

def main():
  codes = read_csv()
  for code in codes:
    snapshots(code)

main()
