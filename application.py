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

streamerLabel = Label(root, text="Enter a streamer's username", pady=10)
streamerLabel.configure(background='#404040', fg='#FFFFFF')
streamerLabel.grid(row=1, column=0)

streamer = Entry(root, width=40)
streamer.grid(row=2, column=0)
streamer.insert(0, "")

def executeScrape(streamerName, message):
    print("Ready to run scraping process for {}".format(streamerName))
    scrape(streamerName, message)


def startScrape():
    streamerName = streamer.get()
    message = streamermessage.get()
    print("Collected user input values")
    panhandle_thread = threading.Thread(target=executeScrape, name="Scraper", args=[streamerName, message])
    panhandle_thread.start()
    print("Scraper for {} is now running in the background.".format(streamerName))

bitchBtn = Button(root, text="Start Scraping!", command=startScrape, padx=30,\
                    relief=RAISED, cursor="hand2")
bitchBtn.grid(row=2, column=1)

streamermessageLabel = Label(root, text="Enter a message", pady=10)
streamermessageLabel.configure(background='#404040', fg='#FFFFFF')
streamermessageLabel.grid(row=3, column=0)

streamermessage = Entry(root, width=100)
streamermessage.grid(row=4, column=0)
streamermessage.insert(1, "")

root.mainloop()
