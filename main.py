import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

def extract():
  res = requests.get('https://www.worldometers.info/coronavirus/country/india').text
  soup = BeautifulSoup(res, 'html.parser')
  soup.encode('utf-8')
  cases = soup.find("div", { "class": "maincounter-number" }).get_text().strip()
  notifyMe('Total Number of cases', cases)

def notifyMe(title, message):
  notification.notify(title=title, message=message, timeout=6)

while True:
  extract()
  time.sleep(10)
