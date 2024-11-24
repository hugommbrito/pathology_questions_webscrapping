from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

edgeService = Service("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge")
chromeService = ChromeService("/Applications/Google/Chrome.app")
driver = webdriver.Chrome()

try:
  # time.sleep(10)
  for i in range(1, 2):
    url = "https://www.pathologyoutlines.com/review-questions?sid="+str(i)
    driver.get(url)

    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "f12b")))

    questionNumbers = driver.find_elements(By.CLASS_NAME, "f12b")
    questionImages = driver.find_elements(By.TAG_NAME, "img")

    print( "QUESTÕES DA PÁGINA " + str(i) + "!!!")
    print(driver.title)

    time.sleep(3)
    
    for question in range(0, len(questionNumbers)):
      print(questionNumbers[question].text)
      time.sleep(0.005)
    
    print('''
          

          IMAGENS!!!


          ''')
    
    for images in questionImages:
      print(images.get_attribute('src'))
      time.sleep(0.005)

    print('''
          

          NOVA PÁGINA!!!


          ''')

finally:
  driver.quit()