from selenium import webdriver
import time

def scrape(username, password, streamerName, message, userDelay):
    PATH = "./chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driverUrl = "https://www.twitch.tv/{}".format(streamerName)
    driver.get(driverUrl)


    # login
    loginBtn = driver.find_element_by_xpath('//*[@data-a-target="login-button"]')
    loginBtn.click()
    time.sleep(1)
    print("Username is : {}".format(username))
    usernameField = driver.find_element_by_id('login-username')
    usernameField.send_keys(username)
    passwordField = driver.find_element_by_id('password-input')
    passwordField.send_keys(password)

    loginBtn = driver.find_element_by_xpath('//*[@data-a-target="passport-login-button"]')
    loginBtn.click()
    time.sleep(1)


    stored_users = []
    # Make files
    usernameFile = open("usernames.txt", "a+")
    usernameFile.close()

    # Seed stored_users
    usernameFile = open("usernames.txt", "r")
    for line in usernameFile:
        stored_users.append(line)
    usernameFile.close()

    # Probably need to complete the login yourself
    # Hit 'Y' + RETURN to continue
    print("\nPress Enter to continue.")
    input()

    time.sleep(2)
    try:
        playingVid = driver.find_element_by_xpath('//*[@class="video-player"]')
    except Exception as e:
        print("The username you entered is invalid: {}".format(e))
        driver.close()

    messagedelay = 0;
    lastuser = ""
    while True:
        users = driver.find_elements_by_xpath('//*[@class="chat-author__display-name"]')

        if len(users) > 0:
            user = users[-1]
            userdata = user.get_attribute('data-a-user')
            if lastuser == userdata:
                continue
            
            lastuser = userdata

            if 'bot' in userdata:
                continue

            if userdata not in stored_users:
                print(userdata)

                messagedelay = messagedelay + 1
                if messagedelay >= userDelay:
                    stored_users.append(userdata)
                    usernameFile = open("usernames.txt", "a+")
                    usernameFile.write(userdata)
                    usernameFile.write('\n')
                    # Always close your goddamn files
                    usernameFile.close()

                    print(message + userdata)
                    print("Added user data to stored file")
                    try:
                        user.click()
                        time.sleep(2)
                        whisper = user.find_element_by_xpath('//*[@data-test-selector="whisper-button"]')
                        whisper.click()
                        time.sleep(2)

                        inputField = driver.find_element_by_xpath('//*[@data-a-target="whisper-thread-{}"]'.format(userdata))
                        inputText = inputField.find_element_by_xpath('.//*[@data-a-target="tw-input"]')
                        inputText.send_keys(message)
                    except Exception as e:
                        print("An exception occurred: ", e)
                        print("Something happened. Let's keep going anyway!")

                    messagedelay = 0

    time.sleep(15)
    driver.quit()
