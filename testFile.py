from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.youtube.com")
    time.sleep(2)

    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("Sample Video Title")
    search_box.submit()

    time.sleep(2)

    first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]')
    first_video.click()

    time.sleep(10)

finally:
    driver.quit()
