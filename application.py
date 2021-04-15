from tkinter import *
from panhandler import *
import threading
from subprocess import call


root = Tk()
root.configure(background='#404040', padx=10, pady=10)
root.title("Panhandler")

title = Label(root, text="That Panhandlin' Bitch")
title.configure(background='#404040', fg='#FFFFFF')
title.grid(row=0, column=0)

usernameLabel = Label(root, text="Enter your Twitch username", pady=10)
usernameLabel.configure(background='#404040', fg='#FFFFFF')
usernameLabel.grid(row=1, column=0)

credentials = open("credentials.txt", "r")

username = Entry(root, width=40)
username.grid(row=2, column=0)
username.insert(0, credentials.readline())

passwordLabel = Label(root, text="Enter your Twitch password", pady=10)
passwordLabel.configure(background='#404040', fg='#FFFFFF')
passwordLabel.grid(row=3, column=0)

password = Entry(root, show='*', width=40)
password.grid(row=4, column=0)
password.insert(0, credentials.readline())

credentials.close()

streamerLabel = Label(root, text="Enter a streamer's username", pady=10)
streamerLabel.configure(background='#404040', fg='#FFFFFF')
streamerLabel.grid(row=5, column=0)

streamer = Entry(root, width=40)
streamer.grid(row=6, column=0)
streamer.insert(0, "")

def executeScrape(username, password, streamerName, message, userDelay):
    print("Ready to run scraping process for {}".format(streamerName))
    scrape(username, password, streamerName, message, userDelay)


def startScrape():
    usernameError = Label(root, text="Username is required")
    if streamer.get():
        streamerName = streamer.get()
        usernameError.grid_forget()
    else:
        usernameError.configure(background='#404040', fg='#FFFFFF')
        usernameError.grid(row=7, column=1)
    message = streamermessage.get("1.0",END)
    userDelay = messageDelay.get()
    print("Collected user input values")
    panhandle_thread = threading.Thread(target=executeScrape, name="Scraper", args=[username.get(), password.get(), streamerName, message, userDelay])# args=[username.get(), password.get(), streamerName, message, userDelay])
    panhandle_thread.start()
    print("Scraper for {} is now running in the background.".format(streamerName))
    print("Message is: {}".format(message))
    print("Delay between users is {} users".format(userDelay))

# Button to start scraping
bitchBtn = Button(root, text="Start Scraping!", command=startScrape, padx=30,\
                    relief=RAISED, cursor="hand2")
bitchBtn.grid(row=6, column=1)

# Message to send to streamer
streamermessageLabel = Label(root, text="Enter a message", pady=10)
streamermessageLabel.configure(background='#404040', fg='#FFFFFF')
streamermessageLabel.grid(row=7, column=0)

streamermessage = Text(root, height=5)
streamermessage.grid(row=8, column=0)

# Message delay slider
streamermessageLabel = Label(root, text="Select the user delay between messages", pady=10)
streamermessageLabel.configure(background='#404040', fg='#FFFFFF')
streamermessageLabel.grid(row=9, column=0)

messageDelay = Scale(root, from_=2, to=15, orient=HORIZONTAL)
messageDelay.grid(row=10, column=0)

root.mainloop()
