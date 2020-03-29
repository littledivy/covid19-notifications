import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

prev_cases = "0"
def extract():
  global prev_cases
  res = requests.get('https://www.worldometers.info/coronavirus/country/india').text
  soup = BeautifulSoup(res, 'html.parser')
  soup.encode('utf-8')
  cases = soup.find("div", { "class": "maincounter-number" }).get_text().strip()
  if(cases == prev_cases):
      print('['+ time.strftime('%l:%M:%S %p on %b %d, %Y') + ' ] NO CHANGE IN CASES')
  else:
    notifyMe('Total Number of cases', cases)
    if(prev_cases != "0"):
      print('[' + time.strftime('%l:%M:%S %p on %b %d, %Y') + ' ] CASES ROSE FROM ' + prev_cases + ' TO ' + cases)
    prev_cases = cases

def notifyMe(title, message):
  notification.notify(title=title, message=message, timeout=6)

while True:
  extract()
  time.sleep(10)
