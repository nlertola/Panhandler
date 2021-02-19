from selenium import webdriver
import time

def scrape(streamerName, message):
    PATH = "./chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driverUrl = "https://www.twitch.tv/{}".format(streamerName)
    driver.get(driverUrl)


    stored_users = []
    # Make files
    usernameFile = open("usernames.txt", "a+")
    usernameFile.close()

    # Seed stored_users
    usernameFile = open("usernames.txt", "r")
    for line in usernameFile:
        stored_users.append(line)
    usernameFile.close()

    time.sleep(2)
    try:
        playingVid = driver.find_element_by_xpath('//*[@class="video-player"]')
    except Exception as e:
        print("The username you entered is invalid: {}".format(e))
        driver.close()

    messagedelay = 0;
    while True:
        users = driver.find_elements_by_xpath('//*[@class="chat-author__display-name"]')

        if len(users) > 0:
            userdata = users[-1].get_attribute('data-a-user')

            if userdata not in stored_users:
                print(userdata)
                stored_users.append(userdata)
                usernameFile = open("usernames.txt", "a+")
                usernameFile.write(userdata)
                usernameFile.write('\n')
                # Always close your goddamn files
                usernameFile.close()

                messagedelay = messagedelay + 1
                if messagedelay >= 7:
                    print(message + userdata)
                    messagedelay = 0

    time.sleep(15)
    driver.quit()
