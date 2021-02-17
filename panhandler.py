from selenium import webdriver
import time

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.twitch.tv/")

time.sleep(15)
driver.quit()
