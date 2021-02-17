from selenium import webdriver
import time

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)

streamer = "formal"
driver.get("https://www.twitch.tv/{}".format(streamer))

stored_users = []
while True:
    users = driver.find_elements_by_xpath('//*[@class="chat-author__display-name"]')

    userdata = users[-1].get_attribute('data-a-user')
    if userdata not in stored_users:
        print(userdata)
        stored_users.append(userdata)

time.sleep(15)
driver.quit()
