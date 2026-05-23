from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://google.com")

search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('cat')
search_input.submit()

time.sleep(10)
driver.quit()
